# 1~10까지의 합계

result=0                    # 결과값을 int로 설정하기 위해 초기 값 0으로 설정
for x in range(1,11):
    result=result+x         #result변수에 x를 더하면서 반복 ex)1+2+3+4+5+5+6....
    
print(result)               #for문 밖으로 나온 뒤 result값 출력 



# 1~10까지의 3의 배수 출력 


for x in range(1,11):
    if x%3==0:              # 3으로 나눈 나머지가 0이므로 3의 배수가 출력 하게끔 설정 
        print(x)
    else:
        pass


for i in range(1,11):
    if i%3!=0:
        continue            # continue 는 반복문을 skip하는 기능. break와 다른 개념. break는 중단 후 빠져나가는 것 
    print(i)



# 1~10사이의 3의 배수의 합계
    
result=0
for x in range(1,11):
    if x%3==0:
        result=result+x
    else:
        pass                # 3이 아닌 수들은 pass를 사용해 건너뛰기 
print(result)



# 1~100사이의 3과 5의 공배수를 출력 

for x in range(1,101):
    if x%5==0 and x%7==0:
        print(x)
    else:
        pass


# 1~100사이의 5의 배수와 7의 배수를 출력 단 공배수는 제외

for x in range(1,101):
    if x%5==0 or x%7==0:
        
        if x%5==0 and x%7==0:
            pass
        
print(x)