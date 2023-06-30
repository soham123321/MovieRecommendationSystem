import streamlit as st
import pickle
import requests

st.header("Movie Recommender")
movies = pickle.load(open("<directorypath>\movies.pkl", "rb"))
similarity = pickle.load(open("<directorypath>\similarity.pkl", "rb"))
titles = movies["title"].values

def poster(movieID):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=<yourapikey>&language=en-US".format(movieID)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    final_poster_path = "https://image.tmdb.org/t/p/w500/"+ poster_path
    return final_poster_path
def recommend(movie_title):
    movie_index = movies[movies.title == movie_title].index[0]
    cosine_similarity = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda model:model[1])
    recommendations = []
    poster_movies = []
    for i in cosine_similarity[1:6]:
        movieID = movies.iloc[i[0]].id
        recommendations.append(movies.iloc[i[0]].title)
        poster_movies.append(poster(movieID))
    return recommendations, poster_movies

select_button = st.selectbox("Choose Movie", titles)

if st.button("Show"):
    movie_recommendations, movie_poster = recommend(select_button)
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
