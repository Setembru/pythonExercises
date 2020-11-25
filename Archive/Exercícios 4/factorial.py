import math
def main():
    n = int(input("Digite o valor de n: "))
    i = n
    if n == 0:
        print(1)
    else:
        while i > 2:
            i -= 1
            n = n*i
        print(n)
main()