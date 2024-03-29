import openpyxl as excel 
import datetime 

in_file = './input/stock-data.xlsx'
out_file = './output/stock_date_format.xlsx'
cell_format = 'yyyy\/mm\/dd'

# 메인 처리 
def shorten_date(in_file, out_file):
    # 제고표 열기
    book = excel.load_workbook(in_file)
    # 모든 시트 확인하기 
    for sheet in book.worksheets:
        # 모든 행 확인하기 
        for row in sheet.iter_rows():
            # 모든 쉘 확인하기 
            for cell in row:
                check_cell(cell)
    # 저장 
    book.save(out_file)

# 쉘 표시 형식 확인하기
def check_cell(cell):
    # 쉘이 날짜 형식이면 치환 
    if type(cell.value) is datetime.datetime:
        cell.number_format=cell_format

if __name__ == '__main__':
    shorten_date(in_file, out_file)