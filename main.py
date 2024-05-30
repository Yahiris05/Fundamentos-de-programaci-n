#Iteracion sobre la lista de nombres. 
#Que imprima solamente los nombres que tengan igual o más de tres vocales.

vocales = ['a','e','i','o','u','A','E','I','O','U',
   'á','é','í','ó','ú','Á','É','Í','Ó','Ú']
nombre= input("Ingrese un nombre: ")
    
contador=0
for letra in nombre:
  if letra in vocales:
    contador += 1
if contador >= 3:
  print('El nombre', nombre, 'tiene', contador, 'vocales')
elif contador < 3: 
  print('El nombre', nombre, 'no tiene 3 vocales')

        