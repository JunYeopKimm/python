# 숫자 리스트 -> 추가, 목록, 합계, 변경, 삭제   함수 버전






list1=[]
def print_menu():
    print("=====CRUD=====")
    print('1.추가 , 2. 목록 , 3. 합계, 4.삭제 , 999.삭제')


def input_menu():
    print(input('메뉴를 선택해주세요'))


def appendd_numbers():
    iinput=input('추가 할 값을 입력해주세요.')
    iinput.append(list1)

def list_numbers():
    for x in list1:
        print(x,num=' ')
    print()


def summ_numbers():
    print(sum(list1))

def deletee_numbers():
    value=input('삭제할 값 입력')
    index=0
    for x in list1:
        if value==x:
            del x[index]
        index=index+1



while True:
    print_menu()

    select=input_menu()

    if select==1:
        appendd_numbers()
    elif select==2:
        list_numbers()
    elif select==3:
        summ_numbers()
    elif select==4:
        deletee_numbers()
    elif select ==999:
        break
