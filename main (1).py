def es_primo(x):
  cuenta = 0
  for i in range(x)[1:]:
      if x%i == 0:
          cuenta += 1
  if cuenta == 1:
      return True
  return False

a = input("Digite el primer numero: ")
b = input("Digite el segundo numero: ")

c = int(a) - int(b) 
if c%2 == 0:
  print("La diferencia es par. Aquí está la suma de dígitos: ", end="")
  sum = 0
  for x in a:
      sum += int(x)
  for x in b:
      sum += int(x)
  print(sum)

if(es_primo(c)):
  print("La diferencia es prima. Aquí está el producto: ", end="")
  print(int(a)*int(b))

if c%10 == 4:
  print("El numero es par. Aquí están los digitos por separado.")
  for x in a:
      print(x, end=" ")
  for x in b:
      print(x, end=" ")
  print("\n")