import tkinter as tk

def calculate():
    try:
        result.set(eval(expression.get()))
    except Exception as e:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

expression = tk.StringVar()
result = tk.StringVar()

entry = tk.Entry(root, textvariable=expression, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, command=lambda b=button: expression.set(expression.get() + b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="Calculate", width=5, command=calculate).grid(row=row, column=0, columnspan=4)

result_label = tk.Label(root, textvariable=result)
result_label.grid(row=row+1, column=0, columnspan=4)

root.mainloop()

