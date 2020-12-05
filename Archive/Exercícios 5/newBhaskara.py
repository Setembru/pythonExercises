# Introdução à Ciência da Computação com Python Parte 1 // Week 5
# 05/12/2020
# Author: Arthur "Setembru" Kuwahara

def root(a,b,c):
    return (b**2 - 4*a*c)

def equation(a,b,root):
    if root < 0:
        return 'Raízes Imaginárias'
    elif root == 0:
        x = b/(2*a)
        return x
    elif root > 0:
        x1 = (-b - math.sqrt(root))/(2*a)
        x2 = (-b + math.sqrt(root))/(2*a)
        return x1, x2

#--------------------------------
a = int(input("Coeficient a: "))
b = int(input("Coeficient b: "))
c = int(input("Coeficient c: "))

x = root(a,b,c)
print(equation(a,b,x))
print("{:d}x² + {:d}x + {:d} = 0".format(a,b,c))