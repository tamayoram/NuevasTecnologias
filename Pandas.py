# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:34:50 2021

@author: admin
"""

##### Lambda function

contains_a= lambda word: 'a' in word

print contains_a('banana')
print contains_a("apple")
print contains_a("cherry")

#### la palabra supera una longitud de 12

long_string= lambda str: len(str)>12

print long_string("short")
print long_string("photosynthesis")

##### ùltimo caracter

ends_in_a=lambda str:str[-1]=='a'

print ends_in_a("data")
print ends_in_a("aardvark")

#### if / else en funciones lambda

double_or_zero=lambda num:num*2 if num>10 else 0

print double_or_zero(15)
print double_or_zero(5)


#####Par o impar

even_or_odd=lambda num:'even' if num%2==0 else 'odd'

print even_or_odd(10)
print even_or_odd(5)

#### comparativo con mayor que

rate_movie=lambda rating:'I liked this movie' if rating>8.5 else 'This movie was not very good'

### nùmeros aleatorios

import random
#Write your lambda function here

add_random= lambda num: num + random.randint(1,10) 

print add_random(5)
print add_random(100)

### Crear un dataframe
import pandas as pd
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name':['t-shirt','t-shirt','skirt','skirt'],
  'Color':['blue','green','red','black']
})

print(df1)

### Crear un dataframe forma 2

import pandas as pd

df2=pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]  
              ],
  columns=['Store ID','Location','Number of Employees']) 
  

print(df2)

## Crear un dataframe desde CSV
import pandas as pd
df=pd.read_csv('cupcakes.csv')

print(df)

print(df.info())

## Crear un dataframe desde CSV
import pandas as pd
df=pd.read_csv('logger.csv')

print(df)
print(df.head())

print(df.info())

###Seleccionar una columna
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],

  columns=['month', 'clinic_east','clinic_north', 'clinic_south',
           'clinic_west']
)

print(df)

clinic_north=df['clinic_north']
print(clinic_north)
print(type(clinic_north))
print(type(df))

### Seleccionar múltiples columnas
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south=df[['clinic_north','clinic_south']]
print(clinic_north_south)
print(type(clinic_north_south))

#Leer informaciòn de archivo csv
import pandas as pd
inventory=pd.read_csv('inventory.csv')
print(inventory)
print(inventory.head(10))

staten_island=inventory.head(10)

product_request=staten_island['product_description']
print(product_request)

seed_request=inventory[(inventory.location =='Brooklyn')& (inventory.product_type=='seeds')]
# selección de filas con condiciones

inventory['in_stock']=inventory.apply(lambda row : True if row.quantity>0 else False, axis=1)
# se adiciona una nueva columna basado en un condiciòn if
# el axis=1 es para que el sistema entienda que arranca en la fila 1



inventory['total_value']=inventory['price']*inventory['quantity']





combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,row.product_description)
# forma de crear un formato estàndar


inventory['full_description']=inventory.apply(combine_lambda,axis=1)

print(inventory.head(10))



# medidas agregadas
import pandas as pd
import numpy as np
orders=pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive=orders.price.max() #máximo
num_colors=orders.shoe_color.nunique()#cantidad de colores únicos

print(most_expensive)
print(num_colors)

print(orders.columns)

pricey_shoes=orders.groupby('shoe_type').price.max() # máximos agrupados





pricey_shoes = orders.groupby('shoe_type').price.max().reset_index() #convierte los datos filtrados en un nuevo dataframe con estructura

print(pricey_shoes)

print(type(pricey_shoes)) # Se ve que es un dataframe


cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
# el dataframe orders se agrupa por categoría y se calcula para cada categoría el percentil 25. Luego se convierte todo a un data frame.
print(cheap_shoes)


shoe_counts=orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()
# agrupaciones por dos conceptos
print(shoe_counts)

shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id').reset_index()

#reorganización de la tabla se define las columnas, las filas o index y los valores.
# Importante, el pivot es de data frames previos como shoe_counts no es de la base de datos original. 
print(shoe_counts_pivot)


#*****************************************************************************

import pandas as pd

ad_clicks=pd.read_csv('ad_clicks.csv')#lectura de una base de datos en csv para crear un dataframe.

print(ad_clicks.head()) #Ver las primeras 10 líneas del archivo

ad_clicks.groupby('utm_source').user_id.count() #Cuenta cada uno de los registros por la columna fuente.

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#se crea una nueva columna que se llama is_click. El símbolo ~ permite evaluar si es o no nulo.

clicks_by_source=ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
#agrupaciòn por dos variables y conteo

print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
    columns='is_click',
    index='utm_source',
    values='user_id').reset_index()

#Se reorganiza la tabla modificando columnas y filas


clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

#se crea una nueva columnas denominada percent_clicked y esta columna es el resultado de dividir la columna True respecto al total. 


print(clicks_pivot)


 ad_clicks.groupby('experimental_group').user_id.count()
 # Agrupación y conteo para la columna experimental group
 
 
clicks_by_experimental=ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
#agrupaciòn por dos variables y conteo


clicks_pivot = clicks_by_experimental.pivot(
    columns='is_click',
    index='experimental_group',
    values='user_id').reset_index()


print(clicks_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
# se clasifica la informaciòn de aquellos datos en la columna experimental group que son iguales a A

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

print(a_clicks)

#********************************************************************
# Múltiples dataframes






