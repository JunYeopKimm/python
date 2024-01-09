list1=[]

while True:
    print('========메뉴 선택======')
    print('1.숫자 추가 ,2.숫자 출력,3. 합계, 4. 값으로 삭제, 999.종료')
    select = int(input('번호를 입력해주세요.'))

    if select ==1:
        append2=int(input('추가할 값을 입력해주세요.'))
        list1.append(append2)

    elif select ==2:
        print(list1)

    elif select == 3:
        print(f'합계 : {sum(list1)}')

    elif select == 4:
        val=int(input('삭제할 값 입력'))
        if val in list1:
            list1.remove(val)

    elif select ==999:
        print('종료되었습니다.')
        break
    else :
        print('감사합니다.')