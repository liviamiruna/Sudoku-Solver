import tkinter as tk


def solve_sudoku(board):
    if not find_empty(board):
        return True

    row, col = find_empty(board)

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, row, col, num):

    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def print_board(board):
    for row in board:
        print(row)


def solve_sudoku_gui():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entries[i][j].get()
            if entry == "":
                row.append(0)
            else:
                row.append(int(entry))
        board.append(row)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(tk.END, str(board[i][j]))
    else:
        error_label.config(text="No solution exists.")


# Create the GUI window
window = tk.Tk()
window.title("Sudoku Solver")

entries = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(window, width=3, font=("Arial", 12))
        entry.grid(row=i, column=j, padx=2, pady=2)
        row_entries.append(entry)
    entries.append(row_entries)

# Create a Solve button
solve_button = tk.Button(window, text="Solve", command=solve_sudoku_gui)
solve_button.grid(row=9, column=4, pady=10)

window.mainloop()
