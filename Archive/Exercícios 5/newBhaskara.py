import math

def root(a,b,c):
    return (b**2 - 4*a*c)

def equation(a,b,root):
    if root < 0:
        return 'A equação é do tipo: ax² + bx + c = 0\nImaginary'
    elif root == 0:
        x = b/(2*a)
        return 'Essa equação possui uma única equação, que é:', x
    elif root > 0:
        x1 = (-b - math.sqrt(root))/2*a
        x2 = (-b + math.sqrt(root))/2*a
        return 'As raízes dessa equação são:', x1, x2

#--------------------------------
a = round(float(input("Insira o valor do coeficiente a: ")),1)
b = round(float(input("Insira o valor do coeficiente b: ")),1)
c = round(float(input("Insira o valor do coeficiente c: ")),1)

x = root(a,b,c)
print(equation(a,b,x))
print("%ix² + %ix + %i = 0" %(a,b,c))