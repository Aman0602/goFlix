import pyodbc
import tkinter as tk

def register():
    if cpwd.get() == pwd.get():
        try:
            con  = pyodbc.connect("driver={sql server};server=LAPTOP-SJN0V5QS\SA;database=Project_DB;uid=sa;pwd=amandeep")
            cur = con.cursor()
            tup = (nm.get(),uid.get(),pwd.get())
            print(tup)
            cur.execute("Insert into Registration values(?,?,?)",tup)
            con.commit()
            tk.messagebox.showinfo("Registration Successful","Registered..")
        except:
            con.rollback()
            print("rollbacked")
        finally:
            con.close()
    else:
        tk.messagebox.showerror("Registration Failed","Password not Matching!!")

root = tk.Toplevel()

root.title("Registration")
root.geometry("400x350")

nm = tk.StringVar()
uid = tk.StringVar()
pwd = tk.StringVar()
cpwd = tk.StringVar()

lbl1 = tk.Label(root,text = "Name")
lbl1.place(x = 30, y = 60)

ent1 = tk.Entry(root,textvariable = nm)
ent1.place(x = 180 , y = 60)

lbl2 = tk.Label(root,text = "UserId")
lbl2.place(x = 30 , y = 90)

ent2 = tk.Entry(root, textvariable = uid)
ent2.place(x = 180, y = 90)

lbl3 = tk.Label(root, text = "Password")
lbl3.place(x = 30, y = 120)

ent3 = tk.Entry(root,textvariable = pwd)
ent3.place(x = 180, y = 120)

lbl4 = tk.Label(root, text = "Confirm Password")
lbl4.place(x = 30, y = 150)

ent4 = tk.Entry(root, textvariable = cpwd)
ent4.place(x = 180, y = 150)

btn1 = tk.Button(root, text = "Register",command = register)
btn1.place(x = 180, y = 200)

self.root.grab_set()
        self.root.wait_window()