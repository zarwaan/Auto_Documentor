**Simple Command-Line Calculator**
=====================================

**Description**
---------------

This is a simple command-line calculator that performs basic arithmetic operations (+, -, \*, /) on floating-point numbers. The calculator displays a menu to the user, allowing them to select the operation they wish to perform.

**Prerequisites**
-----------------

* Python 3.x (tested on Python 3.8 and above)
* A computer with a terminal or command prompt capable of running Python scripts

**How to Run**
--------------

1. Clone this repository to your local machine using your preferred method (e.g., `git clone https://github.com/username/calculator.git`).
2. Navigate to the project directory in your terminal or command prompt.
3. Run the calculator script using Python: `python calculator.py` (or `python3 calculator.py` in some environments).
4. Follow the on-screen instructions to select an operation and enter numbers.

**Example Usage**
-----------------

```
$ python calculator.py
1:+, 2:-, 3:*, 4:/
Enter choice (1-4): 2
Num 1: 5
Num 2: 3
Result: 2.0
```

**Troubleshooting**
------------------

* If you encounter an error message stating "Invalid number input.", ensure that you have entered valid decimal numbers for the operands.
* If you encounter an error message stating "Invalid choice.", ensure that you have selected a valid operation number (1-4).

**Code Explanation**
-------------------

The calculator script defines a `calculator` function that uses a dictionary `ops` to map operation symbols to their corresponding functions and operations. The user's choice is validated, and if input, the calculator attempts to parse and validate the operands. Finally, the operation is performed, and the result is displayed.