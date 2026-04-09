**README.md**
================

**Title**
--------

N-Queens Problem Solver
------------------------

**Description**
------------

This is a Python program that solves the N-Queens problem, a classic puzzle in which N queens must be placed on an NxN chessboard such that no two queens attack each other.

**Prerequisites**
----------------

* Python 3.x

**How to Run**
--------------

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/NQueens-Solver.git
```

### Step 2: Install Required Packages (optional)

This program does not require any external packages, but if you want to run it from a IDE like PyCharm, you can install the `py_compile` and `unittest` packages:

```bash
pip install py_compile unittest
```

### Step 3: Run the Program

```bash
python nqueens_solver.py
```

You will be prompted to enter the number of queens (N). Enter a positive integer and press Enter.

### Step 4: View the Solution

If a solution exists, the program will print the final configuration of the queens on the board.

### Note

* The program uses a recursive backtracking algorithm to find a solution.
* The `solveNQUtil` function is used to recursively place queens on the board, and the `isSafe` function checks whether it is safe to place a queen at a given position.
* The program prints the solution in a grid format, where 1s represent queens and 0s represent empty squares.

```python
# nqueens_solver.py
import os

# Global variables
global N

def printSolution(board):
    """Prints the final configuration of the queens on the board"""
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    """Checks whether it is safe to place a queen at a given position"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    """Recursively places queens on the board to find a solution"""
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQUtil(board, col + 1) == True:
                return True

            board[i][col] = 0

    return False

def solveNQ():
    """Solves the N-Queens problem"""
    global n
    board = [[0] * n for _ in range(n)]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

n = int(input("Enter total number of rows: "))
N = n
solveNQ()
```