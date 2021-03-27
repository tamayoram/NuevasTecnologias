# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:23:50 2021

@author: admin
"""

# Primer ejercicio: =============================================================================
maximoEstudiantes=25
maximoNotas=5

sumaTotalMatematicas=0
sumaTotalLenguaje=0
 
contadorEstudiantes=1
 
while(contadorEstudiantes<=maximoEstudiantes):
         
    sumaMatematica=0
    contadorNotasMatematicas=0
     
    while(contadorNotasMatematicas<maximoNotas):
         
         notaMatematica=float(input("Ingrese la nota para matemáticas: "))
         
         sumaMatematica=sumaMatematica+notaMatematica
         
         contadorNotasMatematicas+=1
         
    promedioEstudianteMatematicas= round(sumaMatematica/contadorNotasMatematicas,2)
         
    print("\n")
    print("El promedio del estudiante", contadorEstudiantes, " para matemáticas es ", promedioEstudianteMatematicas)
 
    sumaTotalMatematicas=sumaTotalMatematicas+promedioEstudianteMatematicas
    
    
    sumaLenguaje=0
    contadorNotasLenguaje=0
    
    while (contadorNotasLenguaje<maximoNotas):
        notaLenguaje=float(input("Ingrese la nota para lenguaje: "))
        
        sumaLenguaje=sumaLenguaje+notaLenguaje
        
        contadorNotasLenguaje+=1
        
    promedioEstudianteLenguaje=round(sumaLenguaje/contadorNotasLenguaje,2)
    
    print("\n")
    print("El promedio del estudiante", contadorEstudiantes, " para lenguaje es ", promedioEstudianteLenguaje)
     
    sumaTotalLenguaje=sumaTotalLenguaje +promedioEstudianteLenguaje 
    
    contadorEstudiantes+=1
    
print("\n")
print("El promedio general para matemáticas es ",round(sumaTotalMatematicas/maximoEstudiantes,2))
print("El promedio general para lenguaje es ",round(sumaTotalLenguaje/maximoEstudiantes,2))     
print("El promedio general de ambas materias es ",round(((sumaTotalMatematicas+sumaTotalLenguaje)/maximoEstudiantes)/2,2))      
# =============================================================================

#Segundo ejercicio:

valorVehiculo=float(input("Por favor ingrese el valor del vehículo: "))
tiempo=float(input("Por favor ingrese en años el tiempo de financiación: "))

valorFinanciacion=valorVehiculo*0.7
tasaAnual=0.125
tasaMensual=tasaAnual/12
tiempoMes=tiempo*12


if (tiempo<3):
    print("El período es inferior a lo estipulado por política")
elif (tiempo>5):
    print("El período es superior a lo estipulado por política")
else:
    
    cuota=round(((valorFinanciacion*tasaMensual)/(1-(1+tasaMensual)**(-tiempoMes))),0)
   
    print("\n")
    print("El valor de su cuota mensual es: ",cuota)
    print ("El valor final pagado es de : ",cuota*tiempoMes)
    print("El valor final pagado corresponde a ",valorFinanciacion," de capital solicitado (70% valor vehículo) y ",(cuota*tiempoMes)-valorFinanciacion, " por intereses")
    
    


