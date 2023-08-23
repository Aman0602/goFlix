import tkinter as tk
from datalayer import Connect_to_database
from register_form import Registration
from welcome import welcome_page


    
class login_form:
    def __init__(self):
        self.root = tk.Toplevel()
        
        self.response = None
        
        self.root.resizable(width = 0, height = 0)
        FormWidth = 400
        FormHeigth = 300
        ScreenWidth = self.root.winfo_screenwidth()
        ScreenHeigth = self.root.winfo_screenheight()
        x = (ScreenWidth/2)-(FormWidth/2)
        y = (ScreenHeigth/2)-(FormHeigth/2)-35

        self.root.title("GoFlix Login Form")
        self.root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))

        self.uid = tk.StringVar()
        self.pwd = tk.StringVar()


        self.lbl1 = tk.Label(self.root,text = "UserId")
        self.lbl1.place(x= 90, y = 80)

        self.ent1 = tk.Entry(self.root,textvariable = self.uid)
        self.ent1.place(x = 180, y = 80)

        self.lbl2 = tk.Label(self.root,text = "Password")
        self.lbl2.place(x= 90, y = 110)

        self.ent2 = tk.Entry(self.root,textvariable = self.pwd,show="*")
        self.ent2.place(x = 180, y = 110)

        self.btn1 = tk.Button(self.root,text = "LogIn", command=self.login_clicked)
        self.btn1.place(x = 180, y = 140)

        

    def start_login_form(self):
        self.root.grab_set()
        self.root.wait_window()
        return self.response


    def login_clicked(self):
        ad = Connect_to_database()
        userid = self.uid.get()
        password = self.pwd.get()

        obj = ad.Authenticate(userid,password)
        if obj == None:
            self.pwd.set("")
            self.uid.set("")
            tk.messagebox.showinfo("GoFlix","User Id or Password incorrect!")
            
        else:
            self.response = obj
            self.root.destroy()
        