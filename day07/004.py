numbers=[1,3,5,7]

# 숫자를 입력받앙 그 숫자가 numbers에 있는 지 출력 
# 성공과 실패의 조건이 다르다 -> if ~ else~가 아니다
num=7
isFind = False
for x in numbers:
    if x==num:
        print(True)
        isFind=True
if isFind == False:
    print(False)
else : 
    print(True)