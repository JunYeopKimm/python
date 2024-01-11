# 할일은 할일번호, 할일, 완료여부로 구성 
todos=[]
# 할일 : 할일번호, 할일, 완료
todo1={
    'tno':1,'title':'자바공부','finish':False
}
todo2={
    'tno':2,'title':'스프링공부','finish':False
}
todo3={
    'tno':3,'title':'파이썬공부','finish':False
}
tno=4

todos.append({'tno':1,'title':'자바공부','finish':False})
todos.append({'tno':2,'title':'스프링공부','finish':False})
todos.append({'tno':3,'title':'파이썬공부','finish':False})


def print_list():
    for x in todos:
        print(x)




# 함수 안에서 함수 밖에 있는 변수를 사용하려면 사용한다고 적어준다 
def add_todo():
    global tno
    addd=input('추가 할 값을 입력해주세요')
    todos.append({'tno':tno,'title':'title','finish':False})
    tno=tno+1
 

def update_todo():
    update_number=int(input('변경할 값을 입력해주세요.'))


def delete_todo():
    delete_num=int(input('삭제할 번호를 입력해주세요.'))






while True:
    print("====할일관리====")
    print('1:목록, 2: 추가, 3: 변경, 4:삭제, 999:종료')
    select = input('메뉴 선택: ')
    if select =='1':
        print_list()
    elif select=='2': 
        add_todo()
    elif select=='3':
        update_todo()
    elif select=='4':
        delete_todo()
    elif select=='999':
        print('이용해주셔서 감사합니다.')
        break