# Ejercicio 1

""" prestamo=float(input("Por favor ingrese el valor del préstamo: "))
tasaAnual=0.136
nPer=5
cuota=round(((prestamo*tasaAnual)/(1-(1+tasaAnual)**(-nPer))),2)
print("La cuota de su préstamo es: ",cuota) """

# Ejercicio 2

""" nombre=input("Por favor ingrese su nombre: ")
edad=input("Por favor ingrese su edad: ")
telefono=input("Por favor ingrese su teléfono: ")

print("El nombre ingresado es ",nombre)
print("La edad ingresada es ",edad)
print("El teléfono ingresado es ",telefono) """

# Ejercicio 3
prestamoSemestre=float(input("Por favor ingrese el valor del préstamo: "))
nPerSemestre=12
tasaMensual=0.018
totalInteresDosMeses=(prestamoSemestre*(1+tasaMensual)**2)-prestamoSemestre
cuotaMensual=round(((prestamoSemestre*tasaMensual)/(1-(1+tasaMensual)**(-nPerSemestre))),0)
pagoNueveMeses=round(cuotaMensual*9,0) 
totalInteres=round((cuotaMensual*12)-prestamoSemestre,0)
print("El total de intereses los dos primeros meses es de ",totalInteresDosMeses)
print("El valor de la cuota mensual es ",cuotaMensual)
print("En 9 meses se ha pagado ",pagoNueveMeses)
print("Por concepto de interes se ha pagado ",totalInteres)




