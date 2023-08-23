import tkinter as tk
from tkinter import *
from datalayer import Connect_to_database
from PIL import ImageTk,Image
import os


def open_tab(x):
    
    tk.messagebox.showinfo("clickable label","image name is: "+x)

root = tk.Tk()


root.title("Clickable Images")
root.geometry("900x400")
connect = Connect_to_database()
records = connect.get_movies()
script_path = os.path.dirname(os.path.abspath(__file__))
for i in range(5):
    image_name = records.loc[i][4]
    image_name = script_path+"\\Images\\"+image_name
    
    im = Image.open(image_name)

    out= im.resize((120,120))
    img = ImageTk.PhotoImage(out,root)

    lbl = tk.Label(root,image = img)
    lbl.image = img
    lbl.grid(row=0,column=i,padx=10,pady=10)
    x = records.loc[i][4]
    lbl.bind("<Button-1>", lambda e:open_tab(x))


root.mainloop()