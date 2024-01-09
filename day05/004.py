list1=[3,'hello',5>3,True]
tuple1=tuple(list1)

# CRUD - 삭제는 del 연산자
# method : 객체(파이썬을 구성하는 부품)에 소속된 함수 
list1.append(100)
list1[0]=list1[0]*10
print(list1)

del list1[0]
print(list1)

