import tkinter as tk
from tkinter.ttk import Combobox
from components import user
from datalayer import Connect_to_database
        
class Registration:
    def __init__ (self):
    
        self.root = tk.Toplevel()
        self.root.resizable(width = 0, height = 0)
        FormWidth = 400
        FormHeigth = 350
        ScreenWidth = self.root.winfo_screenwidth()
        ScreenHeigth = self.root.winfo_screenheight()
        x = (ScreenWidth/2)-(FormWidth/2)
        y = (ScreenHeigth/2)-(FormHeigth/2)-35
    
        self.root.title("Registration")
        self.root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))
    
        self.nm = tk.StringVar()
        self.uid = tk.StringVar()
        self.pwd = tk.StringVar()
        self.cpwd = tk.StringVar()
        self.sq = tk.StringVar()
        self.an = tk.StringVar()
    
        self.lbl1 = tk.Label(self.root,text = "Name")
        self.lbl1.place(x = 30, y = 60)
    
        self.ent1 = tk.Entry(self.root,textvariable = self.nm)
        self.ent1.place(x = 180 , y = 60)
    
        self.lbl2 = tk.Label(self.root,text = "UserId")
        self.lbl2.place(x = 30 , y = 90)
    
        self.ent2 = tk.Entry(self.root, textvariable = self.uid)
        self.ent2.place(x = 180, y = 90)
        
        self.lbl3 = tk.Label(self.root, text = "Password")
        self.lbl3.place(x = 30, y = 120)
    
        self.ent3 = tk.Entry(self.root,textvariable = self.pwd,show="*")
        self.ent3.place(x = 180, y = 120)
    
        self.lbl4 = tk.Label(self.root, text = "Confirm Password")
        self.lbl4.place(x = 30, y = 150)
        
        self.ent4 = tk.Entry(self.root, textvariable = self.cpwd,show="*")
        self.ent4.place(x = 180, y = 150)
        
        self.lbl5 = tk.Label(self.root, text = "Security Question")
        self.lbl5.place(x = 30, y = 180)
    
        self.cmb1 = Combobox(self.root, width = 27, textvariable = self.sq)
        self.cmb1['values']=('Favourite colour ?','Fathers Name ?','10th School Name ?')
        self.cmb1.place(x = 180, y = 180)
    
        self.lbl6 = tk.Label(self.root, text = "Answer")
        self.lbl6.place(x = 30, y = 210)
    
        self.ent6 = tk.Entry(self.root, textvariable = self.an)
        self.ent6.place(x = 180, y = 210)
        
        self.btn1 = tk.Button(self.root, text = "Register",command = self.register)
        self.btn1.place(x = 180, y = 260)
        
        self.root.grab_set()
        self.root.wait_window()
        
    def register(self):
        if self.cpwd.get()==self.pwd.get():
            ad = Connect_to_database()
            u = user()
            u.Name = self.nm.get()
            u.UserId = self.uid.get()
            u.Password=self.pwd.get()
            u.SecurityQ = self.cmb1.current()
            u.Answer = self.an.get()
            check ,msg = ad.validatefields(u)
            if check ==True:
                check2,msg2 = ad.validateId(u)
                if check2 == True:
                    u.SecurityQ = self.sq.get()
                    ad.add_users(u)
                    self.nm.set("")
                    self.uid.set("")
                    self.pwd.set("")
                    self.cpwd.set("")
                    self.sq.set("")
                    self.an.set("")
                    tk.messagebox.showinfo("GoFlix","Registered successfully..")
                else:
                   tk.messagebox.showerror("GoFlix",msg2)
            else:
               tk.messagebox.showerror("GoFlix",msg)
               
           
        else:
           self.pwd.set("")
           self.cpwd.set("")
           tk.messagebox.showerror("GoFlix","Password not matching!!")
    


