# 제어문 control : 순서를 바꾼다 
# 조건 : 결과가 이럴수도 저럴수도 있다 
# jumsu가 짝수인지 홀수인지 출력해라 (2의 배수)
# 나눠서 나머지가 0이면 배수 

# jumsu = 75

# if jumsu%2==0:
#     print('짝수입니다.')
# else: 
#     print('홀수입니다. ')

# print('수고하셨습니다.')


# 점수가 90점 이상이면 우수, 70점이상 합격, 미만이면 재시험 


jumsu=int(input('점수 입력 : '))



if jumsu>=90:
    print('우수')
elif jumsu>=70:
    print('합격')
else: 
    print('재시험')

