numbers=[100,300,500,700]
# 삭제작업. 내가 알고 싶은 값 :2

# 값을 입력받아 위치를 찾아서 삭제 
value=500


index = 0
for x in numbers:
    if value==x:
        print(index)
    index=index+1
