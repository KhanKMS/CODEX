import openpyxl as excel 

book = excel.Workbook()
sheet = book.active

for y in range (1, 100):
    for x in range (1, 100):
        cell = sheet.cell(y, x)
        cell.value = x*y 

book.save("output/write_99x99.xlsx")