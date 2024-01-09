"""
    1. 값추가   -> input('숫자입력 : ')
    2. 리스트 출력
    999. 종료


"""
list1=[1,2,3,4,5]

while True:
    print("1.값추가")
    print("2.리스트 출력")
    print('3. 리스트의 합계')
    print('4. 리스트의 평균')
    print("999.종료")

    select= int(input('번호선택 : '))
    if select==999:
        print('감사합니다.')
        break
    elif select==1:
        list1.append(int(input('값을 입력해주세요.')))
        
    elif select==2:
        print(list1)
    elif select==3:
        c=sum(list1)
        print(f'입력값의 합계 : {c}')
    elif select==4:
       print(f'입력값의 평균 : {sum(list1)/len(list1)}')
    else : 
        print('다시 입력해주세요')
