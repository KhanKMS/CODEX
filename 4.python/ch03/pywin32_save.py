# pywin32(win32com) 라이브러리 불러오기 
import win32com.client as com 
import os

# 절대 경로 형식으로 파일명 지정
src_file = os.path.abspath(__file__) # __file__ 파이썬 프로그램 자신이 위치한 절대 경로 저장함.
src_dir = os.path.dirname(src_file)
save_file = os.path.join(src_dir, 'output', 'pywin32_save.xslsx')

# 엑셀 실행하기 
app = com.Dispatch("Excel.Application")
app.Visible = True          # excel 실행 창 보이기 
app.DisplayAlerts = True    # 저장하기 경고창 보이기

# 엑셀에 신규 문서 생성
book = app.Workbooks.Add()
# 활성 시트 가져오기 
sheet = book.ActiveSheet

# 시트에 값 쓰기 
sheet.Range("A1").Value = "미국 수도 : 워싱턴 DC"
sheet.Range("B2").Value = "일본 수도 : 도쿄"
sheet.Range("C3").Value = "중국 수도 : 베이징"

# 파일 저장 
book.SaveAs(save_file)
# 엑셀 종료
app.Quit()