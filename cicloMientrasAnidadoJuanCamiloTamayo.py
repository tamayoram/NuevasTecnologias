# =============================================================================
# Ejercicio 1 (Ejercicio de clase para calcular promedio y cantidad de personas
# que ganan y pierden la materia).
# =============================================================================

contador1=0
contadorGanador=0
contadorPerdedor=0

while(contador1<5):
    nombre=input("Ingrese su nombre: ")
    
    promedio=0
    suma=0
    contador2=0

    while(contador2<5):
        notaMateria=float(input("Ingrese la nota: "))
        contador2+=1
        suma=suma+notaMateria

    promedio=round(suma/5,2)
    print("El promedio de la nota es ",promedio)
    
    if(promedio>=3):
        print("Gana la materia")
        contadorGanador+=1
    else:
        print("Pierde la materia")
        contadorPerdedor+=1

    contador1+=1

print("El número total de ganadores es ",contadorGanador)
print("El número total de perdedores es",contadorPerdedor)


# =============================================================================
# Ejercicio 2 (Ejercicio de clase donde se pide la información de 3 jugadores
# de 3 equipos)
# =============================================================================

maximoEquipo=3
maximoJugadores=3
contadorEquipo=1

while(contadorEquipo<=maximoEquipo):
    equipo=input("Ingrese el nombre del equipo: ")

    contadorJugadores=1
    
    while(contadorJugadores<=maximoJugadores):
        
        documento=input("Ingrese su documento: ")
        nombre=input("Ingrese su nombre: ")
        posicion=input("Ingrese su posición: ")
        
        print("\n")
        print("El equipo es: ", equipo)
        print("Jugador número: ", contadorJugadores)
        print("Documento: ",documento)
        print("Nombre: ",nombre)
        print("Posición: ",posicion,"\n")

        contadorJugadores+=1

    contadorEquipo+=1


# =============================================================================
# Ejercicio 3 (Ejercicio para el cálculo del índice de masa corporal y 
# evaluación si la persona tiene sobrepeso)
# =============================================================================

cantidadPersonas=int(input("Ingrese la cantidad de personas encuestadas: "))
contadorPersonas=1

while(contadorPersonas<=cantidadPersonas):
    edad=input("Ingrese su edad: ")
    genero=input("Ingrese su género (hombre/mujer): ")
    peso=float(input("Ingrese su peso en kilogramos: "))
    estatura=float(input("Ingrese su estatura en metros: "))

    imc=round(peso/estatura**2,2)

    if(imc<25):
        print("\n")
        print("Edad: ",edad)
        print("Género: ",genero)
        print("Su índice de masa corporal es ",imc," no tiene sobrepeso","\n")
    else:
        print("\n")
        print("Edad: ",edad)
        print("Género: ",genero)
        print("Su índice de masa corporal es ",imc,"tiene sobrepeso","\n")

    contadorPersonas+=1

# =============================================================================
# Ejericio 4 (Ejercicio donde se calcula la cantidad de colegios participantes
# en las pruebas intercolegiales de matemáticas de la Alcaldía de Medellín)
# =============================================================================

colegios=input("Desea inscribir su colegio (si/no): ")

contadorColegios=0
contadorNino=0
contadorNina=0

while(colegios=="si"):
    contadorColegios+=1

    contadorParticipantes=1
    while(contadorParticipantes<=2):
        grado=input("Por favor ingresa el grado que cursas: ")
        edad=input ("Por favor ingresa la edad: ")
        genero=input("Por favor ingresa el género (niño/niña): ")

        if(genero=="niño"):
            contadorNino+=1
        elif(genero=="niña"):
            contadorNina+=1
        else:
            print("Verifica la información ingresada")

        contadorParticipantes+=1
    
    colegios=input("Desea inscribir su colegio (si/no): ")

print("La cantidad de colegios participantes es ",contadorColegios)
print("La cantidad de niños en la competencia es ",contadorNino)
print("La cantidad de niñas en la competencia es ",contadorNina)

