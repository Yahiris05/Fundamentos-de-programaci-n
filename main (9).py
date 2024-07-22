def contar_vocales(texto):
  vocales = 'aeiouAEIOU'
  contador = 0
  for letra in texto:
      if letra in vocales:
          contador += 1
  return contador

print (contar_vocales("hola"))