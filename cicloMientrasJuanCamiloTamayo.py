#------------------------------------------------------------------------------
#Ejercicio 1 (Total de personas (hombres y mujeres) que ingresan al metro)

continuar=input("Desea continuar con el ingreso (si/no):")
contMujer=0
contHombre=0

while(continuar=="si"):

    genero=input("Ingrese su genero (mujer/hombre):")
        
    if(genero=="mujer"):
        contMujer+=1
    else:
        contHombre+=1

    continuar=input("Desea continuar con el ingreso (si/no):")
   

print ("El total de mujeres es ",contMujer)
print ("El total de hombres es ",contHombre)
print ("El total de personas es ",contMujer + contHombre)

#------------------------------------------------------------------------------

#Ejercicio 2 (Clasificación de personas que se presentan a un cargo y sus costos asociados)

solicitud=input("Desea presentarse a uno de los cargos disponibles (si/no): ")
contAnalista=0
contDesarrollador=0
contArquitecto=0

salarioAnalista=870000
salarioDesarrollador=2300000
salarioArquitecto=790000

while(solicitud=="si"):

    cargo=input("Selecciona el cargo al que se presenta (analista/desarrollador/arquitecto software): ")

    if(cargo=="analista"):
        contAnalista+=1
    elif(cargo=="desarrollador"):
        contDesarrollador+=1
    elif(cargo=="arquitecto software"):
        contArquitecto+=1
    else:
        print("Revisar la información seleccionada")

    solicitud=input("Desea presentarse a uno de los cargos disponibles (si/no): ")

costoAnalista=contAnalista*salarioAnalista
costoDesarrollador=contDesarrollador*salarioDesarrollador
costoArquitecto=contArquitecto*salarioArquitecto
costoTotal=costoAnalista+costoDesarrollador+costoArquitecto

print("La cantidad de analistas es ",contAnalista)
print("La cantidad de desarrolladores es ",contDesarrollador)
print("La cantidad de arquitectos de software es ",contArquitecto)
print("El costo total corresponde a ",costoTotal)

#------------------------------------------------------------------------------

#Ejercicio 3 (Porcentaje de adultos y niños que ingresan a Comfama)

solicitud=input("Desea ingresar a Comfama (si/no): ")

contNinos=0
contJovenes=0
contAdultos=0
contTotalPersonas=0

while(solicitud=="si"):
    edad=int(input("Ingrese la edad: "))

    if(edad<=15):
        contNinos+=1
    elif(edad>=16) and (edad<18):
        contJovenes+=1
    else:
        contAdultos+=1
    
    solicitud=input("Desea ingresar a Comfama (si/no): ")

contTotalPersonas=contNinos+contJovenes+contAdultos

print("El porcentaje de adultos es ",round(contAdultos*100/contTotalPersonas,2)," %")
print("El porcentaje de jovenes es ",round(contJovenes*100/contTotalPersonas,2)," %")
print("El porcentaje de niños es ",round(contNinos*100/contTotalPersonas,2)," %")

#------------------------------------------------------------------------------

#Ejercicio 4 (Total de servicios realizados y total recaudado)

servicio=input("Desea ingresar al lavadero (si/no): ")

contSencillo=0
contFull=0

PrecioSencillo=12000
PrecioFull=17000

totalSencillo=0
totalFull=0

while(servicio=="si"):
    tipoServicio=input("Seleccione el servicio que desea (sencillo/full): ")

    if(tipoServicio=="sencillo"):
        contSencillo+=1
    elif(tipoServicio=="full"):
        contFull+=1
    else:
        print("Por favor verifique la información ingresada")
        
    servicio=input("Desea ingresar al lavadero (si/no): ")
    
totalSencillo=PrecioSencillo*contSencillo
totalFull=PrecioFull*contFull

print("La cantidad de servicios sencillos es ",contSencillo)
print("La cantidad de servicios full es",contFull)
print("El total recolectado por sencillo es ",totalSencillo)
print("El total recolectado por full es ",totalFull)

#------------------------------------------------------------------------------
#Ejercicio 5 (Imprimir los 20 primeros números pares)

num=1
contador=0
par=0

while(contador<=20):
    
    par=num%2

    if(par==0):
        print(num)

    num+=1
    contador=contador+par
    
#------------------------------------------------------------------------------

#Ejercicio 6 (Imprimir los primeros 10 números positivos)

contDiez=1

while(contDiez<=10):
    print(contDiez)
    contDiez+=1
    
