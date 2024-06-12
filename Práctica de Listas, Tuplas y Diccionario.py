#Primera Parte
# Aarón Rafael Beltre Guillen 24-1033
print("\n\n-----Primera Parte----- \n\n")

nums = [1,3,4,6,7,7,6,12,24,78,100,123]
print(f"Lista: ", nums)
multiplos3 =[]
for x in nums:
    if x%3==0:
        multiplos3.append(x)

print(f"\nLista filtrada (Solo los multiplos de 3): ")
del(multiplos3)

#Otros métodos, La version Pythonica
multiplos3 = [num for num in nums if num % 3 == 0]
print(multiplos3)


print("\n\n-----Segunda Parte----- \n\n")
#2.Operaciones Matematicas
sum = 0
producto = 1
for x in nums:
    sum += x 
    producto *= x
print(f"El producto es: {producto}\nLa suma es: {sum}\nLa media es {float(sum)/len(nums)}")

#3.Acceder y Modificar elementos 

#A.Diccionario
print("\n\n-----Tercera Parte----- \n\n")
dias_semana = {1:"Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5:"Viernes", 6:"Viernes"}
print("----- Diccionarios----- \n\n")
print("Dias de la semana (Mal formateadas) ",dias_semana)
dias_semana[7] = "Domingo"
dias_semana[6] = "Sabádo"
print("Dias de la semana (Arreglada formateadas) ",dias_semana)

#Listas
print("\n\n----- Listas----- \n\n")
print("Aceder el los elementos del 6 al último: ",nums[5:-1])
nums[5] = 10000
print("Lista modificada: 6to elemento, es 1000", nums)

#Tuplas 
# Nota: las tuplas no pueden ser modificadas luego de ser declaradas
print("\n\n----- Tuplas ----- \n\n")


numeros = (1,2,3,4,5,6,7,10)
print("Tuplas: ",numeros)
print("Segundo elemento de la tupla: ",numeros[1])





    

