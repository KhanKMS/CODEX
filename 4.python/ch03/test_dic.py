# 더미 데이터
dummy_data = [ 
    ["이영희", 300],
    ["이영희", 600],
    ["이영희", 200],
    ["박철수", 300],
    ["박철수", 200]
]

# 데이터 분류하기 
users ={} # 딕셔너리 변수 초기화 
for row in dummy_data:
    name = row[0] # row에서 고객명 가져오기 
    # 고객명이 처음 나왔다면 딕셔너리에 추가 
    if name not in users: 
        users[name] = [] # 키: 고객명, 값: 빈리스트 
    # 리스트에 row 추가 
    users[name].append(row)

# 고객별 집계 
for name, rows in users.items():
    print(rows)     # 집계 대상 데이터를 표시 
    total = 0 
    for row in rows:
        total += row[1]
    print(name, total) # 결과 출력