# 숫자를 2개 입력받아 큰수와 작은수를 출력하시오
# 예 : 5와 8중 큰수는 9, 작은수는 5입니다.


number1 = int(input('숫자1 입력 : '))
number2 = int(input('숫자2 입력 : '))


max_naumber = max(number1,number2)

min_number = min(number1,number2)


print(f'{number1}와 {number2}중 큰 수는 {max_naumber}, 작은 수는 {min_number}입니다. ')
