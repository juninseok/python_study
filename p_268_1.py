#4.반복문 도전문제 - 리스트에서 몇가지 종류의 숫자가 사용되었는지 구하기

list_a = [1,2,3,4,1,2,3,1,4,1,2,3]
dictionary = {}
count = 0       #개수를 세기 위해서 변수 설정을 하는 방법 말고 len(dictionary)를 이용하는 방법도 있다.

for item in list_a:
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1
        count += 1

print("{}에서 사용한 숫자의 개수는{}{}개 입니다".format(list_a,"\n",count))
print(dictionary)