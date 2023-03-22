#3.조건문 도전문제 - 간단한 대화 프로그램

import datetime

now = datetime.datetime.now()

string = input("입력:")


if "안녕" in string :
    print("안녕하세요.")

elif "지금" in string:
    print("지금은 {}시 입니다.".format(now.hour))

else:
    print(string)

#in 키워드를 이용하여 입력한 문자열 안에 설정한 문자열이 있으면 원하는 출력을 내보낸다.
