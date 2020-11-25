num = int(input("Digite um número inteiro: "))

print(num)
ans1 = num%100
aux = num%10
fans = ans1 - aux
finalAns = fans//10

print("O dígito das dezenas é",finalAns)