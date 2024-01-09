# Set - 중복불가능하고 순서가 없다
#       - 정렬된것처럼 보여도 우연일 뿐
set1={1,2,3,4}
print(set1)
set1.add(5)
print(set1)


# 리스트나 튜플은 중복이 가능하고 순서가 있다 
list1 = [1,3,4,6,1,4,2]

set2 = set(list1)

list1=list(set2)
print(list1)