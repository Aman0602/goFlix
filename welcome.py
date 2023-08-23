import tkinter as tk
from tkinter import *
from components import movie
from datalayer import Connect_to_database
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from PIL import ImageTk,Image
from tkinter.ttk import Scrollbar
import os
import random
from MovieInfo import MovieInfo
from showmore import ShowMore

class welcome_page:
    def __init__(self, pUserNo, pName):
        self.root = tk.Toplevel()
        self.root.resizable(width=0,height = 0)
        FormWidth = 730
        FormHeigth = 700
        ScreenWidth = self.root.winfo_screenwidth()
        ScreenHeigth = self.root.winfo_screenheight()
        x = (ScreenWidth/2)-(FormWidth/2)
        y = (ScreenHeigth/2)-(FormHeigth/2)-35
        
        self.root.title("GoFlix")
        self.root.geometry("%dx%d+%d+%d" % (FormWidth, FormHeigth,x,y))
        
        self.LoggedUserNo = pUserNo
        
        connect = Connect_to_database()
        
        watched_movies=connect.get_watched_movies(pUserNo)
        
        AllMovies = connect.get_movies()
        
        cv = CountVectorizer()

        count_matrix = cv.fit_transform(AllMovies['features'])

        cosine_sim = cosine_similarity(count_matrix)

        cosine_df = pd.DataFrame(cosine_sim,index = AllMovies.MovieName,columns=AllMovies.MovieName)
        
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        AllMovies.set_index("MovieName",inplace =True)
        
        label_name= tk.Label(self.root,text= "Welcome back  "+pName,font=('Poor Richard',25,'bold'))
        label_name.place(x =10, y = 10)
        label_name.config(fg="black")

        label_recommendations = tk.Label(self.root,text = "Movies that you might like...",font=('Gabriola',20,'bold'))
        label_recommendations.grid(row=0,column=0,padx=10,pady=50,columnspan=5)
    
        label_recommendations.config(fg="red")
        
        i=1
        
        random_numbers = []
        
        for k in range(0,2):
            
            while True:
                num = random.randint(0, len(watched_movies)-1)
                if num in random_numbers:
                    continue
                else:
                    random_numbers.append(num)
                    break
            
            
            
            
            recommended = connect.recommend_movies(cosine_df,watched_movies.loc[num][1])
            
            rec_movies= pd.DataFrame(recommended)
            rec_movies['MoviesName']= rec_movies.index
            rec_movies.index= np.arange(0,len(rec_movies))

            self.Show_Movies(rec_movies, AllMovies, i, 0)            
        
            
            i+=1
            
        label_trending = tk.Label(self.root,text = "watched movies",font=('Gabriola',20,'bold'))
        label_trending.grid(row=3,column=0,padx=10,pady=20,columnspan=5)
        
        label_trending.config(fg="red")
            
        trending_movies = connect.get_trending_movies()
            
        counter = 0
            
        for i in range(0,len(trending_movies)):
            movie_id = trending_movies.loc[i][0]
            trending_image=trending_movies.loc[i][3]
                
            image_name = self.script_path+"\\Images\\"+trending_image
            im = Image.open(image_name)
                
            out= im.resize((120,120))
            img = ImageTk.PhotoImage(out,self.root)
            
            self.btn = tk.Button(self.root,image = img, command = lambda movie_id=movie_id: self.movie_image_clicked(movie_id))
            self.btn.image = img
            self.btn.grid(row=4,column=i,padx=10,pady=10)
            counter+=1
                
            if counter ==5:
                break
            
            
        self.btn1 = tk.Button(self.root,text = "Show More",command = self.showmorecomendedmovies)
        self.btn1.place(x = 630, y = 360)
        
        self.btn1 = tk.Button(self.root,text = "Show More",command = self.showmoretrendingmovies)
        self.btn1.place(x = 630, y = 580)
                
            
        self.root.grab_set()

    def Show_Movies(self, rec_movies, AllMovies,  Row, Column):
        for i in range(0,5):
            movie_name = rec_movies.loc[i][1]
            
            image_name = AllMovies.loc[movie_name][3]
            image_name = self.script_path+"\\Images\\"+image_name
            movie_id = AllMovies.loc[movie_name][0]
            im = Image.open(image_name)
            
            out= im.resize((120,120))
            img = ImageTk.PhotoImage(out,self.root)
        
            self.btn = tk.Button(self.root,image = img, command = lambda movie_id=movie_id: self.movie_image_clicked(movie_id))
            self.btn.image = img
            self.btn.grid(row=Row,column=Column,padx=10,pady=10)
            Column+=1
            
    def movie_image_clicked(self, movie_id):
        obj = MovieInfo()
        obj.show_more_info(movie_id, self.LoggedUserNo)
        connect = Connect_to_database()
        connect.add_watched_movies(self.LoggedUserNo,movie_id.item())
        
    def showmoretrendingmovies(self):
        connect = Connect_to_database()
        trending_movies = connect.get_trending_movies()
        obj = ShowMore(self.LoggedUserNo)
        obj.showMoreTrendingMovies(trending_movies)
        
    def showmorecomendedmovies(self):
        obj = ShowMore(self.LoggedUserNo)
        obj.showRecommendedMovies(self.LoggedUserNo)
        

