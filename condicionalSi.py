#condicionales en python
""" numero1=5
numero2=10

if numero1>numero2:
    print("El mayor valor es ",numero1)
else:
    print("El mayor valor es",numero2) """

##################################################
""" iva=0.19
lavado=input("Seleccione el servicio (sencillo/full):")
if lavado == "sencillo":
    precio=12000*(1+iva)
else:
    precio=15000*(1+iva)

print("El precio del servicio es ",precio) """

####################################################
""" nota1=float(input("Ingrese nota 1:"))
nota2=float(input("Ingrese nota 2:"))
nota3=float(input("Ingrese nota 3:"))
nota4=float(input("Ingrese nota 4:"))
nota5=float(input("Ingrese nota 5:"))

notaProme=(0.1*nota1)+(0.2*nota2)+(0.35*nota3)+(0.15*nota4)+(0.2*nota5)

if notaProme>=3.5:
    print("La nota promedio es ",notaProme,".La asignatura esta aprobada")
else:
    print("La nota promedio es ",notaProme,".La asignatura no fue aprobada") """

#####################################################
tipoVehiculo=input("Ingrese el tipo de vehículo (taxi/particular/camion)")
tipoLavado=input("Ingrese el tipo de lavado (sencillo/full)")

if(tipoVehiculo=="taxi") and (tipoLavado=="sencillo"):
    print("El valor a pagar es ",12300)
elif (tipoVehiculo=="particular") and (tipoLavado=="sencillo"):
    print("El valor a pagar es",15000)
elif (tipoVehiculo=="camion") and (tipoLavado=="sencillo"):
    print("El valor a pagar es",23000)

elif (tipoVehiculo=="taxi") and (tipoLavado=="full"):
    print("El valor a pagar es",25000)
elif (tipoVehiculo=="particular") and (tipoLavado=="full"):
    print("El valor a pagar es",27000)
elif (tipoVehiculo=="camion") and (tipoLavado=="full"):
    print("El valor a pagar es",28000)

else:
    print("No se tiene información disponible")

