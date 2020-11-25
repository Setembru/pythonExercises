import math

def main():

    print("A equação é do tipo: ax² + bx + c = 0")
    a = float(input("Insira o valor do coeficiente a: "))
    b = float(input("Insira o valor do coeficiente b: "))
    c = float(input("Insira o valor do coeficiente c: "))
    
    delta = (b**2 - 4*a*c)
    if delta < 0:
        print("Essa equação não possui raíz real.")
    elif delta == 0:
        root = -b/(2*a)
        print("Essa equação possui uma única equação, que é:",root)
    elif delta > 0:
        x1 = (-b - math.sqrt(delta))/2*a
        x2 = (-b + math.sqrt(delta))/2*a
        print("As raízes dessa equação são:",x1,x2)

#Escrevendo a equação
    print("A equação é do tipo: %ix² + %ix + %i = 0" %(a,b,c))

#--------------------------------
main()