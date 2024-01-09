# 몇일인지 입력받아 몇개월 며칠인지 출력
# 333일 -> 11개월 3일
# 코드에 값이 직접 나타나는 것 : literal
# 상수는 대문자로 


d_day = int(input('몇일인지 입력 : '))

month= d_day//30

day= d_day%30


print(f'{month}개월 {day}일')