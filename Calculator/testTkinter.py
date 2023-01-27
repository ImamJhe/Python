from tkinter import*
import math
import parser
import tkinter.messagebox
import time

root = Tk()
root.title("Scientific Calculator")
root. configure(bg="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

txtDisplay = Entry (calc, font = ('arial', 20 , 'bold', ), bg ='powder blue', bd = 30, width= 28, justify = RIGHT)
txtDisplay.grid(row = 0, column=0, columnspan=4, pady = 1)
txtDisplay.insert (0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2,font =('arial',20,'bold', ), bd = 4, text = numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        time.sleep(0.5)
        i += 1
        
root.mainloop()
