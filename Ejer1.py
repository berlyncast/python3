#berlyn
#crear un programa que les permita seleccionar entre una de dos opciones 
#convertir dolares a quetzales
#convertir quetzales a dolares
print ("Bienvenido al conversor".center(50,"*"))

quetzal_dolar = 7.50
dolar_quetzal = 0.13
print ("escoja una opcion")

print ("1 dolares a quetzales")
print ("2 quetzales a dolares")

operacion = raw_input("seleccione la opcion:")
num = float(raw_input("escriba una cifra")

if operacion == "1"
    print("quetzales a dolares".center(50,"*"))
    cantidad = float(input("ingrese la cantidad en dolares:."))
    resultado = cantidad*quetzal_dolar
elif operacion == 2:
    print("dolares a quetzales".center(50,"*"))
    cantidad = float(input("ingrese la cantidad en quetzales:."))
    resultado = cantidad*dolar_quetzal
else:
    print("dato incorrecto")
    print("su cantidad es:.{}".format("dolar * quetzal = dolar / quetzal"))
