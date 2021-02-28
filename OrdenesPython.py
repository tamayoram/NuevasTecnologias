# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:34:04 2020

@author: admin
"""

from datetime import datetime
birthday=datetime(1982,4,22)
birthday.year
birthday.weekday()
datetime.now()
edad=datetime.now()-birthday
print(edad)
parsed_date=datetime.strptime('Jan 15, 2018','%b %d, %Y')
parsed_date.year
print(parsed_date)

# abrir archivos con python

with open('bad_bands.txt','w') as bad_bands_doc:
  bad_bands_doc.write('Bad Bunny')

with open('bad_bands.txt','a') as bad_bands_doc:
  bad_bands_doc.write(' ,Maluma')
  
# abrir csv
  
  
  
  import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict=csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])
    
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
    
import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = [book['ISBN'] for book in books_reader]
  print(isbn_list)
  

# escribir un archivo csv
  access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
    log_writer.writeheader()
    for item in access_log:
      log_writer.writerow(item)
      
# Leer un formato JSON
      
import json
with open('message.json') as message_json:
  message=json.load(message_json)
print(message['text'])
print(message['secret text'])

#Escribir formato JSON

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json
with open('data.json','w') as data_json:
  json.dump(data_payload,data_json)
  
# ejercicio completo para leer y escribir
  import csv
  compromised_users=[] # crear una lista vacía
  with open('passwords.csv') as password_file:
      password_csv=csv.DictReader(password_file) #creando un diccionario con la información que se lee en el open
      for password_row in password_csv:
          compromised_users.append(password_row['Username'])#se adiciona en la lista el username del archivo que se lee

with open('compromise_users.txt','w') as compromised_user_files:
    for compromise_user in compromised_users:
        compromised_user_files.write(compromise_user)#se graba los usuarios
    
import json
with open('boss_message.json','w') as boss_message:
    boss_message_dict={
            'recipient':'The boss',
            'message':'Mission Success'
                        
            }
    json.dump(boss_message_dict,boss_message)

# ejercicio de web scrapping
import requests     # librería para leer url
webpage_response=requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html') #llamar la página y almacenar su contenido en una variable
webpage=webpage_response.content #almacenar el contenido en una variable
#print(webpage) #visualir el contenido

from bs4 import BeautifulSoup # librería para organizar la información
soup = BeautifulSoup(webpage, "html.parser") #Crear un objeto beatifulsoup
print(soup) # con el objeto se observa un html ordenado

soup = BeautifulSoup('<p class="text">Click to learn more about each turtle</p>')

print(soup.p) # ver un p específico

print(soup.p.string) #obtener el string del p

for child in soup.div.children:
    print(child) # imprimir lo que hay en el primer div
    
# diferente maneras de buscar elementos en el archivo html

turtle_links = soup.find_all("a")
print(turtle_links)

soup.find_all(['h1', 'a', 'p'])

soup.find_all(attrs={'class':'banner'})

soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})

def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"
 
soup.find_all(has_banner_class_and_hello_world)









