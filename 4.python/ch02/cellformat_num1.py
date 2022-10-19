# openpyxl 모듈을 xl 이란 이름으로 가져오기 
import openpyxl as xl 
# 새로운 워크북을 생성
book = xl.Workbook()
# 현재 활성화된 시트를 사용함. 
sheet = book.active 

# A1, B1, C2 셀에 val 값을 설정함
val = 3.14159
sheet.append([val, val, val])

# 소수점 이하를 생락해 표시하기
sheet["A1"].number_format = '0'
# 소수점 이하 둘째자리까지 표시 
sheet["B1"].number_format = '0.00'
# 소수점 이하 넷째자리까지 표시 
sheet["C1"].number_format = '0.0000'

# format_num1.xlsx 파일로 저장하기
book.save("output/cellformat_num1.xlsx")