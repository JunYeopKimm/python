# for 문
# hello를 for 를 이용해 3번 출력하기 
# for x in (1,2,3):
#     print('hello')


# for x in range(3):
#     print(x)


# for를 이용해서 0~10사이의 짝수 출력

# for x in range(1,10):         1~10까지


for x in range(11):
    if x%2==0:
        print(x)
    else : 
        pass 



# 1~5까지의 합계를 출력
# 파이썬 변수는 타입이 없다
result=0                    #for 안에 입력 시 반복하면서 0으로 값 초기화. 따라서 for문 밖에 작성
for z in range(1,6):
    
    result=result+z
 
print(result)               #만약 들여쓰기 시 더하면서 출력됨 

