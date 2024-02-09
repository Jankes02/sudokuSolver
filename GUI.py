import tkinter as tk
GRID_SIZE = 9


def validate_input(char):
    return char.isdigit()


def solve():
    pass


def create_window():
    root = tk.Tk()
    root.title("Sudoku Solver")

    grid_frame = tk.Frame(root, width=500, height=600)
    grid_frame.grid(row=0, column=0, padx=10, pady=2)
    
    info_frame = tk.Frame(root, width=500, height=600)
    info_frame.grid(row=0, column=1, padx=10, pady=2)

    group_frames = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            group_frames[i][j] = tk.Frame(grid_frame)
            group_frames[i][j].grid(row=i, column=j, padx=3, pady=3)
        
    entries = [[None] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            group_row = i // 3
            group_col = j // 3
            group_frame = group_frames[group_row][group_col]
            entries[i][j] = tk.Entry(group_frame, width=2, font=('Arial', 40), validate='key', validatecommand=(root.register(validate_input), '%S'), justify='center')
            entries[i][j].grid(row=i % 3, column=j % 3, padx=1, pady=1)

    buttons_frame = tk.Frame(info_frame)
    buttons_frame.grid(row=0, column=0, pady=30)
    solve_button = tk.Button(buttons_frame, width=15, height=2, text='Solve', command=solve)
    solve_button.grid(row=0, column=0, padx=10)
    clear_button = tk.Button(buttons_frame, width=15, height=2, text='Clear', command=lambda: [[entry.delete(0, 'end') for entry in row] for row in entries])
    clear_button.grid(row=0, column=1, padx=10)

    output_text = tk.Text(info_frame, height=2, width=30)
    output_text.grid(row=1, column=0)
    output_text.bind("<Key>", lambda e: "break")

    root.mainloop()
