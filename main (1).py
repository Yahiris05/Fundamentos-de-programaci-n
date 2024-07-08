# Leer un texto y realizar las siguientes operaciones:
Text = input("Ingrese un texto: ") 

Capital_letters = Text.upper()  #1) Retornar el texto en Mayusculas
print("Texto en mayusculas: ", Capital_letters)

Lowercase = Text.lower()  #2) Retornar el texto en Minusculas
print ("2) Texto en minusculas:" , Lowercase)

First_two_characters = Text[:2]  #3) Retornar los dos primeros caracteres
print("3) Dos primeros caracteres: ", First_two_characters)

Last_two_characters = Text[-2:] #4) Retornar los dos últimos caracteres
print("4) Dos ultimos caracteres: ", Last_two_characters)

Last_character = Text[-1]  if Text else "" #5) Retornar el último caracter
Repetitions = Text.count (Last_character)
print ("5) Repeticiones del ultimo caracter: ", Repetitions)

Reversed = Text[::-1]  #6) Retornar el texto invertido
print ( "6) Texto invertido: ", Reversed)