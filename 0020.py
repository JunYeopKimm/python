# 초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초


# time=int(input('초를 입력해주세요.'))

# minite = time//60

# seconds = time%60


# print(f'{minite}분 {seconds}초 ')


# 분과 초를 입력하면 초를 출력

# 5분 10초 -> 310초



minute = int(input('분을 입력해주세요.'))

print(f'{minute}분')
small_seconds = int(input('초를 입력해주세요.'))

print(f'{small_seconds}초')


seconds = (minute*60)+small_seconds

print(f'{seconds}초')