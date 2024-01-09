# 물품 CRUD
# 물품이란 무엇인가?
todos=[
    {'tno':1, 'title':'할일1','reg_day':'2024-01-09','finish':False},
    {'tno':3, 'title':'할일3','reg_day':'2024-01-09','finish':False}
]
tno=2
# Read: 전체읽기, 1개 읽기 
for todo in todos:
    print(todo)



# 할일 번호를 입력받아 할일을 찾아서 출력 
    

work=int(input('찾을 할일의 번호를 입력해주세요.'))

findd = False
for x in todos:
    if x['tno']==work:
        print(x)

        findd = True
        break
if findd==False:
    print('할일을 찾을 수 없습니다. ')
