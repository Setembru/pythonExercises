n = int(input("Digite um número: "))
i = 2
if(n == 0 or n == 1):
	print("Não primo")
	i = n
elif(n == 2):
	print("Primo")
	i = n
while i < n:
	if(n % i == 0):
		print ("Não primo")
		break
	elif(i == (n - 1)):
		print("Primo")
		break
	i += 1