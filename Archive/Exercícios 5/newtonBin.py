def facx(x):
    if x <= 1:
        return 0
    elif x > 1:
        i = x
        while i != 1:
            i -= 1
            x = x * i
        return x

def newtonBin(n, k):
    if n < k:
        return 0
    else:
        return facx(n)/facx(k)*facx(n-k)

n = int(input("Insert n: "))
k = int(input("Insert k: "))
print(newtonBin(n, k))