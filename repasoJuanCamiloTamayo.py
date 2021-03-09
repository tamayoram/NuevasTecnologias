# Ejercicio 1

# Definición de las variables que se va a utilizar en el algoritmo
prestamo=float(input("Por favor ingrese el valor del préstamo: "))
tasaAnual=0.136
nPer=5

# Cálculo de la cuota a partir de la formula financiera utilizada para determinar anualidades
cuota=round(((prestamo*tasaAnual)/(1-(1+tasaAnual)**(-nPer))),0)
print("El valor de su cuota corresponde a : ",cuota)


# Ejercicio 2

# Captura de la información requerida
nombre=input("Por favor ingrese su nombre: ")
edad=input("Por favor ingrese su edad: ")
telefono=input("Por favor ingrese su teléfono: ")

# Comando para presentar la información en pantalla
print("El nombre ingresado es ",nombre)
print("La edad ingresada es ",edad)
print("El teléfono ingresado es ",telefono)

#Ejercicio 3

#Captura de la información requerida
prestamoSemestre=float(input("Por favor ingrese el valor del préstamo: "))
nPerSemestre=12
tasaMensual=0.018

# Intereses correspondiente a los dos meses
totalInteresDosMeses=round((prestamoSemestre*(1+tasaMensual)**2)-prestamoSemestre,0)

#Cuota mensual que debe pagar
cuotaMensual=round(((prestamoSemestre*tasaMensual)/(1-(1+tasaMensual)**(-nPerSemestre))),0)

# Valor cancelado luego de 9 meses
pagoNueveMeses=round(cuotaMensual*9,0)

# Valor pagado por intereses

totalInteres=round((cuotaMensual*12)-prestamoSemestre,0)

#Comando para presentar la información en pantalla
print("El total de intereses para los dos primeros meses corresponde a ",totalInteresDosMeses)
print("El valor de la cuota mensual es ",cuotaMensual)
print("En 9 meses se ha pagado ",pagoNueveMeses)
print("Por concepto de interes se paga un total de ",totalInteres)




