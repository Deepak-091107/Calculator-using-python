def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        try:
            user_input = input("Enter expression (e.g. 5 + 3): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            for op in ['+', '-', '*', '/']:
                if op in user_input:
                    parts = user_input.split(op)
                    if len(parts) == 2:
                        a, b = float(parts[0].strip()), float(parts[1].strip())
                        if op == '+':
                            result = a + b
                        elif op == '-':
                            result = a - b
                        elif op == '*':
                            result = a * b
                        elif op == '/':
                            if b == 0:
                                print("Error: Division by zero\n")
                                break
                            result = a / b
                        print(f"Result: {result}\n")
                        break
            else:
                print("Invalid input. Please try again.\n")

        except ValueError:
            print("Error: Invalid numbers. Please try again.\n")

if __name__ == "__main__":
    calculator()
