import openpyxl as xl 
book = xl.Workbook()
sheet = book.active 

import datetime 
dt = datetime.datetime ( 
    year=2023, month=4, day=5, 
    hour=11, minute=22, second=33)
sheet.append([dt, dt, dt, dt, dt, dt, dt])

# 2022/04/05로 표시하기 
sheet["A1"].number_format = 'yyyy\/mm\/dd'
# 2022년 4월 5일로 표시하기
sheet["B1"].number_format = 'yyyy년 mm월 dd일'
# 11:22:33 으로 표시하기 
sheet["C1"].number_format = 'hh:mm:ss'
# 04/05 11:22:33 으로 표시하기 
sheet["D1"].number_format = 'mm/dd hh:mm:ss'
# Apr/04로 표기
sheet["E1"].number_format = 'mmm\/d'
# Apr/04 Wednesday로 표기
sheet["E1"].number_format = 'mmm\/d dddd'
# 2022/04/05 수요일 표기
sheet["F1"].number_format = 'mm\/dd ([$-411]ddd)'


book.save("output/cellformat_datetime.xlsx")