# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오

number1=int(input('숫자를 입력하시오.'))


if number1%3==0:
    print(f'{number1}는 3의 배수입니다.')
else :
    print(f'{number1}는 3의 배수가 아닙니다.')





# 점수를 입력받아 90점 이상이면 우수, 70점이상이면 패스, 미만이면 낙제라고 출력하시오.
    


jumsu1=int(input('점수를 입력하시오'))

if jumsu1>=90:
    print('우수')
elif jumsu1>=70:
    print('패스')
else : 
    print('낙제')