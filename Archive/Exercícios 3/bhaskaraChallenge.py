import math

def main():

    a = float(input("Insira o valor do coeficiente a: "))
    b = float(input("Insira o valor do coeficiente b: "))
    c = float(input("Insira o valor do coeficiente c: "))
    
    delta = (b**2 - 4*a*c)
    if delta < 0:
        print("esta equação não possui raízes reais")
    if delta == 0:
        root = -b/(2*a)
        print("a raiz desta equação é",root)
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("as raízes da equação são",x1,"e",x2)
main()