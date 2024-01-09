# 숫자를 입력받아 음수면 양수로, 양수면 음수로 바꿔 출력


number1 = int(input('숫자를 입력하세요.'))

if number1>0:
    print(-(number1))
else:
    print(-(number1))




# 길이를 입력받아 센티미터면 인치로, 인치면 센티미터로 변경
# 1인치=2.54 센티미터
    

lenth=int(input('길이를 입력하세요'))
mm=input('종류를 입력해주세요.')


if mm=='센티미터':
    print(lenth/2.54)
elif mm=='인치':
    print(lenth*2.54)
else:
    print('"센티미터"나 "인치" 로 입력해주세요.')


