"""
🧮 Smart Calculator
A fully functional calculator with support for basic and advanced operations.
Author: Priyanka
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

def calculator():
    print("=" * 40)
    print("   🧮 SMART CALCULATOR")
    print("=" * 40)
    
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("7. Exit")
        
        choice = input("\nSelect operation (1-7): ").strip()
        
        if choice == '7':
            print("\n👋 Thank you for using Smart Calculator!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("❌ Invalid choice! Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue
        
        operations = {
            '1': ('+', add),
            '2': ('-', subtract),
            '3': ('×', multiply),
            '4': ('÷', divide),
            '5': ('^', power),
            '6': ('%', modulus)
        }
        
        symbol, func = operations[choice]
        result = func(num1, num2)
        print(f"\n✅ Result: {num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()
