# calculadora.py - Versión 1.0.0
def calculadora():
    print("=== Calculadora Básica v1.0.0 ===")
    print("Operación: Suma")
    
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado}")
        
    except ValueError:
        print("Error: Por favor ingresa números válidos")

if __name__ == "__main__":
    calculadora()