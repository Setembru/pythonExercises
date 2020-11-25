sec = int(input("Por favor, entre com o número de segundos que deseja converter: "))

days = sec//(60*60*24)
remainingSeg1 = sec%(60*60*24)

hours = remainingSeg1//(60*60)
remainingSeg2 = remainingSeg1%(60*60)

mins = remainingSeg2//60
remainingSeg3 = remainingSeg2%60

secc = remainingSeg3

print(days,"dias,",hours,"horas,",mins,"minutos e",secc,"segundos")