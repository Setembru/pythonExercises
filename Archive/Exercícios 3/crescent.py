def main():
    a = int(input("Escreva o primeiro número: "))
    b = int(input("Escreva o segundo número: "))
    c = int(input("Escreva o terceiro número: "))

    if a < b < c:
        print("crescente")
    else:
        print("não está em ordem crescente")
main()