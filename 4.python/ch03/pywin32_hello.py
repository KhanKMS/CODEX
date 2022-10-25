# pywin32(win32com) 라이브러리 불러오기 
# Excel이 설치되어야 하고, pip으로 pywin32 모듈 설치 필요
import win32com.client as com 

# 엑셀 실행하기 
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False 

# 엑셀에 신규 문서 생성
book = app.Workbooks.Add() 
# 활성 시트 가져오기 
sheet = book.ActiveSheet 

# 시트에 값 쓰기 
sheet.Range("B2").Value = "안녕하세요. 이 예제는 win32 COM 객체를 이용했습니다."