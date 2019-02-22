#escriba un programa donde se ingrese el tiempo necesario para un cierto proceso en horas, minutos y segundos.
#Se calcule el costo total del proceso sabiendo que el costo  por segundo es Bs0,25

horas = 0 
minutos = 0 
segundos = 0
total = 0

horas = int(input("ingrese horas:."))
minutos = int(input("ingrese minutos:."))
segundos = int(input("ingrese segundo:."))

total = (((horas * 3600) + (minutos * 60) + segundos) * 0.25)
print("costo total del proceso Bs.", total)
