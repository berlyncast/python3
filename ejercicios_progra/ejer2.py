#calcula el precio de un boleto de viaje, tomando en cuenta el numero de kilometros
#que se van a recorrer, siendo el precio Bs./.10,50 por km
KILOMETRO = 10.50
costo = 0
km =int(input("ingrese kilometros a recorrer:"))
costo = km * KILOMETRO
print("el costa a pagar por los boletos es de:{}".format(costo))
