# 월급을 입력받아 1년치 소득세와 소득세를 제외한
# 연봉 실수령액 출력 출력하시오
# 소득세율은 3.3%

salary=int(input('월급을 입력하시오'))


year_salary = salary*12

print(year_salary)

segum=float(year_salary)*0.033


print(segum)

real_salary=year_salary-segum

print(real_salary)
