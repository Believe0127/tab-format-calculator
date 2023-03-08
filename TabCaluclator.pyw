import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Tab切り替え計算機")
app.geometry("300x150")
app.iconbitmap("AppIcon.ico")

notebook = ttk.Notebook(app)

plus = ttk.Frame(notebook)
minus = ttk.Frame(notebook)
multiply = ttk.Frame(notebook)
divisive = ttk.Frame(notebook)

notebook.add(plus, text="足し算")
notebook.add(minus, text="引き算")
notebook.add(multiply, text="かけ算")
notebook.add(divisive, text="わり算")
notebook.pack()

#足し算-------------------------------------------------------------

def Caluclator_plus():
    value1 = int(write1.get())
    value2 = int(write2.get())
    answer = value1 + value2
    answer_plus.delete(0, tk.END)
    answer_plus.insert(0, answer)

submit1 = ttk.Button(plus, text="計算", command=Caluclator_plus)
write1 = ttk.Entry(plus)
write2 = ttk.Entry(plus)
plus_Label = ttk.Label(plus, text="+")
answer_plus = ttk.Entry(plus)

write1.pack()
plus_Label.pack()
write2.pack()
submit1.pack()
answer_plus.pack()

#-------------------------------------------------------------------
#引き算-------------------------------------------------------------

def Caluclator_minus():
    value1 = int(write3.get())
    value2 = int(write4.get())
    answer = value1 - value2
    answer_minus.delete(0, tk.END)
    answer_minus.insert(0, answer)

submit2 = ttk.Button(minus, text="計算", command=Caluclator_minus)
write3 = ttk.Entry(minus)
write4 = ttk.Entry(minus)
minus_Label = ttk.Label(minus, text="-")
answer_minus = ttk.Entry(minus)

write3.pack()
minus_Label.pack()
write4.pack()
submit2.pack()
answer_minus.pack()

#--------------------------------------------------------------------
#かけ算--------------------------------------------------------------

def Caluclator_multiply():
    value1 = int(write5.get())
    value2 = int(write6.get())
    answer = value1 * value2
    answer_multiply.delete(0, tk.END)
    answer_multiply.insert(0, answer)

submit3 = ttk.Button(multiply, text="計算", command=Caluclator_multiply)
write5 = ttk.Entry(multiply)
write6 = ttk.Entry(multiply)
multiply_Label = ttk.Label(multiply, text="×")
answer_multiply = ttk.Entry(multiply)

write5.pack()
multiply_Label.pack()
write6.pack()
submit3.pack()
answer_multiply.pack()

#---------------------------------------------------------------------
#わり算---------------------------------------------------------------

def Caluclator_divisive():
    value1 = int(write7.get())
    value2 = int(write8.get())
    answer = value1 / value2
    answer_divisive.delete(0, tk.END)
    answer_divisive.insert(0, answer)

submit4 = ttk.Button(divisive, text="計算", command=Caluclator_divisive)
write7 = ttk.Entry(divisive)
write8 = ttk.Entry(divisive)
divisive_Label = ttk.Label(divisive, text="÷")
answer_divisive = ttk.Entry(divisive)

write7.pack()
divisive_Label.pack()
write8.pack()
submit4.pack()
answer_divisive.pack()

#---------------------------------------------------------------------


app.mainloop()