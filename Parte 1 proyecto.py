 # Requisito 1: Declarar Variables y Tipos de Datos
disponibilidad_habitaciones = {
    "02-08-2024": {"individual": 5, "doble": 3},
    "03-08-2024": {"individual": 2, "doble": 4}
}

  # Lista de hoteles con sus detalles
hoteles = [
      {"nombre": "Hotel Sol", "calificacion": 4.2,"precio_noche": 150, "disponibilidad": 
       { "02-08-2024": {"individual": 5, "doble": 3},"03-08-2024": {"individual": 2, 
                                                                    "doble": 4}} },
      {"nombre": "Hotel Luna","calificacion": 3.8,"precio_noche": 120,
          "disponibilidad": {"04-08-2024": {"individual": 1, "doble": 2},
              "05-08-2024": {"individual": 0, "doble": 3}
          }
      }
  ]

 

nombre_usuario = input("Ingrese su nombre: ")

  # Para mostrar la lista de hoteles y permitir seleccionar uno
print("Hoteles disponibles:")
for i, hotel in enumerate(hoteles):
      print(f"{i + 1}. {hotel['nombre']} - Calificación: {hotel['calificacion']}")

seleccion_hotel = int(input("Selecciona el número del hotel que deseas: ")) - 1
hotel_seleccionado = hoteles[seleccion_hotel]

  # Para mostrar las fechas disponibles y la calificación actual del hotel seleccionado
print(f"\nHas seleccionado: {hotel_seleccionado['nombre']}")
print("Fechas disponibles para reservar:")
for fecha in hotel_seleccionado["disponibilidad"]:
      print(f"- {fecha}")

print(f"Calificación actual del hotel: {hotel_seleccionado['calificacion']}")

  # Requisito 2: Implementar Operadores Matemáticos y de Asignación

numero_noches = int(input("¿Cuántas noches deseas reservar?: "))
precio_noche = hotel_seleccionado['precio_noche']
costo_total = precio_noche * numero_noches  
print(f"El costo total de la reservación es: {costo_total}.")


  # Requisito 3: Estructuras de Control de Flujo

fecha_reserva = input("Introduce la fecha de reserva (DD-MM-YYYY): ")
tipo_habitacion = input("Introduce el tipo de habitación (individual/doble): ")

if fecha_reserva in hotel_seleccionado["disponibilidad"]:
      if hotel_seleccionado["disponibilidad"][fecha_reserva][tipo_habitacion] > 0:
          print(f"Habitación {tipo_habitacion} disponible para la fecha seleccionada.")
          hotel_seleccionado["disponibilidad"][fecha_reserva][tipo_habitacion] -= 1 
      else:
          print(f"No hay habitaciones {tipo_habitacion} disponibles para la fecha seleccionada.")
else:
      print ("La fecha seleccionada no está disponible.")
