# string 타입 
str1='10'
str2='3.14'
str3='홀짝홀짝홀짝홀짝'

# 연산
print(str1+str2)        #연결
print(str1*10)          #반복
# 인덱스 연산 ->시퀀스와 동일 
print(str3[0])


# slicing 연산 -> 시퀀스와 동일 
print(str3[0:3])
print(str3[3:])
str4="72568"
print(str4[0:3])    
print(str4[1:])     # 2568
print(str4[::2])

str5='0123456789'
# 홀수만 입력 
# 3의 배수만 입력

print(str5[1::2])       #13579
print(str5[3::3])       #369   
print(str5[::3])        #0369

# 내장함수 : len 
print(len('hello'))
# print(len(5))

# 문자열은 변경불가능(immutable <-> mutable)
# str6[3] = 'hello'       #변경 불가능 
list6=['h','e','l','l','o']

# str6[0] = 'z'
list6[0] = 'z'
