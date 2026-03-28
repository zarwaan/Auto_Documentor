def calculator():
    """Simple command-line calculator."""
    ops = {'1': ('+', lambda x, y: x + y), 
           '2': ('-', lambda x, y: x - y),
           '3': ('*', lambda x, y: x * y), 
           '4': ('/', lambda x, y: x / y if y != 0 else "Error")}

    print("1:+, 2:-, 3:*, 4:/")
    choice = input("Enter choice (1-4): ")
    if choice in ops:
        try:
            n1 = float(input("Num 1: "))
            n2 = float(input("Num 2: "))
            op_sym, func = ops[choice]
            print(f"Result: {func(n1, n2)}")
        except ValueError:
            print("Invalid number input.")
    else:
        print("Invalid choice.")