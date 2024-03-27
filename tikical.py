from tkinter import *

win = Tk()

win.geometry("312x325")
win.resizable(0, 0)

win.title('Iya alata Calculator')

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_delete():
    global expression
    expression = input_text.get()
    new_expression = expression[:-1]
    input_text.set(new_expression)

def btn_percent():
    global expression
    expression = input_text.get()
    expression_numeric = float(expression)
    divide = str(expression_numeric / 100)
    result = str(eval(divide))
    input_text.set(result)
    expression(f'{result}')

def btn_click(item):
    global expression 
    expression = expression + str(item)
    input_text.set(expression)

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = f"{result}"

expression = ""

input_text = StringVar()

input_frame = Frame(win, width=312, bd=0, height=50, highlightbackground="gray",highlightthickness=3,highlightcolor="black")
input_frame.pack(side=TOP)

input= Entry(input_frame, width=50, textvariable=input_text, bg="#000", fg="#fff",font=('arial', 21, 'bold'),bd=0, justify=RIGHT)
input.insert(0, '0 ')
input.grid(row=0, column=0)
input.pack(ipady=10)

btn = Frame(win, width=312, height=272.5, bg='black')
btn.pack()

# first row
clear = Button(btn, text='AC', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_clear()).grid(row=0, column=0, padx=1, pady=1)
delete = Button(btn, text='del', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_delete()).grid(row=0, column=1, padx=1, pady=1)
percent = Button(btn, text='%', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_percent()).grid(row=0, column=2, padx=1, pady=1)
divide = Button(btn, text='/', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Second row
one = Button(btn, text='1', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('1')).grid(row=1, column=0, padx=1, pady=1)
two = Button(btn, text='2', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('2')).grid(row=1, column=1, padx=1, pady=1)
three = Button(btn, text='3', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('3')).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btn, text='*', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)
# Third row
four = Button(btn, text='4', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('4')).grid(row=2, column=0, padx=1, pady=1)
five = Button(btn, text='5', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('5')).grid(row=2, column=1, padx=1, pady=1)
six = Button(btn, text='6', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('6')).grid(row=2, column=2, padx=1, pady=1)
plus = Button(btn, text='+', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('+')).grid(row=2, column=3, padx=1, pady=1)

#forth row
seven = Button(btn, text='7', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('7')).grid(row=3, column=0, padx=1, pady=1)
eight = Button(btn, text='8', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('8')).grid(row=3, column=1, padx=1, pady=1)
eight = Button(btn, text='9', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('9')).grid(row=3, column=2, padx=1, pady=1)
equal = Button(btn, text='=', fg='black', width=10, height=6, bd=0, bg='brown', cursor='hand2', command=lambda: btn_equal()).grid(row=3,rowspan=2,column=3,padx=1, pady=1)

# fifth row
zero = Button(btn, text='0', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('0')).grid(row=4, column=0, padx=1, pady=1)
dot = Button(btn, text='.', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('.')).grid(row=4, column=1, padx=1, pady=1)
minus = Button(btn, text='-', fg='black', width=10, height=3, bd=0, bg='brown', cursor='hand2', command=lambda: btn_click('-')).grid(row=4, column=2, padx=1, pady=1)

win.mainloop()