def es_palindromo(palabra):
  palabra = palabra.replace(" ", "").lower()
  return palabra == palabra[::-1]

print (es_palindromo("Anita lava la tina"))