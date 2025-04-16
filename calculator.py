def calculadora():
    print("Calculadora sencilla en Python")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")

    try:
        num1 = float(input("Introduce el primer número: "))
        operacion = input("Introduce la operación (+, -, *, /): ")
        num2 = float(input("Introduce el segundo número: "))

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                return
            resultado = num1 / num2
        else:
            print("Operación no válida.")
            return

        print(f"Resultado: {resultado}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    calculadora()
