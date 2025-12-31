import tkinter as tk
def press(v):
    entry.insert(tk.END, v)
def clear():
    entry.delete(0, tk.END)
def cal() :
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
root = tk.Tk()
root.title("Calculator")
root.config(bg='#1e1e1e')
root.resizable(False, False)
entry = tk.Entry(root, font=("Segoe UI", 20), bg='#2d2d2d', fg='white', bd=0, justify = "right")
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+',  '='
]

r = 1
c = 0
for b in buttons:
    cmd = cal if b == '=' else lambda x=b: press(x)
    tk.Button(root, text=b, command=cmd, width=5, height=2, font=("Segoe UI", 14), bg ='#ff9500' if b in "+-*/=" else '#3a3a3a', fg='white', bd=0).grid(row=r, column=c, padx=6, pady=6)
    c += 1
    if c == 4:
        c = 0
        r += 1
tk.Button(root, text='C', width=22, height=2, font=("Segoe UI", 14), bg='#ff3b30', fg='white', bd=0, command=clear).grid(row=r, column=0,pady=8, columnspan=4)
root.mainloop()