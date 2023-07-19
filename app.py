
import streamlit as st
import pickle
import requests
import numpy as np

st.header("Movie Recommender")
movies = pickle.load(open("path to movies dataet\movies.pkl", "rb"))
similarity = pickle.load(open("path to the similarity matrix\similarity.pkl", "rb"))
titles = movies["title"].values

def poster(movieID):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=<your API key>&language=en-US'.format(movieID)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    final_poster_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return final_poster_path

##Use for bag of words and tfidf

# def recommend(movie_title):
#     movie_index = movies[movies.title == movie_title].index[0]
#     cosine_similarity = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda model:model[1])
#     recommendations = []
#     poster_movies = []
#     for i in cosine_similarity[1:6]:
#         movieID = movies.iloc[i[0]].id
#         recommendations.append(movies.iloc[i[0]].title)
#         poster_movies.append(poster(movieID))
#     return recommendations, poster_movies

## Use for SVDS
def recommend_movies_svds(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    movie_score = similarity[movie_index].reshape(1, -1)
    similar_indices = np.argsort(movie_score)[-1,-6:-1][::-1].tolist()
    recommended_movies = movies.loc[similar_indices, 'title'].values.tolist()
    movie_ids = []
    for i in similar_indices:
        movie_ids.append(movies.loc[i,"id"])
    poster_movies = []
    x = 0
    for i in movie_ids:
        poster_movies.append(poster(i))
    return recommended_movies, poster_movies

select_button = st.selectbox("Choose Movie", titles)

if st.button("Show"):
    movie_recommendations, movie_poster = recommend_movies_svds(select_button)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_recommendations[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_recommendations[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_recommendations[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_recommendations[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_recommendations[4])
        st.image(movie_poster[4])
