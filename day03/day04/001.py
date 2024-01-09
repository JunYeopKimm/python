# 75, 80, 70이라는 국어 점수가 있다 -> 집합 타입(sequence)
# 값 하나를 저장 : int, float, str, bool
# 값 여러개를 저장 : list,tuple,dictionary,set


# kor1= 75
# kor2= 80
# kor3= 70


# print(kor1)
# print(kor2)
# print(kor3) 


kor=[75,80,70]
# kor의 타입 출력
print(type(kor))
print(kor[0])
print(kor[1])
print(kor[2])

# 조건문, 반복문 
# kor 리스트의 원소를 하나씩 꺼내서 x에 담는다
for x in kor:
    print(x) 

# 리스트는 변경가능하고 튜플은 변경불가능
list1 = ["사과","귤","수박"]
tuple1 = ("사과","귤","수박")

# Create Read Update Delete


# 리스트, 튜플 print하기

for x in list1:
    print(x)


for z in tuple1:
    print(z)


