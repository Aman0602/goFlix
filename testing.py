import tkinter as tk
from tkinter import * 
from tkinter.ttk import Scrollbar
from datalayer import Connect_to_database
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from PIL import ImageTk,Image


root = tk.Tk()

root.resizable(width = 0, height = 0)
FormWidth = 1000
FormHeigth = 400
ScreenWidth = root.winfo_screenwidth()
ScreenHeigth = root.winfo_screenheight()
x = (ScreenWidth/2)-(FormWidth/2)
y = (ScreenHeigth/2)-(FormHeigth/2)-35

root.title("Welcome page")
root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))


# main_frame=Frame(self.root)
# main_frame.pack(fill=BOTH,expand=1)

# my_canvas = Canvas(main_frame)
# my_canvas.pack(side=LEFT, fill=BOTH,expand=1)

# my_scrollbar = ttk.Scrollbar(main_frame,orient = VERTICAL,command = my_canvas.yview)
# my_scrollbar.pack(side=RIGHT,fill=Y)

# my_canvas.configure(yscrollcommand = my_scrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

# second_frame = Frame(my_canvas)
# my_canvas.create_window((0,0),window=second_frame,anchor="nw")


connect=Connect_to_database()
records = connect.get_movies()

cv = CountVectorizer()

count_matrix = cv.fit_transform(records['features'])

cosine_sim = cosine_similarity(count_matrix)

cosine_df = pd.DataFrame(cosine_sim,index = records.MovieName,columns=records.MovieName)

recommended = connect.recommend_movies(cosine_df,records.loc[0][1])

rec_movies= pd.DataFrame(recommended)
rec_movies['MoviesName']= rec_movies.index
rec_movies.index= np.arange(0,len(rec_movies))
print(rec_movies)

records.index=records['MovieName']
# print(records)

# frame = tk.Frame(root)
# frame.pack()



for i in range(5):
        imagename = Image.open('Images\\'+ records.loc[rec_movies.loc[i][1]][4])
        img2=imagename.resize((100,100))
        newimg= ImageTk.PhotoImage(img2)
        lbl1 = tk.Label(root, image = newimg)
        lbl1.grid(row = 0, column = i, padx = 20, pady = 20)
        print('Images\\'+ records.loc[rec_movies.loc[i][1]][4])
        
    

root.mainloop()


