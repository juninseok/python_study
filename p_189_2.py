#3.조건문 도전문제 - 나누어 떨어지는 숫자

number = int(input("정수를 입력해주세요: "))

if (number % 2) == 0:
    print("{}은 2로 나누어 떨어지는 숫자입니다.".format(number))

else:
    print("{}는 2로 나누어 떨어지는 숫자가 아닙니다.".format(number))

if (number % 3) == 0:
    print("{}은 3로 나누어 떨어지는 숫자입니다.".format(number))

else:
    print("{}는 3로 나누어 떨어지는 숫자가 아닙니다.".format(number))

if (number % 4) == 0:
    print("{}은 4로 나누어 떨어지는 숫자입니다.".format(number))

else:
    print("{}는 4로 나누어 떨어지는 숫자가 아닙니다.".format(number))

if (number % 5) == 0:
    print("{}은 5로 나누어 떨어지는 숫자입니다.".format(number))

else:
    print("{}는 5로 나누어 떨어지는 숫자가 아닙니다.".format(number))


#print(f"{number}는 2로 나누어 떨어지는 수가 아닙니다.") 와 같은 f사용법에 대해 익숙해지자.
#elif를 쓰면 2,3,4,5중 하나의 결과만 도출된다.


