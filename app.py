def calculator():
    """Simple command-line calculator."""
    
    ops = {
        '1': ('+', lambda x, y: x + y), 
        '2': ('-', lambda x, y: x - y),
        '3': ('*', lambda x, y: x * y), 
        '4': ('/', lambda x, y: x / y),
        '5': ('^2', lambda x: x * x)
    }

    print("1:+, 2:-, 3:*, 4:/, 5:^2")
    choice = input("Enter choice (1-5): ")

    if choice in ops:
        try:
            if choice == '5':  # Square operation
                n1 = float(input("Enter number: "))
                op_sym, func = ops[choice]
                print(f"Result: {func(n1)}")
            else:
                n1 = float(input("Num 1: "))
                n2 = float(input("Num 2: "))
                op_sym, func = ops[choice]

                if choice == '4' and n2 == 0:
                    print("Error: Division by zero")
                else:
                    print(f"Result: {func(n1, n2)}")

        except ValueError:
            print("Invalid number input.")
    else:
        print("Invalid choice.")
