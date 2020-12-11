# Introdução à Ciência da Computação com Python Parte 1 // Week 6
# 09/12/2020
# Author: Arthur "Setembru" Kuwahara

import math

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x = delta(a, b, c)
    prRoots(a, b, x)

def delta(a,b,c):
    return b**2 - 4*a*c

def prRoots(a,b,x):
    if x == 0:
        print("Apenas uma raiz:",-b/(2*a))
    elif x < 0:
        print("Sem raízes reais.")
    else:
        r1 = (-b - math.sqrt(x)/(2*a))
        r2 = (-b + math.sqrt(x)/(2*a))
        print("As raízes são:",r1 ,r2)
