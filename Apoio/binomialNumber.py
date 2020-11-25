import math

def main():
    n = int(input("Insert the first integer (n): "))
    k = int(input("Insert the second integer (k): "))
    if n < k:
        print("O resultado é: 0")
    x = (math.factorial(n)) / (math.factorial(k) * math.factorial (n - k))

    print("A equação é do tipo: %i!/(%i!*(%i-%i)!)"%(n,k,n,k))
    print("A resolução é:",x)
    print(math.comb(n,k))
main()