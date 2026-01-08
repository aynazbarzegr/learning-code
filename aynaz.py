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
        messagebox.showinfo("عنوان","نام عنوان")
    else:
        messagebox.showerror("eror,incurrect username or password")
        
logbtn = tk.Button(root,text="عنوان",command=login)
logbtn.pack(pady=10,padx=15)
root.mainloop()

