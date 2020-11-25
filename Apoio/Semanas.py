def main():
    seg = input("Insira um número de segundos: ")
    segInt = int(seg)

    weeks = segInt//(60*60*24*7)
    remainingSeg1 = segInt%(60*60*24*7)

    days = remainingSeg1//(60*60*24)
    remainingSeg2 = remainingSeg1%(60*60*24)

    hours = remainingSeg2//(60*60)
    remainingSeg3 = remainingSeg2%(60*60)

    mins = remainingSeg3//60
    remainingSeg4 = remainingSeg3%60

    sec = remainingSeg4

    print("O tempo é:",weeks,"semanas,",days,"dias,",hours,"horas,",mins,"minutos e",sec,"segundos")
#------------------------------
main()