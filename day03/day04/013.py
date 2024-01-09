# 주민번호를 입력받아 태어난 년도를 계산해 나이를 출력하시오


jumin = input("주민번호를 입력하세요")








jumin2=jumin[0:2]

jumin1 = jumin[6:7]


if jumin1 == '1' or jumin1 == '2':
    print("19"+jumin2)
elif jumin1 in ('3','4'):
    print("20"+jumin2)




print(jumin1) 

