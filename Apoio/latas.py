# Ex. 4

N = int(input("Qual é o número de paredes?"))
L = int(input("Qual é a largura das paredes?"))
H = int(input("Qual é a altura das paredes?"))

A = L*H*N
VLata = 20*(A/5)
VTempo = 30*(A/10)
Liq = VLata + VTempo
print("O orçamento deve ser:",Liq)