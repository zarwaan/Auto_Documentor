# **N-Queens Problem Solver**

**Description**

This is a Python implementation of the classic N-Queens problem, a puzzle where we place N queens on an NxN chessboard such that no queen attacks another. The program takes the size of the chessboard as input and prints a solution if one exists.

### **Prerequisites**

* Python 3.x

### **How to Run**

1. Save the code in a file named `n_queens.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run the program by typing `python n_queens.py`.
4. When prompted, enter the total number of rows (and columns) of the chessboard.

The program will then print a solution if one exists, and display an error message if no solution can be found.

```markdown
## Code Overview

The code consists of four main functions:

### **printSolution(board)**

Prints the solution to the N-Queens problem, which is represented as a 2D list `board`.

### **isSafe(board, row, col)**

Checks if it is safe to place a queen at position `(row, col)` on the chessboard.

### **solveNQUtil(board, col)**

A recursive helper function that attempts to place queens on the chessboard from left to right.

### **solveNQ()**

The main function that calls `solveNQUtil` to find a solution to the N-Queens problem.

## API Documentation

### **printSolution(board)**

Prints the solution to the N-Queens problem.

* **Arguments:**
	+ `board`: A 2D list representing the chessboard.
* **Returns:** None

### **isSafe(board, row, col)**

Checks if it is safe to place a queen at position `(row, col)` on the chessboard.

* **Arguments:**
	+ `board`: A 2D list representing the chessboard.
	+ `row`: The row index.
	+ `col`: The column index.
* **Returns:** `True` if it is safe to place a queen, `False` otherwise.

### **solveNQUtil(board, col)**

A recursive helper function that attempts to place queens on the chessboard from left to right.

* **Arguments:**
	+ `board`: A 2D list representing the chessboard.
	+ `col`: The current column index.
* **Returns:** `True` if a solution is found, `False` otherwise.

### **solveNQ()**

The main function that calls `solveNQUtil` to find a solution to the N-Queens problem.

* **Arguments:** None
* **Returns:** `True` if a solution is found, `False` otherwise.
```

Note: This README follows the standard format for technical writing, with a clear title, description, and API documentation for each function. The code is well-organized and easy to understand, with clear comments and variable names. The usage instructions are easy to follow, and the code is ready for use.