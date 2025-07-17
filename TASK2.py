# --------------------------------------------
# Task 2: Calculator
# --------------------------------------------
# PROJECT Description:
# A basic calculator that performs arithmetic operations:
# Addition, Subtraction, Multiplication, and Division.
# --------------------------------------------

def calculate(num1, operator, num2):
    """Performs the arithmetic operation based on the operator."""
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            return num1 / num2
        else:
            return "Invalid operator. Please use +, -, *, or /."
    except Exception as e:
        return f"An error occurred: {e}"

def run_calculator():
    """Runs the calculator by taking user input and displaying the result."""
    print("====================================")
    print("          Python Calcultor   ")
    print("====================================")
    print("Operations: (+  -  *  /)")
    print()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide" )

    try:
        # Input: First number
        num1 = float(input("Enter the first number: "))
        
        # Input: Second number
        num2 = float(input("Enter the second number: "))
        
        # Input: Operator
        operator = input("Choose Operation ( + -  *  / ): ").strip()


        # Perform and display result
        result = calculate(num1, operator, num2)
        print(f"\nResult: {result}")

    except ValueError:
        print("\nError: Please enter valid numeric values.")

# Run the calculator
if __name__ == "__main__":
    run_calculator()
