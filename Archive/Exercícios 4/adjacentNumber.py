def main():
    n = (input("Insira o número n: "))
    length = len(n)
    n = int(n)

    if length < 2:
        print("não")
    else:
        i = length
        while i > 1:
            if n % 10 == (n//10) % 10:
                print("sim")
                break
            n = n // 10
            i -= 1
        if i == 1:
            print("não")

#-----------------
main()