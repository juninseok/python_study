#4.반복문 도전문제 - 염기 코돈의 개수를 세기

dna = input("염기 서열을 입력하세요: ")

output = {}

for i in range(0,len(dna),3):
    codon = dna[i:i+3]

    if len(codon) == 3:
        if codon in output:
            output[codon] += 1
        else:
            output[codon] = 1

print(output)


