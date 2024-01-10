# 숫자 리스트 -> 추가, 목록, 합계, 변경, 삭제   함수 버전



numbers=[1,3,5]

def print_menu():
    print('#### 숫자 CRUD ####')
    print('1:추가, 2:목록 ,3:삭제, 999:종료')


def add_value():
    value = int(input('값 입력'))
    numbers.append(value)


def input_select():
    return input('메뉴를 선택')

def list_numbers():
    for num in numbers:
        print(num,end=" ")
    print()

def delete_numbers():
    value = int(input("삭제할 값 입력 : "))

    index = 0
    for num in numbers:
        if value==num:
            del numbers[index]
        index=index+1

while True:
    print_menu()
    select = input_select()
    if select == '1':
        add_value()
    elif select =='2':
        list_numbers()
    elif select =='3':
        delete_numbers()
    elif select =='999':
        break


