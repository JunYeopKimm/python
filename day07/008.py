# 정수 2개를 인자로 받아 덧셈 후 출력하는 함수를 정의하고 호풀 

def summ(a:int|float,b:int|float):
    print(a+b)

summ(10,22)
summ(10.32,22.67)


def sum2(a:int|float,b:int|float):
    # return 결과 -> 함수를 종료하고 결과로 바꿔라 
    return a+b


print(sum2(3,4))

result = sum2(3,4)