#------------------------------------------------------------------------------

#Ejericicio 7 (Imprimir los primeros 10 números negativos impares)

DiezNegativo=-1
contadorNegativos=0
imparNegativo=0

while(contadorNegativos<10):

    imparNegativo=DiezNegativo%2

    if(imparNegativo==1):
        print(DiezNegativo)

    DiezNegativo-=1
    contadorNegativos=contadorNegativos+imparNegativo
    
#------------------------------------------------------------------------------

#Ejercicio 8 (Suma de los primeros treinta números pares)

numTreinta=1
contadorTreinta=0
parTreinta=0
sumaTreinta=0

while(contadorTreinta<=30):
    
    parTreinta=numTreinta%2

    if(parTreinta==0):
        sumaTreinta=sumaTreinta+numTreinta

    numTreinta+=1
    contadorTreinta=contadorTreinta+parTreinta

print("La suma de los primeros 30 números pares es ",sumaTreinta)

#------------------------------------------------------------------------------

# Ejercicio 9 (Suma de los primeros diez números impares)

numDiez=1
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

#------------------------------------------------------------------------------

# Ejercicio 10 (Imprimir la serie Fibonacci)

limite=int(input("Ingrese el número que representa el límite de la serie: "))

serie=0
auxiliar=1

while(serie<limite):
    print(serie,end='\n')
    
    serie,auxiliar=auxiliar, serie+auxiliar
    
#------------------------------------------------------------------------------
# Ejercicicio 11 (Venta de boletas en el estadio Atanasio Girardot)

cantidadDisponible=0
cantidadVendida=0
contNorte=0
contSur=0
contOriente=0
contOccidente=0
contMujer=0
contHombre=0

ingreso=input("Desea ingresar al estadio (si/no):")

while(ingreso=="si"):
    tribuna=input("Seleccione su tribuna (Norte/Sur/Oriente/Occidente):")
    genero=input("Indique su genero (Mujer/Hombre): ")
    
    if(tribuna=="Norte"):
        contNorte+=1
    elif(tribuna=="Sur"):
        contSur+=1
    elif(tribuna=="Oriente"):
        contOriente+=1
    elif(tribuna=="Occidente"):
        contOccidente+=1
    else:
        print("Verifique la selección de la tribuna")
        
    if(genero=="Mujer"):
        contMujer+=1
    elif(genero=="Hombre"):
        contHombre+=1
    else:
        print("Verifique el género ingresado")
        
    ingreso=input("Desea ingresar al estadio (si/no):")

cantidadVendida=contNorte+contSur+contOriente+contOccidente
cantidadDisponible=45000-cantidadVendida

print("La cantidad de boletas vendidas es ",cantidadVendida)
print("La cantidad de boletas disponibles es ",cantidadDisponible)
print("Personas que ingresaron a norte ",contNorte)
print("Personas que ingresaron a sur ",contSur) 
print("Personas que ingresaron a oriente ",contOriente)
print("Personas que ingresaron a occidente ",contOccidente)
print("Mujeres que ingresaron ",contMujer)
print("Hombres que ingresaron ",contHombre)   

#------------------------------------------------------------------------------
#Ejercicio 12 (Escuela de natación con clasificación por niveles)

contBasico=0
contExperimentado=0
contProfesional=0
contTotal=0

precioBasico=120000
precioExperimentado=250000
precioProfesional=280000

limiteCupos=int(input("Ingrese cantidad de cupos para este mes: "))

while(contTotal<limiteCupos):
    edad=int(input("Ingrese su edad: "))
    
    if(edad>=4)and(edad<=8):
        contBasico+=1
    elif(edad>=9)and(edad<=12):
        contExperimentado+=1
    elif(edad>12):
        contProfesional+=1
    else:
        print("Tu edad es inferior a 4 años y no puedes participar")
        
    contTotal+=1
        
ingresoBasico=precioBasico*contBasico
ingresoExperimentado=precioExperimentado*contExperimentado
ingresoProfesional=precioProfesional*contProfesional
ingresoTotal=ingresoBasico+ingresoExperimentado+ingresoProfesional

print("Cantidad de matriculas básico ",contBasico," /Ingresos ",ingresoBasico)
print("Cantidad de matriculas experimentado ",contExperimentado," /Ingresos ",ingresoExperimentado)
print("Cantidad de matriculas profesional ",contProfesional, " /Ingresos ",ingresoProfesional)
print("Total de ingresos ",ingresoTotal)


        
    
        
    
    
    

