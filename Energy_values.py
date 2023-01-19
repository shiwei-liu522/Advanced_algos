#Python 3
'''
Problem: Infer Energy Values of Ingredients
Problem Introduction
In this problem, you will apply Gaussian Elimination to infer the energy values of ingredients given a restaurant menu
with calorie counts and ingredient lists provided for each item.
The goal is to find the energy values of the ingredients, which will allow you to estimate the calorie counts of any new menu item.

Problem Description
Task: You are given a set of n ingredients, each with its own energy value. You are also given a set of m menu items,
each with a list of ingredients and a calorie count. Your goal is to infer the energy values of the ingredients,
which will allow you to estimate the calorie counts of any new menu item.
Input Format. The first line of the input contains integers n and m. Each of the following n lines defines the energy value of one ingredient.
The next line contains the list of ingredients of the first menu item, followed by its calorie count.
The ingredients of each menu item are given in non-decreasing order of their energy values.
The last line contains the list of ingredients of the last menu item, followed by its calorie count.
Constraints. 1 ≤ n, m ≤ 100; 0 ≤ energy value of an ingredient ≤ 104; 0 ≤ calorie count of a menu item ≤ 106; 1 ≤ number of ingredients in a menu item ≤ 10; all the numbers are integers.
Output Format. Output n real numbers — the energy values of the ingredients. The i-th of these numbers should correspond to the energy value of the i-th ingredient in the input. Your answer will be considered correct if its absolute or relative error does not exceed 10−6.
'''

# python3

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEqu():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def DivideRow(a, b, row, value):
    for key, v in enumerate(a[row]):
        a[row][key] /= value
    b[row] /= value


def AddRow(a, b, b_add, row_add, index_row_receive):
    for column, value in enumerate(row_add):
        a[index_row_receive][column] += value
    b[index_row_receive] += b_add

def SelectPivotElement(a, used_rows, used_columns, b):
    pivot_element = Position(0, 0)
    while used_columns[pivot_element.column]:
        pivot_element.column += 1

    while pivot_element.row < len(a) and (
            used_rows[pivot_element.row] or a[pivot_element.row][pivot_element.column] == 0):
        pivot_element.row += 1

    if pivot_element.row == len(a):
        pivot_element.row = 0
        while used_columns[pivot_element.row]:
            pivot_element.row += 1
        return pivot_element

    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[
        pivot_element.column]
    pivot_element.row = pivot_element.column


def ProcessElement(a, b, pivot_element):
    row_add = []
    b_add = 0
    DivideRow(a, b, pivot_element.row, a[pivot_element.row][pivot_element.column])
    for row in range(len(a)):
        if row != pivot_element.row:
            row_add = [x * (-a[row][pivot_element.column]) for x in a[pivot_element.row]]
            b_add = b[pivot_element.row] * (-a[row][pivot_element.column])
            AddRow(a, b, b_add, row_add, row)

def PrintCol(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

def SolveEqu(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns, b)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b


EPS = 1e-6
PRECISION = 20

if __name__ == "__main__":
    equation = ReadEqu()
    solution = SolveEqu(equation)
    PrintCol(solution)
    exit(0)