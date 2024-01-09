# 임의로 가정
# 남자의 적정체중은 키-100, 여자의 적정체중은 키-105
# 키를 입력받아 적정체중을 출력하시오 




lengh=int(input('키를 입력해주세요.'))
gender=input('성별을 입력해주세요')
 

if gender=='남자':
    print("남자의 적정 체중은 ",lengh-100,'kg 입니다.')
elif gender=='여자':
    print("여자의 적정 체중은 ",lengh-105,'kg 입니다.')
else:
    print('다시 입력해주세요.')