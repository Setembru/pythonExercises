import math

def main():
    x1 = float(input("Insira a abscissa (x) do primeiro ponto: "))
    y1 = float(input("Insira a ordenada (y) do primeiro ponto: "))
    x2 = float(input("Insira a abscissa (x) do segundo ponto: "))
    y2 = float(input("Insira a ordenada (x) do segundo ponto: "))
    
    # Calculando a distância
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance >= 10:
        print("longe")
    else:
        print("perto")
main()