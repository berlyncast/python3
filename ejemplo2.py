##berlyn
##calcular la edad actual de una persona,
##previamene ingresando
##el año actual y el año de nacimiento
print("bienvenido al programa".center(50,"*"))
FEC_ACT = 2019
fec_nac = int(input("ingresa tu año de nacimiento"))

edad = FEC_ACT - fec_nac

print("Tu edad es {}".format(edad))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
