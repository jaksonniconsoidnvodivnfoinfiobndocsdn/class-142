import numpy as np
import pandas as pd
df = pd.read_csv("final.csv")
c = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)
q_movies = df.copy().loc[df['vote_count']>= m]
def weighted_rating(x,l = m,c = c):
    v = x['vote_count']
    r = x['vote_average']
    return(v/(v+m)*r)+(m/(m+v)*c)

q_movies['score'] = q_movies.apply(weighted_rating,axis = 1)
q_movies = q_movies.sort_values('score',ascending= False)
output = q_movies[['title','vote_count','vote_average','poster_link']].head(20).values.tolist()