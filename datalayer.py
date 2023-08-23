import pyodbc
from components import movie
import pandas as pd
import numpy as np
from components import user

class Connect_to_database:
    def __init__(self):
        self.con = pyodbc.connect("driver={sql server};server=LAPTOP-SJN0V5QS\SA;database=Project_DB;uid=sa;pwd=amandeep")
        
    def __del__(self):
        self.con.close()
        self.con=None
        
         
         
    def add_users(self,us):
        query ="Insert into Users values(?,?,?,?,?)"
        try:
            tup = (us.Name,us.UserId,us.Password,us.SecurityQ,us.Answer)
            cur = self.con.cursor()
            cur.execute(query,tup)
            self.con.commit()
        except:
            self.con.Rollback()
            
    def validateId(self,us):
        msg = ""
        flag = True
        cur = self.con.cursor()
        query1 = "Select UserId from Users where UserId = (?)"
        tup1 = (us.UserId)
        cur.execute(query1,tup1)
        check1 = cur.fetchall()
        for x in check1:
            if x[0]== us.UserId:
                flag = False
                msg = "UserId "+ us.UserId+" already exists!!"
        return flag, msg
    def validatefields(self,us):
        flag = True
        msg = ""
        if len(us.Name)==0:
            msg = "Name is empty!\n"
            flag = False
        if len(us.UserId)==0:
            msg = msg + "UserId is empty!\n"
            flag = False
        if len(us.Password)==0:
            msg = msg + "Password is empty!\n"
            flag = False
        if us.SecurityQ ==-1:
            msg = msg + "Security Question is empty!\n"
            flag = False
        if len(us.Answer)==0:
            msg = msg + "Answer is empty!\n"
            flag = False
        if len(us.Password)<8:
            msg = msg + "Length of password is short!"
            flag = False
        return flag,msg
    
    
    def Authenticate(self,uid,pwd):
        
        ret = None
        
        query ="select * from Users where UserId=? and Upassword=?"
        cur = self.con.cursor()
        tup = (uid,pwd)
        cur.execute(query,tup)
        records= cur.fetchall()
        
        if len(records)>0:
            ret = user()
            ret.UserNo = records[0][0]
            ret.Name = records[0][1]
            
            
            
        return ret
    
    
    def get_movies(self):
        
        df_movies = pd.read_sql("Select M.MovieId,M.MovieName,M.Genre,D.DirectorName,M.ImageName from Movies as M, Directors as D where M.DirectorId = D.DirectorId",self.con)
        df_starcast = pd.read_sql("select M.MovieId, A.ActorName AS actors from Movies as M,Actors as A ,Casts as C  where M.MovieId = C.MovieId and C.ActorsId=A.ActorsId ",self.con)
        
        df_starcast["StarCast"] = df_starcast.groupby(["MovieId"])['actors'].transform(lambda a: ' '.join(a))
        df_starcast.drop_duplicates(subset="MovieId",keep='first',inplace=True)
        
        df_starcast=df_starcast.drop(['MovieId','actors'],axis=1)
        df_starcast.index=np.arange(0,len(df_starcast))
        df_movies=df_movies.join(df_starcast)
        df_movies['features'] = df_movies['MovieName']+' '+df_movies['Genre']+' '+df_movies['DirectorName']+' '+df_movies['StarCast']
    
        return df_movies 
    
    
    def get_movie_info(self, movie_id):
        df_movies = pd.read_sql("Select M.MovieId,M.MovieName,M.Genre,D.DirectorName,M.ImageName from Movies as M, Directors as D where M.DirectorId = D.DirectorId and M.MovieId="+str(movie_id),self.con)
        df_starcast = pd.read_sql("select M.MovieId, A.ActorName AS actors from Movies as M,Actors as A ,Casts as C  where M.MovieId = C.MovieId and C.ActorsId=A.ActorsId and M.MovieId="+str(movie_id),self.con)
        
        df_starcast["StarCast"] = df_starcast.groupby(["MovieId"])['actors'].transform(lambda a: ' , '.join(a))
        
        df_starcast.drop_duplicates(subset="MovieId",keep='first',inplace=True)
        
        df_starcast=df_starcast.drop(['MovieId','actors'],axis=1)
        
        df_starcast.index=np.arange(0,len(df_starcast))
        df_movies=df_movies.join(df_starcast) 
        
        return df_movies
    
    def recommend_movies(self,cosine_df,MovieName):
        # print(MovieName)
        return cosine_df[MovieName].sort_values(ascending = False)[:]
    
    def get_watched_movies(self,userno):
        query = "select W.MovieID,M.MovieName from WatchedMovies as W,Movies as M where UserNo = "+str(userno)+" and W.MovieId=M.MovieId"
        
        watched = pd.read_sql(query,self.con)
        return watched
    
    def add_rating(self,rating,movieid,userno):
        cur = self.con.cursor()
        tup = (userno,movieid.item())
        cur.execute("select * from Rating where UserNo =? and MovieId = ?",tup)
        rated_movies = cur.fetchall()
        if len(rated_movies)==0:
            tup = (rating,movieid.item(),userno)
            cur = self.con.cursor()
            cur.execute("insert into Rating values(?,?,?)",tup)
            self.con.commit()
            
        
    def add_watched_movies(self,userno,movie_id):
        cur = self.con.cursor()
        tup = (userno,movie_id)
        cur.execute("select * from WatchedMovies where UserNo =? and MovieId = ?",tup)
        watched_movies = cur.fetchall()
        if len(watched_movies)==0:
            cur.execute("insert into WatchedMovies values(?,?)",tup)
            self.con.commit()
            
            
    def get_trending_movies(self):
        trending_movies = pd.read_sql("select R.MovieId,Avg(R.Rating) as [Rating], (select MovieName from Movies where MovieId=R.MovieId) as [MovieName],(select ImageName from Movies where MovieId = R.MovieId) as [ImageName] from Rating as [R] group by R.MovieId order by AVG(R.Rating) Desc",self.con)[:]
        return trending_movies  

# obj = Connect_to_database()

        

                
    
        
        

    
        
        
        
   
        