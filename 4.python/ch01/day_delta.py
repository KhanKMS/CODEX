from datetime import datetime, timedelta

base_t = datetime(2025, 2, 27)
# 기준일 설정 
t = base_t + timedelta(days=3)
# 기준일 + 3일 날짜 계산 
print(t.strftime('%Y/%m/%d'))