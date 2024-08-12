import csv
import os
from datetime import datetime

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def csv_a_lista_diccionarios(ruta_csv):
    lista_diccionarios = []
    with open(ruta_csv, mode='r', newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            lista_diccionarios.append(fila)
    return lista_diccionarios

def mostrar_hoteles(hoteles):
    limpiar_pantalla()
    print("\n" + "-"*50)
    print(" " * 15 + "Lista de Hoteles")
    print("-" * 50)
    for hotel in hoteles:
        print(f"ID: {hotel['id']}, Nombre: {hotel['Nombre']}, Tipo: {hotel['Tipo_hotel']}, Rating: {hotel['Rating']}, Precio/Noche: ${hotel['precio_noche']}")
    print("-" * 50)

def mostrar_reservaciones_por_hotel(hotel_id):
    limpiar_pantalla()
    try:
        with open('reservaciones.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            print("\n" + "-"*50)
            print(" " * 15 + f"Reservaciones para el Hotel ID {hotel_id}")
            print("-" * 50)
            print(f"{'Fecha Inicio':<15}{'Fecha Fin':<15}{'Tipo Habitación':<20}")
            for fila in lector:
                if fila['id_hotel'] == hotel_id:
                    print(f"{fila['fecha_inicio']:<15}{fila['fecha_fin']:<15}{fila['tipo_habitacion']:<20}")
    except FileNotFoundError:
        print("No se han encontrado reservaciones.")
    print("-" * 50)

def calcular_precio_total(precio_noche, fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    dias_estadia = (fecha_fin - fecha_inicio).days
    return dias_estadia * precio_noche

def solicitar_datos_pago():
    print("\n" + "-"*50)
    print("Método de Pago")
    print("-" * 50)
    tarjeta = input("Número de tarjeta de crédito: ").strip()
    nombre = input("Nombre del titular: ").strip()
    fecha_exp = input("Fecha de expiración (MM/AA): ").strip()
    cvv = input("Código de seguridad (CVV): ").strip()

    if not (tarjeta and nombre and fecha_exp and cvv):
        print("Todos los campos de pago son obligatorios.")
        return False
    
    # En un entorno real, aquí se realizaría la verificación del pago.
    print("Pago procesado con éxito.")
    return True

def hacer_reservacion(hoteles):
    limpiar_pantalla()
    id_hotel = input("Ingrese el ID del hotel para hacer la reservación: ")
    tipos_disponibles = {'económica': True, 'presidencial': True, 'normal': True}

    for hotel in hoteles:
        if hotel['id'] == id_hotel:
            print(f"Reserva para el hotel {hotel['Nombre']}")
            tipo_habitacion = input("Ingrese el tipo de habitación (económica, presidencial, normal): ").strip().lower()
            if tipo_habitacion not in tipos_disponibles:
                print("Tipo de habitación no válido.")
                return
            
            # Verificar disponibilidad
            reservaciones = []
            try:
                with open('reservaciones.csv', mode='r', newline='', encoding='utf-8') as archivo_csv:
                    lector = csv.DictReader(archivo_csv)
                    for fila in lector:
                        if fila['id_hotel'] == id_hotel and fila['tipo_habitacion'] == tipo_habitacion:
                            reservaciones.append(fila)
            except FileNotFoundError:
                pass
            
            if reservaciones:
                print(f"No hay disponibilidad para habitación {tipo_habitacion} en este hotel.")
            else:
                fecha_inicio = input("Ingrese la fecha de inicio de la reservación (YYYY-MM-DD): ")
                fecha_fin = input("Ingrese la fecha de fin de la reservación (YYYY-MM-DD): ")
                
                # Validar fechas
                try:
                    datetime.strptime(fecha_inicio, "%Y-%m-%d")
                    datetime.strptime(fecha_fin, "%Y-%m-%d")
                except ValueError:
                    print("Fecha inválida. Use el formato YYYY-MM-DD.")
                    return
                
                precio_noche = float(hotel['precio_noche'])
                precio_total = calcular_precio_total(precio_noche, fecha_inicio, fecha_fin)
                print(f"\nPrecio total de la reservación: ${precio_total:.2f}")
                
                if not solicitar_datos_pago():
                    return
                
                with open('reservaciones.csv', mode='a', newline='', encoding='utf-8') as archivo_csv:
                    escritor = csv.writer(archivo_csv)
                    escritor.writerow([id_hotel, fecha_inicio, fecha_fin, tipo_habitacion])
                print("Reservación realizada con éxito.")
            return
    
    print("Hotel no encontrado.")

def main():
    ruta_csv = 'hoteles.csv'
    hoteles = csv_a_lista_diccionarios(ruta_csv)

    while True:
        limpiar_pantalla()
        print("\n" + "-"*50)
        print(" " * 15 + "Bienvenido a la aplicación Reservación de Hoteles")
        print("-" * 50)
        print("1. Ver Hoteles")
        print("2. Ver Reservaciones por Hotel")
        print("3. Hacer Reservación")
        print("4. Salir")
        print("-" * 50)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            mostrar_hoteles(hoteles)
            input("Presiona Enter para continuar...")

        elif opcion == '2':
            hotel_id = input("Ingrese el ID del hotel para ver las reservaciones: ")
            mostrar_reservaciones_por_hotel(hotel_id)
            input("Presiona Enter para continuar...")
        elif opcion == '3':
            hacer_reservacion(hoteles)
            input("Presiona Enter para continuar...")
        elif opcion == '4':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            input("Presiona Enter para continuar...")

            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()