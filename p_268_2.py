#4.반복문 도전문제 - 염기서열의 갸수 구하기

dna = input("염기 서열을 입력하세요: ")

dic = {"c": 0,
       "a": 0,
       "t": 0,
       "g": 0
}

for i in dna:
    dic[i] += 1

for j in dic:
    print("{}의 개수 : {}".format(j,dic[j]))

