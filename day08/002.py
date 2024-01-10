# 두 숫자를 입력받아 큰 수를 가리는 함수 


def large_numbers(numbers1:int,numbers2:int):
    
    if numbers1>numbers2:
        return numbers1
    elif numbers2>numbers1:
        return numbers2
    else :
        return "다시 입력해주세요"
    









def abs_numbers(a:int):
    if a<0:
        return -a
    return a

d=abs_numbers(-20)
print(d)    