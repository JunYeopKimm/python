# 주민번호를 입력받아 성별을 출력
jumin = '970702-1231231'

jumin[7]
print
if jumin[7]=='1' or jumin[7]=='3':
    print('남자')
elif jumin[7]=='2' or jumin[7]=='4':
    print('여자')
else:
    print('다시입력해주세요.')
