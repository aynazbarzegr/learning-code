import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("form vorod")
root.geometry("350x450")
userlbl = tk.Label(root,text="username")
userlbl.pack(pady=10,padx=15)
userent = tk.Entry(root)
userent.pack(pady=10,padx=15)
passlbl = tk.Label(root,text="password")
passent = tk.Entry(root)
passent.pack(pady=10,padx=15)
passlbl.pack(pady=10,padx=15)
def login():
    username = userent.get()
    password= passent.get()
    if username == "admin"    and password == "2234":
     userlbl.pack_forget()
     userent.pack_forget()
     passlbl.pack_forget()
     passent.pack_forget()
     
     messagebox.showinfo("ورود","نام عنوان")
    else:
        messagebox.showerror("eror,incurrect username or password")
        
logbtn = tk.Button(root,text="ورود",command=login)
logbtn.pack(pady=10,padx=15)
num1 = tk.Entry(root)
num1.pack()
tk.Label(root,text="عدد دوم را وارد کنید").pack()
num2 = tk.Entry(root)
num2.pack()
result_label = tk.Label(root,text="",fg="red")
result_label.pack()
def add():
    
      a = float(num1.get())
      b = float(num2.get())
      javab = a + b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(root,text ="+",command=add).pack(pady=10,padx=15)

def zarb():
      a = float(num1.get())
      b = float(num2.get())
      javab = a * b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(root,text ="*",command=zarb).pack(pady=10,padx=15)
def tagsim():
      a = float(num1.get())
      b = float(num2.get())
      javab = a / b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(root,text ="/",command=tagsim).pack(pady=10,padx=15)

def tafrig():
      a = float(num1.get())
      b = float(num2.get())
      javab = a - b
      result_label.config(text=f"نتیجه برابر است با{str (javab)}")
      
tk.Button(root,text ="-",command=tafrig).pack(pady=10,padx=15)

root.mainloop()

