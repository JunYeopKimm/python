# 섭씨를 입력받아 화씨로 출력하시오

# sub=int(input('섭씨를 입력하시오'))

# hwa=(sub*9/5)+32

# print(f'섭씨 {sub}도는 화씨 {hwa}도')


# 온도와 종류를 입력받으시오
# 예) 온도 : 35
# 예) 종류:섭씨
# 종류가 섭씨면 온도를 화씨로 변환, 아니면 섭씨로 변환 


ondo = int(input('온도를 입력해주세요.'))

kind = input('종류를 입력해주세요.')


hwa=(ondo*9/5)+32

sub=(ondo-32)/(9/5)  




if kind=='섭씨':
    print(f'섭씨 {ondo}도는 화씨 {hwa}도')
else:
    print(f'화씨 {ondo}도는 섭씨 {sub}도')



