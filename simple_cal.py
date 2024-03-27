from tkinter import *

window = Tk()
window.minsize(width=400, height=400)
window.title('Calculator')

word = Label(text='Enter your expression (e.g., 2 + 3)')
word.pack()

input_entry = Entry()
input_entry.pack()

result_label = Label(text=":") 
result_label.pack()

def btn_clear():
    input_entry.delete(0, END)

def calculator():
    expression = input_entry.get()
    solve = expression.split()
    x = int(solve[0])
    y = solve[1]
    z = int(solve[2])
    if y == '+':
        result = x+z
    elif y == '-':
        result = x-z
    elif y == '*':
        result = x*z
    elif y == '/':
        result = x/z
    else:
        result = 'Invalid expression'
    result_label.config(text=f"Result = {result}")
   
button = Button(text="Calculate", command=calculator)
button.pack()

clear = Button(text='clear', command = btn_clear )
clear.pack()
window.mainloop()