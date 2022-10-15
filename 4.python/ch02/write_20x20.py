import openpyxl as excel 

book = excel.Workbook()
sheet = book.active

for y in range (1, 21):
    for x in range (1, 21):
        cell = sheet.cell(y, x)
        cell.value = x*y 

book.save("output/write_20x20.xlsx")