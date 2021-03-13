#Ejercicio 1
# continuar=input("Respuesta si/no:")
# cont=0
# cont2=0

# while(continuar=="si"):

#     genero=input("Respuesta mujer/hombre:")
        
#     if(genero=="mujer"):
#         cont+=1
#     else:
#         cont2+=1

#     continuar=input("Desea continuar si/no:")
   

# print ("El total de mujeres es ",cont)
# print ("El total de hombres es ",cont2)
# print ("El total de personas ",cont + cont2)

# Ejercicio 2

# solicitud=input("Desea presentarse a un cargo (si/no): ")
# contAnalista=0
# contDesarrollador=0
# contArquitecto=0

# salarioAnalista=870000
# salarioDesarrollador=2300000
# salarioArquitecto=790000

# while(solicitud=="si"):

#     cargo=input("Selecciona el cargo al que se presenta (analista/desarrollador/arquitecto software): ")

#     if(cargo=="analista"):
#         contAnalista+=1
#     elif(cargo=="desarrollador"):
#         contDesarrollador+=1
#     elif(cargo=="arquitecto software"):
#         contArquitecto+=1
#     else:
#         print("Revisar la información seleccionada")

#     solicitud=input("Desea presentarse a un cargo (si/no): ")

# costoAnalista=contAnalista*salarioAnalista
# costoDesarrollador=contDesarrollador*salarioDesarrollador
# costoArquitecto=contArquitecto*salarioArquitecto
# costoTotal=costoAnalista+costoDesarrollador+costoArquitecto

# print("Cantidad de analistas: ",contAnalista)
# print("Cantidad de desarrolladores: ",contDesarrollador)
# print("Cantidad de arquitectos software: ",contArquitecto)
# print("Costo total ",costoTotal)

# Ejercicio 3

# solicitud=input("Desea ingresar (si/no): ")

# contNinos=0
# contJovenes=0
# contAdultos=0

# while(solicitud=="si"):
#     edad=int(input("Cuál es su edad?"))

#     if(edad<=15):
#         contNinos+=1
#     elif(edad>=16) and (edad<18):
#         contJovenes+=1
#     else:
#         contAdultos+=1
#     solicitud=input("Desea ingresar (si/no): ")

# contTotalPersonas=contNinos+contJovenes+contAdultos

# print("El porcentaje de adultos es",round(contAdultos/contTotalPersonas,2))
# print("El porcentaje de niños es",round(contNinos/contTotalPersonas,2))

# Ejercicio 4

# centinela=input("Desea ingresar al lavadero (si/no): ")

# contSencillo=0
# contFull=0

# PrecioSencillo=12000
# PrecioFull=17000

# while(centinela=="si"):
#     servicio=input("Seleccione el servicio (sencillo,full): ")

#     if(servicio=="sencillo"):
#         contSencillo+=1
#     elif(servicio=="full"):
#         contFull+=1
#     else:
#         print("Por favor verifique la información ingresada")

# totalSencillo=PrecioSencillo*contSencillo
# totalFull=PrecioFull*contFull

# print("La cantidad de servicios sencillos es ",contSencillo)
# print("La cantidad de servicios full es",contFull)
# print("El total recolectado por sencillo es",totalSencillo)
# print("El total recolectado por fullo es",totalFull)


# Ejercicio 5

# num=1
# contador=0
# par=0

# while(contador<=20):
    
#     par=num%2

#     if(par==0):
#         print(num)

#     num+=1
#     contador=contador+par

#Ejercicio 6

# contDiez=1

# while(contDiez<=10):
#     print(contDiez)
#     contDiez+=1

#Ejericicio 7

# DiezNegativo=-1
# contadorNegativos=0
# parNegativo=0

# while(contadorNegativos<=10):

#     parNegativo=DiezNegativo%2

#     if(parNegativo==0):
#         print(DiezNegativo)

#     DiezNegativo-=1
#     contadorNegativos=contadorNegativos+parNegativo

# Ejercicio 8

# numTreinta=1
# contadorTreinta=0
# parTreinta=0
# sumaTreinta=0

# while(contadorTreinta<=30):
    
#     parTreinta=numTreinta%2

#     if(parTreinta==0):
#         sumaTreinta=sumaTreinta+numTreinta

#     numTreinta+=1
#     contadorTreinta=contadorTreinta+parTreinta

# print("La suma de los primeros 30 números pares es ",sumaTreinta)

# Ejercicio 9

numDiez=0
contadorDiez=0
imparDiez=0
sumaDiez=0

while(contadorDiez<10):
    
    imparDiez=numDiez%2

    if(imparDiez==1):
        sumaDiez=sumaDiez+numDiez

    numDiez+=1
    contadorDiez=contadorDiez+imparDiez

print("La suma de los primeros 10 números impares es ",sumaDiez)

# Ejercicio 9