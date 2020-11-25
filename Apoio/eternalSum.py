def main():
    num = int(input("Digite um número para a soma: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite o próximo número: "))
    
    print("A soma é",soma)
main()