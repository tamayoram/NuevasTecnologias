# Ejemplo 1

# contador1=0
# contadorGanador=0
# contadorPerdedor=0

# while(contador1<5):
#     nombre=input("Ingrese su nombre")
#     print(contador1)

#     promedio=0
#     suma=0
#     contador2=0

#     while(contador2<5):
#         notaMateria=float(input("Ingrese la nota: "))
#         print(contador2)
#         contador2+=1
#         suma=suma+notaMateria

#     promedio=suma/5
#     print("El promedio de la nota es ",promedio)
    
#     if(promedio>3):
#         print("Gana la materia")
#         contadorGanador+=1
#         else:
#             print("Pierde la materia")
#             contadorPerdedor+=1

#     contador1+=1

# print("El número total de ganadores es ",contadorGanador)
# print("El número total de perdedores es",contadorPerdedor)


# Ejemplo 2

# maximoEquipo=2
# maximoJugadores=3
# contadorEquipo=1

# while(contadorEquipo<=maximoEquipo):
#     equipo=input("Ingrese el nombre del equipo: ")

#     contadorJugadores=1
#     while(contadorJugadores<=maximoJugadores):
        
#         documento=input("Ingrese su documento: ")
#         nombre=input("Ingrese su nombre: ")
#         posicion=input("Ingrese su posición: ")
        

#         print("El equipo es", equipo,"\n")
#         print("Jugador número", contadorJugadores)
#         print("Documento: ",documento)
#         print("Nombre: ",nombre)
#         print("Posición: ",posicion,"\n")

#         contadorJugadores+=1

#     contadorEquipo+=1


# Ejemplo 3 Cálculo del índice de masa corporal y evaluación si la persona tiene sobrepeso.

# cantidadPersonas=int(input("Ingrese la cantidad de personas encuestadas: "))
# contadorPersonas=1

# while(contadorPersonas<=cantidadPersonas):
#     edad=input("Ingrese la edad: ")
#     genero=input("Ingrese género (hombre/mujer): ")
#     peso=float(input("Ingrese el peso en kilogramos: "))
#     estatura=float(input("Ingrese la estatura en metros: "))

#     imc=round(peso/estatura**2,2)

#     if(imc<25):
#         print("\n")
#         print("Edad: ",edad)
#         print("Género: ",genero)
#         print("Su índice de masa corporal es ",imc," no tiene sobrepeso","\n")
#     else:
#         print("\n")
#         print("Edad: ",edad)
#         print("Género: ",genero)
#         print("Su índice de masa corporal es ",imc,"tiene sobrepeso","\n")

#     contadorPersonas+=1

# Ejemplo 4 (Pruebas intercolegiales de matemáticas de la Alcaldía de Medellín)

# colegios=input("Desea inscribir su colegio (si/no): ")

# contadorColegios=0
# contadorNino=0
# contadorNina=0

# while(colegios=="si"):
#     contadorColegios+=1

#     contadorParticipantes=1
#     while(contadorParticipantes<=2):
#         grado=input("Por favor ingresa el grado en curso: ")
#         edad=input ("Por favor ingresa la edad: ")
#         genero=input("Por favor ingresa el género (niño/niña): ")

#         if(genero=="niño"):
#             contadorNino+=1
#         elif(genero=="niña"):
#             contadorNina+=1
#         else:
#             print("Verifica la información ingresada")

#         contadorParticipantes+=1
    
#     colegios=input("Desea inscribir su colegio (si/no): ")

# print("La cantidad de colegios participantes es ",contadorColegios)
# print("La cantidad de niños en la competencia es ",contadorNino)
# print("La cantidad de niñas en la competencia es ",contadorNina)

# Ejemplo 5 (Ejercicio correspondiente a la agencia de viajes aviatur)

solicitudViaje=input("Desea realizar un viaje (si/no): ")

valorTotal=0
contadorTotalPersonas=0
contadorCapurgana=0
contadorNuqui=0
contadorMargarita=0
contadorGalapagos=0
contadorMukura=0
contadorAndres=0

while(solicitudViaje=="si"):
    destino=input("Ingrese el destino deseado (capurgana/nuqui/margarita/galapagos/mukura/san andres): ")
    cantidadPersonas=int(input("Ingrese la cantidad de personas que viajan: "))

    if(destino=="capurgana"):
        valorTotal=1500000*(1.15)*(1.2)*cantidadPersonas
        contadorCapurgana=contadorCapurgana+cantidadPersonas
    
    elif(destino=="nuqui"):
        valorTotal=1200000*(1.09)*(1.19)*cantidadPersonas
        contadorNuqui=contadorNuqui+cantidadPersonas

    elif(destino=="margarita"):
        valorTotal=200*(1.16)*(1.11)*cantidadPersonas
        contadorMargarita=contadorMargarita+cantidadPersonas
        valorPesos=input("Desea conocer el valor en pesos (si/no): ")
        if (valorPesos=="si"):
            valorTotal=valorTotal*3600
        else:
            valorTotal=valorTotal

    elif(destino=="galapagos"):
        valorTotal=400*(1.08)*(1.09)*cantidadPersonas
        contadorGalapagos=contadorGalapagos+cantidadPersonas
        valorPesos=input("Desea conocer el valor en pesos (si/no): ")
        if (valorPesos=="si"):
            valorTotal=valorTotal*3600
        else:
            valorTotal=valorTotal

    elif(destino=="mukura"):
        valorTotal=1200000*(1.09)*(1.11)*cantidadPersonas
        contadorMukura=contadorMukura+cantidadPersonas

    elif(destino=="san andres"):
        valorTotal=1500000*(1.12)*(1.13)*cantidadPersonas
        contadorMukura=contadorMukura+cantidadPersonas

    else:
        print("Verifique el destino seleccionado")

    print ("Su viaje a ", destino, " tiene un valor de ", round(valorTotal,0))

    solicitudViaje=input("Desea realizar un viaje (si/no): ")

contadorTotalPersonas=contadorCapurgana+contadorNuqui+contadorMargarita+contadorGalapagos+contadorMukura+contadorAndres

print("El total de personas a capurgana es ",contadorCapurgana, "representa un ",contadorCapurgana*100/contadorTotalPersonas, "%")

print("El total de personas a nuqui es ",contadorNuqui, "representa un ",contadorNuqui*100/contadorTotalPersonas, "%")

print("El total de personas a margarita es ",contadorMargarita, "representa un ",contadorMargarita*100/contadorTotalPersonas, "%")

print("El total de personas a galapagos es ",contadorGalapagos, "representa un ",contadorGalapagos*100/contadorTotalPersonas, "%")

print("El total de personas a mukura es ",contadorMukura, "representa un ",contadorMukura*100/contadorTotalPersonas, "%")

print("El total de personas a San Andres es ",contadorAndres, "representa un ",contadorAndres*100/contadorTotalPersonas, "%")

#Ejemplo 6



    
            










