jumin='961011-1021023'

gender=jumin[7]

# 남자인지 여자인지 출력
if gender =='1':
    print('남자')
else:
    print('여자')

# 둘중의 하나 if문을 한줄로 -> 삼항연산자 
# 복잡한 조건 삼항연산은 쓰지말자 -> 스파게티 코드
print("남자" if gender=='1' else '여자')

# gender가 1또는 3또는 5면 남자 2또는 4또는 7이면 여자 

# junmin1 = (input('주민번호를 입력해주세요'))
# gender1=junmin1[7]

# print('남자' if gender1 in('1','3','5') else '여자')



# 주민번호로 나이 출력하기 
# 1. 올해의 년도
# 2. 태어난 년도 
#  주민번호 앞 2자리를 슬라이싱한다
#  주민번호 7번째가 '1','2' -> '19'+year

jumin2=(input('주민번호를 입력해주세요'))



year1 = '19'

year2 = '20'

year4 = jumin2[7]
 
year5 = jumin2[0:2]



print(year5)

if year4=='1' or year4=='2':
    print(year1+year5)
elif year4=='3' or year4=='4':
    print(year2+year5)
else:
    print('다시입력해주세요')




