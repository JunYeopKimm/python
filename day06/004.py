# f문자열
# replace : 치환 
str4="010-1111-2222"
# 함수 : 소속없는 함수 + 소속있는 메소드
print(len(str4))
# method : 특정 타입 소속 -> 타입은 함수도 가질 수 있다 
# 문자열 메소드는 새로운 문자열을 만든다 
str4.replace("-",'.')
str4=str4.replace("-",'.')
str4=str4.replace("1111",'xxxx')
print(str4)


j1="971011-1231231"

j1=j1.replace("231231",'xxxxxx')
print(j1)

print(j1.replace(j1[8:], '******'))
str5='   aa   aa     '
print(str5.strip())