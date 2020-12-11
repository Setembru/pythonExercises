# Introdução à Ciência da Computação com Python Parte 1 // Week 5
# 09/12/2020
# Author: Arthur "Setembru" Kuwahara

def maior_primo(n):
    i = n - 1
    # The logical repeat loop to see if n is divisible by its predecessors (prime) or not.
    while i > 2 and n % i != 0:
        i -= 1
    # I can't do this to 2, so i created this exception.
    if n == 2:
        return n
    # First test, to see if the first n is prime or not.
    elif n % i == 0:
        key = 'on'
        k = n
        while key == 'on':
            k -= 1
            i = k - 1
            # Line 7
            while i > 2 and k % i != 0:
                i -= 1
            if k % i != 0:
                key = 'off'
                return k
    else:
        return n