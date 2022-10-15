import openpyxl as excel 

book = excel.load_workbook("output/write_cellname.xlsx")
sheet = book.active 

for row in sheet["B2":"D4"]:
    print([c.value for c in row]) 
# 파이썬 리스트 압축 기법 응용 코드 