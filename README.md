**Simple Command-Line Calculator**
=====================================

**Description**
---------------

This is a basic command-line calculator that performs addition, subtraction, multiplication, and division operations. It uses a dictionary to map user input to the corresponding mathematical operations.

**Prerequisites**
----------------

* Python 3.6 or later (due to the use of f-strings for formatting output)

**How to Run**
--------------

1. Save the code in a file with a `.py` extension, e.g., `calculator.py`.
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using Python, e.g., `python calculator.py`.
4. Follow the prompts to enter your choice of operation, the first number, and the second number.
5. The calculator will display the result of the operation.

**Code**
------

```python
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

# Run the calculator
calculator()
```