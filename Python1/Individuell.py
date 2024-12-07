import requests
import pandas as pd
import json
import os
from datetime import datetime


# Väderinformationen från SMHI:s API

response = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.022/lat/59.3099/data.json')

if response.status_code == 200:
    report = response.json()
else:
    print(f'Error fetching products. Status code:{response.status_code}')

# timeSeries 是一个列表，不能直接使用 report['timeSeries']['validTime']访问
# 需要通过数字索引或遍历的方式来访问字典中的 validTime

# Datum Och Hour
valid_time = [item['validTime'] for item in report['timeSeries']]
dates = []
times = []

# datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ') 对应 ISO 8601 时间格式，转换为 datetime 对象
# dt_object.date() 提取 datetime 对象中的日期部分。dt_object.time() 提取 datetime 对象中的时间部分。
# strftime() 日期和时间对象转换为可读的字符串形式，而原来是对象。

for vd in valid_time:
    vd_object = datetime.strptime(vd, '%Y-%m-%dT%H:%M:%SZ')
    dates.append(vd_object.date().strftime('%Y-%m-%d'))
    times.append(vd_object.time().strftime('%H:%M'))

# Temperature och RainOrSnow

temperature = []

for i in report['timeSeries']:
    for j in i['parameters']:
        if j['name'] == 't':
            temperature.append(j['values'][0])  # 假设 'values' 列表里只有一个值,这样才返回字符串，否则返回列表

precipitation = []

for i in report['timeSeries']:
    for j in i['parameters']:
        if j['name'] == 'pcat':
            if j['values'][0] == 0:           
                rain = 'Ingen nederbörd'
            else:
                rain = 'Nederbörd'
            precipitation.append(rain)

# Longitude och Latitude 

lon = report['geometry']['coordinates'][0][0]   # 不知道为什么有两个[]
lat = report['geometry']['coordinates'][0][1]

# Created
# strptime 用于解析 ISO 8601 时间格式(2024-10-06T21:30:15Z --> ISO time ).
# strftime 用于将 datetime 对象格式化为常见的日期时间格式。

dtime = datetime.strptime(report['approvedTime'], '%Y-%m-%dT%H:%M:%SZ')
created = dtime.strftime('%Y-%m-%d %H:%M:%S')

# skapa SMHI DataFrame

df_SMHI = pd.DataFrame({'Datum': dates,
                   'Hour': times,
                   'Temperature': temperature,
                   'RainOrSnow': precipitation,
                   'Longitude': lon,
                   'Latitude': lat,
                   'Created': created,
                   'Provider': 'SMHI' 
                   }).head(24)

# print(df_SMHI)


# Väderinformationen från OpenWeatherMap:s API

response2 = requests.get('https://api.openweathermap.org/data/3.0/onecall?lat=59.3099&lon=18.022&exclude=minutely&units=metric&appid=3c37a33f0f77b29b4ff106427d669a72')

if response2.status_code == 200:
    report2 = response2.json()
else:
    print(f'Error fetching products. Status code:{response2.status_code}')

# Datum Och Hour

# 时间戳："dt": 1728237600， 需转化为正常格式
# fromtimestamp() 方法一次只能接受一个时间戳，而 timestamp 变量是一个列表，不能直接传递给 fromtimestamp()。
timestamp = [item['dt'] for item in report2['hourly']]
valid_time2 = [datetime.fromtimestamp(ts) for ts in timestamp]     # 输出的是对象 格式奇怪

dates2 = []
times2 = []
for dt in valid_time2:
    dt_date = dt.date()
    dt_time = dt.strftime('%H:%M')           # 使用 strftime('%H:%M') 可以去掉秒，只显示小时和分钟。
    dates2.append(dt_date)
    times2.append(dt_time)

# Temperature och RainOrSnow

temperature2 = []
for i in report2['hourly']:
    temperature2.append(i['temp'])

precipitation2 = []
for i in report2['hourly']:
    if i == 0:
        rain = "Ingen nederbörd"
    else:
        rain = "Nederbörd"
    precipitation2.append(rain)


