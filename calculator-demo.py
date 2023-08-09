import tkinter as tk
from tkinter import ttk

#calculator function button
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))
def button_clear():
    entry.delete(0, tk.END)
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")

# window
window = tk.Tk()
window.title('Siesta Calculator Demo')
window.geometry('300x600')

# create text entry widget
entry = tk.Entry(window,width=18,justify='right',font='Calibri 24 bold')
entry.grid(row=0,column=0,columnspan=10)

# create number buttons
for i in range(9):
    button = tk.Button(window, text=str(i+1), padx=30, pady=30, command=lambda i=i: button_click(i+1))
    button.grid(row=i // 3 + 1, column=i % 3)
# create operator buttons
operators = ['+','-','*','/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, padx=30, pady=30, command=lambda operator=operator: button_click(operator))
    button.grid(row=i + 1, column=3)
# create other buttons
# zero button
button_zero = tk.Button(window, text='0', padx=30, pady=30, command=lambda: button_click(0))
button_zero.grid(row=4,column=1)
#clear button
button_clear = tk.Button(window, text='C', padx=30, pady=30, command=button_clear)
button_clear.grid(row=4, column=0)
# button equal
button_equal = tk.Button(window, text='=',padx=30, pady=30, command= button_equal)
button_equal.grid(row=4, column=2)

# run
window.mainloop()