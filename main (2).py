def capturar_notas():
    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        matricula = input("Ingrese la matrícula del estudiante: ")

        notas = []
        for i in range(1, 5):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {i}: "))
                    if 0 <= nota <= 100:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 100. Intente nuevamente.")
                except ValueError:
                    print("Entrada no válida. Por favor ingrese un número.")

        promedio = sum(notas) / len(notas)

        if promedio <= 69:
            resultado = "tiene un promedio de 1.0 y reprobó"
        elif 70 <= promedio <= 79:
            resultado = "tiene un promedio de 2.0 y aprobó"
        elif 80 <= promedio <= 89:
            resultado = "tiene un promedio de 3.0 y aprobó"
        else:  # 90 <= promedio <= 100
            resultado = "¡Felicidades! tiene un promedio de 4.0 y aprobó"

        print(f"{nombre_estudiante} ({matricula}) {resultado}")

        otra_vez = input("¿Desea ingresar otro estudiante? (s/n): ").strip().lower()
        if otra_vez != 's':
            break

    print("Captura de datos finalizada.")

capturar_notas()
