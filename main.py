from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("\nCalculadora en Python")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {sumar(num1, num2)}")
        
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {restar(num1, num2)}")
        
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {multiplicar(num1, num2)}")
        
        elif opcion == "4":
            num1 = float(input("Ingrese el numerador: "))
            num2 = float(input("Ingrese el denominador: "))
            try:
                print(f"Resultado: {dividir(num1, num2)}")
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero")
        
        elif opcion == "5":
            numeros = input("Ingrese números separados por espacios: ").split()
            numeros = [float(num) for num in numeros]
            print(f"Resultado: {suma_avanzada(*numeros)}")
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
