def main():
    n = input("Insira um número n >= 0: ")

    l = len(n) # len() só lê strings

    n = int(n)

    i = 0 # Iteração
    f = 0 # Auxiliar para a soma
    
    while i < l:
        d = n % 10 # O último algarismo do número digitado
        n = n // 10
        f = f + d
        i += 1
    print(f)
main() 