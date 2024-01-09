# 숫자를 입력받아 CR(합계, 평균)UD 
# 메뉴를 띄운다(1. 숫자추가, 2. 숫자출력, 999. 종료)




list1=[]

while True:
    print('=====메뉴선택======')
    print('(1.추가, 2.출력,3.합계, 4.평균 , 5. 삭제, 999. 종료)')
    select = int(input('번호를 입력해주세요.'))
    if select ==1:
        append1=int(input('추가할값을 입력해주세요.'))
        list1.append(append1)
    elif select ==999:
        print('종료 되었습니다.')
        break
    elif select ==2:
        print(list1)
    elif select ==3:
        print(f'합계 : {sum(list1)}')

    elif select ==4:
        print(f'평균 : {sum(list1)/len(list1)}')

    elif select ==5:
        val = int(input('삭제할 값 입력'))
        if val in list1:        # 값이 있다면 30줄 실행 
            list1.remove(val)

    else :
        print('다시 입력해주세요')

print('감사합니다.')
