import openpyxl as excel 

book=excel.Workbook()
sheet=book.active 

for i in range(10):  # 0부터 9까지 10번 반복함 
    i=i+1
    sheet.cell(row=i, column=1, value=i)

book.save("output/write_column.xlsx")