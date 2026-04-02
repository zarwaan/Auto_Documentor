**Simple Command-Line Calculator**
=====================================

**Description**
---------------

This is a simple command-line calculator that performs basic arithmetic operations, such as addition, subtraction, multiplication, division, and squaring. The calculator takes user input using a numbered menu and allows users to enter two numbers (for operations 1-4) or a single number (for operation 5).

**Prerequisites**
----------------

* Python 3.x installed on your system
* A terminal or command prompt to run the calculator

**How to Run**
--------------

1. Save this code in a file named `calculator.py`.
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the command `python calculator.py` to execute the calculator.
4. Follow the on-screen menu to enter your choice and numbers.

**Example Usage**
----------------

```
$ python calculator.py
1:+, 2:-, 3:*, 4:/, 5:^2
Enter choice (1-5): 3
Num 1: 4
Num 2: 5
Result: 20

$ python calculator.py
1:+, 2:-, 3:*, 4:/, 5:^2
Enter choice (1-5): 5
Enter number: 4
Result: 16

$ python calculator.py
1:+, 2:-, 3:*, 4:/, 5:^2
Enter choice (1-5): 4
Num 1: 10
Num 2: 0
Error: Division by zero
```

Note: This code uses a dictionary to map user input to mathematical operations, making it easy to add or remove operations in the future. However, it does not handle multiple-digit numbers or more complex mathematical operations.