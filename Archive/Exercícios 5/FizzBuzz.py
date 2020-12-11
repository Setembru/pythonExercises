# Introdução à Ciência da Computação com Python Parte 1 // Week 5
# 09/12/2020
# Author: Arthur "Setembru" Kuwahara

def fizzbuzz(a):
    if a % 3 == 0 and a % 5 != 0:
        return 'Fizz'
    elif a % 5 == 0 and a % 3 != 0:
        return 'Buzz'
    elif a % 5 == 0 and a % 3 == 0:
        return 'FizzBuzz'
    else:
        return a