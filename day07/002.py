todos = [
    {"tno": 1, "title": "자바공부", "finish": False},
    {"tno": 3, "title": "파이썬공부", "finish": False}
]
tno = 4
# Create
# title = input('할일 입력 : ')
# todo={"tno":tno,"title":title,"finish":False}
# todos.append(todo)
# tno=tno+1

# Read : for로 todos 출력
for todo in todos:
    print(todo)


# update : tno로 찾아 finish를 toggle
#       못 찾으면 아무것도 하지 않는다

# 꺼내서 찾을땐 무조건 for ~~~
    # if
    # 꼭 외우기

#     input_tno = int(input('변경할 할일 번호:'))
# for todo in todos:
#     if todo['tno'] == input_tno:
#         todo['finish'] = not todo['finish']
#         break

# print(todos)


# 삭제 : 입력한 tno에 해당하는 todo를 todos에 찾는다 
# 
del_tno = int(input('삭제할 번호 입력 : '))
for todo in todos:
    if todo["tno"]==del_tno:
        todos.remove(todo)      # remove는 필수적으로 인자값을 무조건 받아야함 
        
        
        
print(todos)