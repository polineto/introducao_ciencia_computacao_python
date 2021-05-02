numero = input("Por favor, entre com o número de segundos que deseja converter: ")

dias = int(numero) // (60*60*24)
horas = (int(numero) % (60*60*24)) // (60*60)
minutos = ((int(numero) % (60*60*24)) % (60*60)) // 60
segundos = ((int(numero) % (60*60*24)) % (60*60)) % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")
