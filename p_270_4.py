#4.반복문 도전문제 - 2차원 리스트 평탄화

list_a = [1,2,[3,4],5,[6,7],[8,9]]
output = []

for i in list_a:
    if type(i) == list:
        for j in i:
            output.append(j)
    else:
        output.append(i)

print(output)
