def main():
    n = int(input("Digite o número n: "))
    i = (n - 1)

    while i > 2 and n % i != 0:
        i -= 1

    if n == 1:
        print("não primo")
    elif n == 0:
        print("não primo")
    elif n % i == 0 and i > 1:
        print("não primo")
    else:
        print("primo")
main()