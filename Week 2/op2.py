segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // 86400
horas = (segundos - (dias * 86400)) //  3600
minutos = (segundos - (dias * 86400) - (horas * 3600)) // 60
segundos = (segundos - (dias * 86400) - (horas * 3600) - (minutos * 60))

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))