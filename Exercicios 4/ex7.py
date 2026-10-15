numF = 1
numN = int(input("Digite número fatorial: "))

for i in range(1, numN + 1):
    numF = numF * i
print(f"O número fatorial é {numF}")