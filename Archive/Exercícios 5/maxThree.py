# Introdução à Ciência da Computação com Python Parte 1 // Week 5
# 05/12/2020
# Author: Arthur "Setembru" Kuwahara

def maximo(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c