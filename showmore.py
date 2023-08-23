import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import pandas as pd
import os
from datalayer import Connect_to_database
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
from components import movie
import numpy as np
from MovieInfo import MovieInfo

class ShowMore:
    def __init__(self,puserno):
        self.SM=tk.Toplevel()

        self.SM.resizable(width=0, height=0)
        FormWidth = 740
        FormHeight = 490
        ScreenWidth = self.SM.winfo_screenwidth()
        ScreenHeight = self.SM.winfo_screenheight()
        x = (ScreenWidth/2) - (FormWidth/2)  
        y = (ScreenHeight/2) - (FormHeight/2) -35  
        self.SM.geometry("%dx%d+%d+%d" % (FormWidth, FormHeight, x,y))
        self.SM.title("Movies")
        self.LoggedUserNo=puserno
        
        self.main_frame1=Frame(self.SM)
        self.main_frame1.pack(fill=BOTH, expand=1 )
        
        self.my_canvas1=Canvas(self.main_frame1)
        self.my_canvas1.pack(side=LEFT, fill=BOTH, expand=1)
        
        self.my_scrollbar1=Scrollbar(self.main_frame1, orient=VERTICAL, command=self.my_canvas1.yview)
        self.my_scrollbar1.pack(side=RIGHT, fill=Y)
        
        self.my_canvas1.configure(yscrollcommand=self.my_scrollbar1.set)
        self.my_canvas1.bind('<Configure>', lambda e: self.my_canvas1.configure(scrollregion=self.my_canvas1.bbox('all')))
        
        self.SMframe=Frame(self.my_canvas1)#Second Frame
        self.my_canvas1.create_window((0,0), window=self.SMframe, anchor='nw')
        
        
        self.SM.grab_set()
    
    def showMoreTrendingMovies(self, trending_movies):
        r = 0
        col = 0
        counter=0
        
        for i in range(0, len(trending_movies)):
            movie_id= trending_movies.loc[i][0]
            trending_image= trending_movies.loc[i][3]            
            
            script_path = os.path.dirname(os.path.abspath(__file__))

            image_name = script_path+ "\\Images\\"+trending_image

            im = Image.open(image_name)

            out = im.resize((120,120))
            img= ImageTk.PhotoImage(out, self.SMframe)
            
            btn = tk.Button(self.SMframe, image=img,command = lambda movie_id=movie_id: self.movie_image_clicked(movie_id))
            btn.image=img
            btn.grid(row=r, column=col, padx=10, pady=10)
            
            counter+=1
            col+=1
            if counter==5:
                r+=1
                col=0
                counter=0
        

    def showRecommendedMovies(self, UserNo):
        
        objDAL = Connect_to_database()
        
        df_movies = objDAL.get_movies()

        df_watchedMovies = objDAL.get_watched_movies(UserNo)

        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df_movies['features'])
        cosine_sim = cosine_similarity(count_matrix)
        cosine_df = pd.DataFrame(cosine_sim, index = df_movies.MovieName, columns = df_movies.MovieName)
               
        df_movies.set_index("MovieName", inplace=True)

        num = random.randint(0, len(df_watchedMovies)-1)

        recommended_movies =  objDAL.recommend_movies(cosine_df, df_watchedMovies.loc[num][1])

        rec_movies = pd.DataFrame(recommended_movies)

        rec_movies['MovieName']= rec_movies.index
        rec_movies.index = np.arange(0, len(rec_movies))    



        r = 0
        col = 0
        counter=0
        
        for i in range(0, len(rec_movies)):
            movie_name=rec_movies.loc[i][1]
            movie_id = df_movies.loc[movie_name][0]
            image_name = df_movies.loc[movie_name][3]

            script_path = os.path.dirname(os.path.abspath(__file__))

            image_name = script_path+ "\\Images\\"+image_name

            im = Image.open(image_name)

            out = im.resize((120,120))
            img= ImageTk.PhotoImage(out, self.SMframe)
            
            btn = tk.Button(self.SMframe, image=img,command = lambda movie_id=movie_id: self.movie_image_clicked(movie_id))
            btn.image=img
            btn.grid(row=r, column=col, padx=10, pady=10)
            
            counter+=1
            col+=1
            if counter==5:
                r+=1
                col=0
                counter=0
    def movie_image_clicked(self, movie_id):
        obj = MovieInfo()
        obj.show_more_info(movie_id, self.LoggedUserNo)
        connect = Connect_to_database()
        connect.add_watched_movies(self.LoggedUserNo,movie_id.item())
        