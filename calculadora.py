import suma as file_suma
import resta as file_resta
import multiplicacion as file_multiplicacion
import division as file_division

def calculadora():
    print("Bienvenido a la calculadora básica")
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    while True:
        opcion = input("Ingrese el número de la operación (1/2/3/4) o 'q' para salir: ")
        
        if opcion == 'q':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
                continue

            if opcion == '1':
                print(f"{num1} + {num2} = {file_suma.suma(num1, num2)}")
            elif opcion == '2':
                print(f"{num1} - {num2} = {file_resta.resta(num1, num2)}")
            elif opcion == '3':
                print(f"{num1} * {num2} = {file_multiplicacion.multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"{num1} / {num2} = {file_division.division(num1, num2)}")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()