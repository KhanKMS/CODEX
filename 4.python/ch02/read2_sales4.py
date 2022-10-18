import openpyxl as excel 
#매출명세서 엑셀 파일을 읽어 들이고, 엑셀 수식을 사용함. 
book = excel.load_workbook(
    "input/monthly_sales2.xlsx", data_only=True)
sheet = book.active     # 현재 열린 시트를 sheet에 저장함. 
# A3부터 F999까지 범위 데이터를 rows에 저장함. 
rows = sheet["A3":"F999"]
for row in rows: 
    # 각 셀의 값을 values 리스트에 저장함. 
    values = [cell.value for cell in row]
    # 반복 순환하다가 None(비어있는 셀)이 생기면 순환을 빠져나감. 
    if values[0] is None : break 
    # 리스트 값을 출력함. 
    print(values)
