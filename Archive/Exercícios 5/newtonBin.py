# Introdução à Ciência da Computação com Python Parte 1 // Week 5
# 05/12/2020
# Author: Arthur "Setembru" Kuwahara

def facx(x):
    i = x
    if i > 0:
        while i > 1:
            i -= 1
            x = i * x
        return x
    elif x == 0:
        return 1
    else:
        return 'Undefined'

def binNumber(n, k):
    if n >= k:
        return facx(n)/(facx(k)*facx(n-k))
    else:
        return 0