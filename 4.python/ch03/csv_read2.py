import openpyxl as excel
import csv

book=excel.Workbook()
sheet=book.active

# 파일을 열어, reader 가져오기 
with open('./input/items2.csv', encoding='ansi') as f: 
    reader = csv.reader(f)
    # 헤더 행 건너뛰기
    head = next(reader)
    # 한 행씩 조사하기 
    total = 0
    for row in reader:
        # csv의 한행 요소를 각 변수에 담기 
        name, price, cnt, subtotal = row 
        print(name, price, cnt, subtotal)
        total += int(subtotal)
    # 합계를 출력
    print("합계:", total, "원")