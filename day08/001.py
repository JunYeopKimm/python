# 나이를 입력받아 성년, 또는 미성년을 리턴하는 함수 




def is_adult(age:int):
    if age>=18:
        return True
    else : 
        return False
    

age=25

if is_adult(age)==True:
    print("당신은 출입가능합니다.")
else :
    print('당신은 출입불가합니다.')