def celsius_a_fahrenheit(celsius):
  return (celsius * 9/5) + 32

celsius=int(input ("ingrese un grado: "))
conversion=celsius_a_fahrenheit(celsius)
print("La conversión es:", conversion)