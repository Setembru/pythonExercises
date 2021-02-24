def juros(C, mth, itaxa, t):
    taxa = (100 + itaxa)/100

    Cap = C
    C = C*taxa
    i = 0
    while i < t - 1:
        C = (C+mth)*taxa
        i += 1
    print("\nBalança",C)
    print("Total investido:",mth*(t-1)+Cap)
    print("Rendimento:",C-(mth*(t-1)+Cap))
    return C

def entrada():
    tCapital = round(float(input("Qual o investimento inicial? ")),2)
    tMensal = round(float(input("Qual o valor mensal a ser investido? ")),2)
    tTaxa = round(float(input("Qual a taxa de juros? ")),4)
    tTempo = int(input("Quanto tempo? "))

    juros(tCapital, tMensal, tTaxa, tTempo)

entrada()