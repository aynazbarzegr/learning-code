import tkinter as tk
win = tk.Tk()
win.title("ماشین حساب ساده")
win.geometry("350x450")
tk.Label(win,text="عدد اول را وارد کنید").pack()
num1 = tk.Entry(win)
num1.pack()
tk.Label(win,text="عدد دوم را وارد کنید").pack()
num2 = tk.Entry(win)
num2.pack()
result_label = tk.Label(win,text="",fg="red")
result_label.pack()
def add():
      a = float(num1.get())
      b = float(num2.get())
      javab = a + b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(win,text ="+",command=add).pack()

def zarb():
      a = float(num1.get())
      b = float(num2.get())
      javab = a * b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(win,text ="*",command=zarb).pack()
def tagsim():
      a = float(num1.get())
      b = float(num2.get())
      javab = a / b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(win,text ="/",command=zarb).pack()

def tafrig():
      a = float(num1.get())
      b = float(num2.get())
      javab = a - b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(win,text ="-",command=zarb).pack()

win.mainloop()      
    
   

    
     