import tkinter as tk
from tkinter import *
from register_form import Registration
from Login_form import login_form
from welcome import welcome_page
from AboutUs import AboutDeveloper
from PIL import ImageTk,Image

class form:
    def __init__(self):

        self.root = tk.Tk()
        self.root.resizable(width = 0, height = 0)
        FormWidth = 370
        FormHeigth = 370
        ScreenWidth = self.root.winfo_screenwidth()
        ScreenHeigth = self.root.winfo_screenheight()
        x = (ScreenWidth/2)-(FormWidth/2)
        y = (ScreenHeigth/2)-(FormHeigth/2)-35

        self.root.title("GoFlix")
        self.root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))
        
        
        
        im1 = Image.open(r"C:\Users\Admin\Desktop\project\register.png")
        
        out1= im1.resize((80,80))
        img1 = ImageTk.PhotoImage(out1,self.root)

        self.btn1 = tk.Button(self.root,image = img1 ,command = self.signup)
        self.btn1.place(x = 30, y = 50)
        
        self.lbl1= tk.Label(self.root,text = "Register")
        self.lbl1.place(x = 50,y = 140)
        
        im2 = Image.open(r"C:\Users\Admin\Desktop\project\login.png")
        
        out2= im2.resize((80,80))
        img2 = ImageTk.PhotoImage(out2,self.root)

        self.btn2 = tk.Button(self.root,image = img2, command = self.login)
        self.btn2.place(x = 200, y = 50)
        
        self.lbl2= tk.Label(self.root,text = "Login")
        self.lbl2.place(x = 220,y = 140)
        
        im3 = Image.open(r"C:\Users\Admin\Desktop\project\aboutus.png")
        
        out3= im3.resize((80,80))
        img3 = ImageTk.PhotoImage(out3,self.root)

        self.btn3 = tk.Button(self.root,image = img3, command = self.aboutus)
        self.btn3.place(x = 30, y = 200)
        
        self.lbl1= tk.Label(self.root,text = "About Us")
        self.lbl1.place(x = 50,y = 290)
        
        im4 = Image.open(r"C:\Users\Admin\Desktop\project\exit.png")
        
        out4= im4.resize((80,80))
        img4 = ImageTk.PhotoImage(out4,self.root)

        self.btn5 = tk.Button(self.root,image = img4, command = self.root.destroy)
        self.btn5.place(x = 200, y = 200)
        
        self.lbl1= tk.Label(self.root,text = "Exit")
        self.lbl1.place(x = 230,y = 290)

        self.root.mainloop()
        
    def signup(self):
        
        obj=Registration()
        
    def login(self):
        
        obj=login_form()
        
        res = obj.start_login_form()
        
        if res!=None:
            wel = welcome_page(res.UserNo, res.Name)
        
    def aboutus(self):
        obj = AboutDeveloper()
    
        
        
obj = form()