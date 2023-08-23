import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

class AboutDeveloper:
    def __init__(self):
        self.root = tk.Toplevel()
        
        self.root.title("GoFlix")
        self.root.resizable(width = 0, height = 0)
        FormWidth = 400
        FormHeigth = 350
        ScreenWidth = self.root.winfo_screenwidth()
        ScreenHeigth = self.root.winfo_screenheight()
        x = (ScreenWidth/2)-(FormWidth/2)
        y = (ScreenHeigth/2)-(FormHeigth/2)-35
    
        self.root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))
        
        
        self.lbl1 = tk.Label(self.root,text = "Developer's Name : ")
        self.lbl1.place(x = 30, y = 30)
        
        self.lbl2 = tk.Label(self.root,text = "AMANDEEP KAUR SAINI")
        self.lbl2.place(x = 150, y = 30)
        
        self.lbl3 = tk.Label(self.root,text = "Application Name : ")
        self.lbl3.place(x = 30, y = 60)
        
        self.lbl4 = tk.Label(self.root,text = "GoFlix")
        self.lbl4.place(x = 150, y = 60)
        
        # self.lbl5 = tk.Label(self.root,text = "" )
        # self.lbl5.place(x = 30, y = 30)
        
        self.root.grab_set()