# Created

created2 = datetime.fromtimestamp(report2['current']['dt'])



df_OpenWeatherMap = pd.DataFrame({'Datum': dates2,
                                'Hour': times2,
                                'Temperature': temperature2,
                                'RainOrSnow': precipitation2,
                                'Longitude': report2['lon'],
                                'Latitude': report2['lat'],
                                'Created': created2,
                                'Provider': 'OpenWeatherMap' 
                   }).head(24)

# print(df_OpenWeatherMap)


# 使用 concat() 按行合并
df = pd.concat([df_SMHI, df_OpenWeatherMap], axis=0, ignore_index=True)
# print(df)



def hämta_data():
    api = int(input("vill du Hämta data från:\n 1. SMHI \n 2. OpenWeatherMap \n 3. båda\n"))
    if api == 1:
        # 将索引改为从 1 开始
        df_SMHI.index = df_SMHI.index + 1
        excel_doc = df_SMHI.to_excel('Datainsamling_SMHI.xlsx', index=True)
    elif api == 2:
        df_OpenWeatherMap.index = df_OpenWeatherMap.index + 1
        excel_doc = df_OpenWeatherMap.to_excel('Datainsamling_OpenWeatherMap.xlsx', index=True)
    elif api == 3:
        df.index = df.index + 1
        excel_doc = df.to_excel('Datainsamling.xlsx', index=True)
    else:
        print('Ogiltigt val, försök igen.')

def skriv_ut_prognosen():
    api = int(input("vill du skriva ut data från:\n 1. SMHI \n 2. 3OpenWeatherMap\n"))

    if api == 1:
        print("Hämta och skriv ut prognos från SMHI:")
        print(f"Prognos från SMHI {df_SMHI['Datum'].iloc[0]}:")

        # 使用DataFrame.iterrows()来迭代每一行，这样可以同时访问索引和行数据
        for index, row in df_SMHI.iterrows():
            if row['Datum'] == df_SMHI['Datum'].iloc[0]:
                print(f"{row['Hour']} {row['Temperature']} grader {row['RainOrSnow']}")
            else:
                break              
        print(f"Prognos från SMHI {row['Datum']}:")
        for idx, row in df_SMHI.iterrows():
            if row['Datum'] != df_SMHI['Datum'].iloc[0]:
                print(f"{row['Hour']} {row['Temperature']} grader {row['RainOrSnow']}")              
        
    elif api == 2:
        print('Hämta och skriv ut prognos från OpenWeatherMap:')
        print(f"Prognos från OpenWeatherMap {df_OpenWeatherMap['Datum'].iloc[0]}:")

        # 使用DataFrame.iterrows()来迭代每一行，这样可以同时访问索引和行数据
        for index, row in df_OpenWeatherMap.iterrows():
            if row['Datum'] == df_OpenWeatherMap['Datum'].iloc[0]:
                print(f"{row['Hour']} {row['Temperature']} grader {row['RainOrSnow']}")
            else:
                break              
        print(f"Prognos från OpenWeatherMap {row['Datum']}:")
        for idx, row in df_OpenWeatherMap.iterrows():
            if row['Datum'] != df_OpenWeatherMap['Datum'].iloc[0]:
                print(f"{row['Hour']} {row['Temperature']} grader {row['RainOrSnow']}") 

    else:
        print('Ogiltigt val, försök igen.')
        skriv_ut_prognosen()

def main():
    
    print('MENY:')
    print('1. Hämta data')
    print('2. Skriv ut senaste prognosen')
    print('3. Avsluta')
    val = int(input('Välj ett alternativ (1-3):'))
    
    if val == 1:
        hämta_data()
    elif val == 2:
        skriv_ut_prognosen()
    elif val == 9:
        print('Ha en trevlig dag!')
    else:
        print('Ogiltigt val, försök igen.')
        main()
    
if __name__ == '__main__':
    main()
















