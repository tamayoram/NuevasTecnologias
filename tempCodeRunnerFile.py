DiezNegativo=-1
contadorNegativos=0
parNegativo=0

while(contadorNegativos<=11):

     parNegativo=DiezNegativo%2

    if(parNegativo==0):
        print(DiezNegativo)

    DiezNegativo-=1
    contadorNegativos=contadorNegativos+parNegativo