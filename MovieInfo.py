import tkinter as tk
from datalayer import Connect_to_database
from PIL import ImageTk,Image
import os

class MovieInfo:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.resizable(width=0,height = 0)
        FormWidth = 500
        FormHeigth = 350
        ScreenWidth = self.root.winfo_screenwidth()
        ScreenHeigth = self.root.winfo_screenheight()
        x = (ScreenWidth/2)-(FormWidth/2)
        y = (ScreenHeigth/2)-(FormHeigth/2)-35
        
        self.root.title("GoFlix")
        self.root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))
        
        self.lbl1 = tk.Label(self.root , text = "Movie :")
        self.lbl1.place(x= 30,y = 30)
        
        self.lbl2 = tk.Label(self.root,text = "--")
        self.lbl2.place(x = 90, y = 30)
        
        self.lbl3 = tk.Label(self.root , text = "Director :")
        self.lbl3.place(x= 30,y = 60)
        
        self.lbl4 = tk.Label(self.root,text = "--")
        self.lbl4.place(x = 90, y = 60)
        
        self.lbl5 = tk.Label(self.root , text = "Star Cast :")
        self.lbl5.place(x= 30,y = 90)
        
        self.lbl6 = tk.Label(self.root,text = "--")
        self.lbl6.place(x = 90, y = 90)
        
        self.lbl7 = tk.Label(self.root , text = "Genre :")
        self.lbl7.place(x= 240,y = 30)
        
        self.lbl8 = tk.Label(self.root,text = "--")
        self.lbl8.place(x = 300, y = 30)
        
        
        
        self.scale1 = tk.Scale(self.root,from_=1,to=5,orient = tk.HORIZONTAL)
        self.scale1.place(x = 240,y = 130)
        
        self.btn2 = tk.Button(self.root,text = "Rate",command = self.rate_clicked)
        self.btn2.place(x = 380, y = 145)
        
        
    def show_more_info(self,movieid, pUserNo):
        objDAL = Connect_to_database()
        df = objDAL.get_movie_info(movieid)
        
        self.MovieId = movieid
        self.LoggedUserNo = pUserNo
        
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        
        image_name = df.loc[0][4]
        image_name = self.script_path+"\\Images\\"+image_name
        im = Image.open(image_name)
        
        out= im.resize((170,190))
        img = ImageTk.PhotoImage(out,self.root)
        
        self.lbl9 = tk.Label(self.root, image=img)
        self.lbl9.image=img
        self.lbl9.place(x = 30, y = 120)
        
        
        self.lbl2.config(text=df.loc[0][1]  )
        self.lbl4.config(text=df.loc[0][3]  )
        self.lbl6.config(text=df.loc[0][5]  )
        self.lbl8.config(text=df.loc[0][2]  )

        
        self.root.grab_set()  
    def rate_clicked(self):
        obj = Connect_to_database()
        
        rating = self.scale1.get()
        
        obj.add_rating(rating, self.MovieId, self.LoggedUserNo)
        
