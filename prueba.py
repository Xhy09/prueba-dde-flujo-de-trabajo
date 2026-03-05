# calculadora.py - Versión 2.0.0
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def calculadora():
    print("=== Calculadora Básica v2.0.0 ===")
    print("Operaciones: Suma | Resta | Multiplicación")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        print(f"\nResultados:")
        print(f"Suma: {num1} + {num2} = {suma(num1, num2)}")
        print(f"Resta: {num1} - {num2} = {resta(num1, num2)}")
        print(f"Multiplicación: {num1} * {num2} = {multiplicacion(num1, num2)}")
        
    except ValueError:
        print("Error: Por favor ingresa números válidos")

if __name__ == "__main__":
    calculadora()