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

# timeSeries är en lista och kan inte nås direkt med report['timeSeries']['validTime']
# Behöver komma åt validTime i ordboken genom numerisk indexering eller genomgång

# Datum Och Hour
valid_time = [item['validTime'] for item in report['timeSeries']]
dates = []
times = []

# datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ') Motsvarar ISO 8601 tidsformat, konverterat till datetime objekt.
# dt_object.date() Extrahera datumdelen av datetime objekt.
# dt_object.time() Extrahera timedelen av datetime objekt.dt_object。
# strftime() Konverterar date och time objekt till strängform som kan läsas av människor, istället för originalobjekten.

for vd in valid_time:
    vd_object = datetime.strptime(vd, '%Y-%m-%dT%H:%M:%SZ')
    dates.append(vd_object.date().strftime('%Y-%m-%d'))
    times.append(vd_object.time().strftime('%H:%M'))

# Temperature och RainOrSnow

temperature = []

for i in report['timeSeries']:
    for j in i['parameters']:
        if j['name'] == 't':
            temperature.append(j['values'][0])      # "values": [13.4]
            # Antag att det bara finns ett värde i listan 'values', så en sträng returneras, annars returneras en lista.

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

lon = report['geometry']['coordinates'][0][0]   # "coordinates": [[18.038218, 59.315406]]  två [[]] square brackets
lat = report['geometry']['coordinates'][0][1]

# Created
# strptime Används för att analysera ISO 8601 tidsformat.(2024-10-06T21:30:15Z --> ISO time ).
# strftime Används för att formatera datetime-objekt till vanliga datetime-format.

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



# Väderinformationen från OpenWeatherMap:s API

response2 = requests.get('https://api.openweathermap.org/data/3.0/onecall?lat=59.3099&lon=18.022&exclude=minutely&units=metric&appid=3c37a33f0f77b29b4ff106427d669a72')

if response2.status_code == 200:
    report2 = response2.json()
else:
    print(f'Error fetching products. Status code:{response2.status_code}')

# Datum Och Hour

# Timestamp: "dt": 1728237600， Behöver konverteras till normalt format.
# Metoden fromtimestamp() kan bara acceptera en tidsstämpel åt gången, 
# och 'timestamp' variabel är en lista och kan inte skickas direkt till fromtimestamp().
timestamp = [item['dt'] for item in report2['hourly']]
valid_time2 = [datetime.fromtimestamp(ts) for ts in timestamp]     

dates2 = []
times2 = []
for dt in valid_time2:
    dt_date = dt.date()
    dt_time = dt.strftime('%H:%M')     # Använd strftime('%H:%M') för att ta bort sekunderna och visa bara timmar och minuter.
    dates2.append(dt_date)
    times2.append(dt_time)

# Temperature och RainOrSnow   --> Celsius temperatur

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



# Sammanfoga rad för rad med concat(), skapa ny index.
df = pd.concat([df_SMHI, df_OpenWeatherMap], axis=0, ignore_index=True)
# print(df)



def hämta_data():
    api = int(input("vill du Hämta data från:\n 1. SMHI \n 2. OpenWeatherMap \n 3. båda\n"))
    if api == 1:
        # Ändra index för att börja från 1
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
        hämta_data()

def skriv_ut_prognosen():
    api = int(input("vill du skriva ut data från:\n 1. SMHI \n 2. 3OpenWeatherMap\n"))

    if api == 1:
        print("Hämta och skriv ut prognos från SMHI:")
        print(f"Prognos från SMHI {df_SMHI['Datum'].iloc[0]}:")
        
        # Använd DataFrame.iterrows() för att iterera över varje rad så att du kan komma åt både index och rad data.
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
    print('9. Avsluta')
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