# =============================================================================
# Ejercicio 5 (Ejercicio que calcula el valor del pasaje, la cantidad de personas
# y el porcentaje del total de viajeros para la agencia Aviatur)
# =============================================================================

solicitudViaje=input("Desea realizar un viaje con nuestra agencia (si/no): ")

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
        contadorAndres=contadorAndres+cantidadPersonas

    else:
        print("Verifique el destino seleccionado")

    print ("Su viaje a ", destino, " tiene un valor de ", round(valorTotal,0))

    solicitudViaje=input("Desea realizar un viaje con nuestra agencia (si/no): ")

contadorTotalPersonas=contadorCapurgana+contadorNuqui+contadorMargarita+contadorGalapagos+contadorMukura+contadorAndres

print("El total de personas que viajan a capurgana es ",contadorCapurgana, "representa un ",round(contadorCapurgana*100/contadorTotalPersonas,2), "% del total")

print("El total de personas que viajan a nuqui es ",contadorNuqui, "representa un ",round(contadorNuqui*100/contadorTotalPersonas,2), "% del total")

print("El total de personas que viajan a margarita es ",contadorMargarita, "representa un ",round(contadorMargarita*100/contadorTotalPersonas,2), "% del total")

print("El total de personas que viajan a galapagos es ",contadorGalapagos, "representa un ",round(contadorGalapagos*100/contadorTotalPersonas,2), "% del total")

print("El total de personas que viajan a mukura es ",contadorMukura, "representa un ",round(contadorMukura*100/contadorTotalPersonas,2), "% del total")

print("El total de personas que viajan a San Andres es ",contadorAndres, "representa un ",round(contadorAndres*100/contadorTotalPersonas,2), "% del total")

# =============================================================================
# #Ejercicio 6 (Ejercicio que calcula )
# =============================================================================

cupoMaximo=20
contadorVuelosDisponibles=0
precioVuelo=80000
contadorVuelosAceptados=0
contadorMujer=0
contadorHombre=0

while(contadorVuelosDisponibles<cupoMaximo):
    deseoVolar=input("Desea realizar el vuelo (si/no): ")
    
    if (deseoVolar=="si"):
        edad=int(input("Ingrese su edad: "))
        
        if(edad>=18):
            firma=input("Acepta los términos establecidos para el vuelo (si/no): ")
            
            if (firma=="si"):
                
                contadorVuelosAceptados+=1
                eps=input("Ingrese su eps: ")
                genero=input("Ingrese su género (hombre/mujer): ")
                if(genero=="mujer"):
                    contadorMujer+=1
                elif (genero=="hombre"):
                    contadorHombre+=1
                else:
                    print("Por favor verifique el género ingresado")
                
            else:
                print("Sin la firma no es posible realizar el vuelo")
                       
              
        else:
            print("No se aceptan menores de edad")
            
    else:
        print("Te esperamos en una próxima ocasión")
        
        
    contadorVuelosDisponibles+=1
    
if(contadorVuelosAceptados==0):
    
    print("\n")
    
    print("La cantidad de vuelos aceptados (firma términos y condiciones) por mayores de edad es de: ",contadorVuelosAceptados) 
    print("El total recaudado en el día es: $ ",contadorVuelosAceptados*precioVuelo)
    
else:

    print("\n")
    
    print("La cantidad de vuelos aceptados (firma términos y condiciones) por mayores de edad es de: ",contadorVuelosAceptados)    
    
    print("La cantidad de mujeres que realizan el vuelo es de ",contadorMujer, "que representa un ",round(contadorMujer*100/contadorVuelosAceptados,2),"% del total de vuelos aceptados")
    
    print("La cantidad de hombres que realizan el vuelo es de ",contadorHombre, "que representa un ",round(contadorHombre*100/contadorVuelosAceptados,2),"% del total de vuelos aceptados")
    
    print("El total recaudado en el día es: $ ",contadorVuelosAceptados*precioVuelo)
    
            










