# 타입, 변수, 산술 연산 (+,-,*,   /,//,   %)
# 조건문(if문)
# a=10
# if a>5:
#     print('5보다 큽니다')
#     print('if가 참이면 동작')

# print('if와 관계없다.')


money = 5000
if money>=4500:
    print('떡볶이를 먹어요. ')
    print('행복합니다. ')
else:
    print('집에 가서 물이나 먹읍시다.')
print('집에 왔어요')

# 점수를 입력받아 70점 이상이면 합격, 아니면 불합격이라고 출력\
# 출력이 끝나면 "수고하셨습니다"라고 출력

# scre=int(input('점수를 입력해주세요 : '))

# if score>=70:
#     print("합격")
# else:
#     print('불합격')
# print('"수고하셨습니다."')o



# kor에 75, eng에 80
# 평균이 70이상이면 합격, 아니면 불합격


kor=int(input('국어 점수 입력 : '))
eng=int(input('영어 점수 입력 : '))

avg = (kor+eng)/2


if avg>=70:
    print('합격')
else:
    print('불합격')




