# Solicitar al usuario la cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))

# Calcular las horas, minutos y segundos
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

# Verificar si la cantidad de horas es menor o igual a 24
if horas <= 24:
    print(f"El tiempo transcurrido fue de {horas} horas, {minutos} minutos y {segundos} segundos.")
else:
    print("Excedido")

# Proceso inverso
# Solicitar al usuario las horas, minutos y segundos
horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

# Calcular la cantidad total de segundos
total_segundos = horas * 3600 + minutos * 60 + segundos
print(f"La cantidad total de segundos es {total_segundos}.")
