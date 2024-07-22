def es_par_o_impar(numero):
  if numero % 2 == 0:
      return "Par"
  else:
      return "Impar"

numero=int(input ("ingrese un numero: "))
resultado=es_par_o_impar(numero)
print("El numero es:",resultado)
