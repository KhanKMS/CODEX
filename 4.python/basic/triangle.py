#######################################
#         * 로 삼각형 만들기          #
#######################################

line = int (input("Tree의 높이를 입력하세요(5~30) : "))

for x in range (1, line * 2, 2): 
    # x // y : x를 y로 나눈 몫(정수), ex) 10 // 5 --> 2
    print((" " * ((line * 2 - 1 - x) // 2 )) + ("*" * x)) 