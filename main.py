dato = "oso, perro, 10, 5 son animales"

valores = dato.split(",")

animal1 = valores[0]
animal2 = valores[1]
cantidad_animal2= valores[2]
cantidad_animal1= valores[3].split()[0]

def es_palindromo(palabra):
  return palabra == palabra [:: -1]

if es_palindromo(animal1):
    print(f"{animal1} es un palíndromo")
else:
    print(f"{animal1} no es un palíndromo")

if es_palindromo (animal2):
  print(f"{animal2} es un palíndromo")
else:
  print(f"{animal2} no es un palíndromo")

print (f"tenemos {cantidad_animal1} {animal1.upper()}S")
print (f"tenemos {cantidad_animal2} {animal2}s")
print (f"{animal1} y {animal2} son animales")
