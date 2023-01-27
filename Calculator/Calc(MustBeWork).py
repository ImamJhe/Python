from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="Powder Blue")
root.resizable(width=False, height=False)
root.geometry("494x568+0+0")

calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=29, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad ="789567123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i += 1
#=================#===============#==============#====================
btnClear = Button(calc, text =chr(67), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=0, pady =1)

btnAllClear = Button(calc, text =chr(67) + chr (69), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=1, pady =1)

btnSq = Button(calc, text = "√", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=2, pady =1)

btnAdd = Button(calc, text =chr (43), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=3, pady =1)

btnMult = Button(calc, text =chr (42), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 2, column=3, pady =1)

btnSub = Button(calc, text = chr(45), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 3, column=3, pady =1)

btnDiv = Button(calc, text =chr (247), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 4, column=3, pady =1)

btnZero = Button(calc, text =chr (48), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=0, pady =1)

btnDot = Button(calc, text =".", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=1, pady =1)

btnPM = Button(calc, text =chr (177), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=2, pady =1)

btnEquals = Button(calc, text =chr (61), width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=3, pady =1)

#================================Scientific====================================================================

btnPi = Button(calc, text ="π", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=4, pady =1)

btnCos = Button(calc, text ="Cos", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=5, pady =1)

btnTan = Button(calc, text = "Tan", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=6, pady =1)

btnSin = Button(calc, text ="Sin", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 1, column=7, pady =1)

#================================================================================================================

btn2Pi = Button(calc, text ="2π", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 2, column=4, pady =1)

btnCosh = Button(calc, text = "Cosh", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 2, column=5, pady =1)

btnTanh = Button(calc, text ="Tanh" , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 2, column=6, pady =1)

btnSinh = Button(calc, text ="Sinh" , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 2, column=7, pady =1)

#=================================================================================================================
btnLog = Button(calc, text ="Log", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 3, column=4, pady =1)

btnExp = Button(calc, text ="Exp" , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 3, column=5, pady =1)

btnMod = Button(calc, text ="Mod", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 3, column=6, pady =1)

btnE = Button(calc, text = chr(69) , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 3, column=7, pady =1)

#=================================================================================================================

btnLog2 = Button(calc, text ="log2", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 4, column=4, pady =1)

btnDeg = Button(calc, text ="deg" , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 4, column=5, pady =1)

btnacosh = Button(calc, text ="acosh", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 4, column=6, pady =1)

btnasinh = Button(calc, text ="asinh", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row =4, column=7, pady =1)

#============================================================================================================

btnLog10 = Button(calc, text ="log10", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=4, pady =1)

btnlog1p = Button(calc, text ="log1p" , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=5, pady =1)

btnexpm1 = Button(calc, text ="expm1" , width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row = 5, column=6, pady =1)

btnalgamma = Button(calc, text ="lgamma", width = 6, height=2,font =('arial',20,'bold', ), bd = 4,
                  bg = 'powder blue').grid(row =5, column=7, pady =1)

lblDisplay = Label(calc, tect="Scientific Calculator", font = ('arial', 30, 'bold'), justify = CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan =4)

#============================Menu=====================================
def iExit ():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")

def Stantard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")


menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Stantard", command=Stantard)
filemenu.add_command(label="Scientific", command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="View Help")

root.config(menu=menubar)
root.mainloop()

