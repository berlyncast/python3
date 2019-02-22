#en un hospital existen 3 areas: Urgencias, Pedriatria y Traumatologia. El
#presupuesto anual del hospital se reparte de la siguiente manera:

#Area                   Presupuesto
#Ugencias                  37%
#Pedriatria                42%
#Traumatologia             21%

urgencias = 0
pedriatria = 0
traumatologia = 0
presupuesto = 0

presupuesto = float(input("ingrese presupuesto anual para el hospital"))
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print("el area de urgencais recibira la cantidad de dinero de:.",urgencias)
print("el area de pediatria recibira la cantidad de dinero de:.",pediatria)
print("el area de traumatologia recibira la cantidad de dinero de :.",traumatologia)
