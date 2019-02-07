#solicitar al usuario que seleccione una opcion
#solicitar dos numeros y elevar el primer numero elevado al segundo numero
#solicitar tres numeros y elevar el primero al segundo y el resultado elevarlo al tercer numero
elevacion = 0
print("bienvenido al programa".center(18,"*"))
opcion=input("1. elevar el primer numero con el segundo 2. 3 numeros y elevar el primero con el segundo y el resultado elevarlo al tercero:.")
               
if opcion == "1":
    valor1 = input("ingrese el primer valor")
    valor2 = input("ingrese el segundo valor")
    elevacion = int(valor1) ** int(valor2)
    print("la elevacion es:. {}".format(elevacion))
elif opcion == "2":
    valor1 = int(input("ingrese primer valor"))
    valor2 = int(input("ingrese segundo valor"))
    valor3 = int(input("ingrese tercer valor"))
    elevacion = (valor1 ** valor2) ** valor3
    print("la elevacion es:. {}".format(elevacion))
else:
    ("opcion no valida")
