
# import requests
# import pandas as pd
# import json
# import os
# from datetime import datetime


# # Väderinformationen från SMHI:s API

# response = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.022/lat/59.3099/data.json')

# if response.status_code == 200:
#     report = response.json()
# else:
#     print(f'Error fetching products. Status code:{response.status_code}')

# # timeSeries 是一个列表，不能直接使用 report['timeSeries']['validTime']访问
# # 需要通过数字索引或遍历的方式来访问字典中的 validTime

# # Datum Och Hour
# valid_time = [item['validTime'] for item in report['timeSeries']]
# dates = []
# times = []

# # datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ') 对应 ISO 8601 时间格式，转换为 datetime 对象，不是
# # dt_object.date() 提取 datetime 对象中的日期部分。dt_object.time() 提取 datetime 对象中的时间部分。
# # strftime() 日期和时间对象转换为可读的字符串形式，而原来是对象。

# for vd in valid_time:
#     vd_object = datetime.strptime(vd, '%Y-%m-%dT%H:%M:%SZ')
#     dates.append(vd_object.date().strftime('%Y-%m-%d'))
#     times.append(vd_object.time().strftime('%H:%M'))

# # Temperature och RainOrSnow

# temperature = []

# for i in report['timeSeries']:
#     for j in i['parameters']:
#         if j['name'] == 't':
#             temperature.append(j['values'][0])  # 假设 'values' 列表里只有一个值,这样才返回字符串，否则返回列表

# precipitation = []

# for i in report['timeSeries']:
#     for j in i['parameters']:
#         if j['name'] == 'pcat':
#             if j['values'][0] == 0:           
#                 rain = 'Ingen nederbörd'
#             else:
#                 rain = 'Nederbörd'
#             precipitation.append(rain)

# # Longitude och Latitude 

# lon = report['geometry']['coordinates'][0][0]   # 不知道为什么有两个[]
# lat = report['geometry']['coordinates'][0][1]

# # Created
# # strptime 用于解析 ISO 8601 时间格式(2024-10-06T21:30:15Z --> ISO time ).
# # strftime 用于将 datetime 对象格式化为常见的日期时间格式。

# dtime = datetime.strptime(report['approvedTime'], '%Y-%m-%dT%H:%M:%SZ')
# created = dtime.strftime('%Y-%m-%d %H:%M:%S')

# # skapa SMHI DataFrame

# df_SMHI = pd.DataFrame({'Datum': dates,
#                    'Hour': times,
#                    'Temperature': temperature,
#                    'RainOrSnow': precipitation,
#                    'Longitude': lon,
#                    'Latitude': lat,
#                    'Created': created,
#                    'Provider': 'SMHI' 
#                    }).head(24)


# # 为了让生成的 Excel 表格更加美观，包括对齐和颜色，可以使用 Pandas 的 ExcelWriter 结合 XlsxWriter 引擎来实现。
#     # 通过 XlsxWriter，可以轻松地为表格添加格式，如对齐、字体颜色、背景颜色等。

# excel_file = 'Datainsamling_SMHI.xlsx'
# with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
#     df_SMHI.to_excel(writer, index=True, sheet_name='Weather Data')
#     worksheet = writer.sheets['Weather Data']

# # 定义格式
# header_format = writer.book.add_format({'bold': True, 'bg_color': '#FFA07A', 'border': 1, 'align': 'center'})
# cell_format = writer.book.add_format({'border': 1, 'align': 'center'})
# temperature_format = writer.book.add_format({'border': 1, 'align': 'center', 'bg_color': '#FFD700'})  # 温度列高亮
# rain_format = writer.book.add_format({'border': 1, 'align': 'center', 'bg_color': '#ADD8E6'})  # 降水列高亮

#  # 设置列宽
# worksheet.set_column('A:A', 12)  # Datum
# worksheet.set_column('B:B', 10)  # Hour
# worksheet.set_column('C:C', 12)  # Temperature
# worksheet.set_column('D:D', 12)  # RainOrSnow
# worksheet.set_column('E:E', 12)  # Longitude
# worksheet.set_column('F:F', 12)  # Latitude
# worksheet.set_column('G:G', 20)  # Created
# worksheet.set_column('H:H', 15)  # Provider

#  # 应用格式到表头
# for col_num, value in enumerate(df_SMHI.columns.values):
#     worksheet.write(0, col_num, value, header_format)  # 表头









