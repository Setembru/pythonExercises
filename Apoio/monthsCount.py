def main():
    print("-------------- SEJA BEM-VINDO --------------")
    sec1 = int(input("Digite o número de segundos que deseja dividir: "))
    
    months = sec1//(60*60*24*7*4)
    monRema = sec1%(60*60*24*7*4)

    weeks = monRema//(60*60*24*7)
    weeRema = monRema%(60*60*24*7)

    days = weeRema//(60*60*24)
    dRema = monRema%(60*60*24)

    hours = dRema//(60*60)
    hRema = dRema%(60*60)

    minu = hRema//60
    secFinal = minu%60

    print("O tempo é",months,"meses,",weeks,"semanas,",days,"dias,",hours,"horas,",minu,"minutos e",secFinal,"segundos.")
main()