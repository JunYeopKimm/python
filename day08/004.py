# 정수변수를 2개 만들어, 나눗셈 결과를 출력하시오
# 예외처리가 필요하면 예외처리하시오.


num1=12
num2=30


def num111(num1:int,num2:int):
    num3=num1/num2
    return num3


try:
    
    num3=num111(num1,num2)
    print(num3)
    

except:
    print('예외처리이이이')