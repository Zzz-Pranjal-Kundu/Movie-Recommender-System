import streamlit as st
import pickle
import pandas as pd
import requests # to hit APIs


#Modify the background
background = """
              <style>
                [data-testid="stAppViewContainer"] {
                    background-color: #e3ad23;
                    opacity: 0.8;
                    background-image: repeating-radial-gradient(circle at 0 0, transparent 0, #e3ad23 28px),
                                      repeating-linear-gradient(#ff1f0055, #ff1f00);
                }
                [data-testid="stExpander"]{
                    background-color: #34495e;
                }
                [data-testid="stHeadingWithActionElements"]{
                    background-color: #22313f;
                    border-radius: 15px;
                    text-align: center;
                    font-style: italic;
                }
                .st-emotion-cache-13k62yr {
                    background: rgb(14, 17, 23);
                    color: white;
                }
                .st-emotion-cache-nok2kl {
                    color: white;
                }
             </style>
             """
st.markdown(background,unsafe_allow_html=True)


movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

st.title("MOVIE RECOMMENDER SYSTEM")
st.write("")
selected_movie_name = st.selectbox( "Select a movie: ", movies['title'].values )


#Takes a movie name as an input and returns 5 similar movie names
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_idx]
    mapping = list(enumerate(distances))  # mapping each movie score to its respective index
    entire_movie_list = sorted(mapping, reverse=True, key=lambda x: x[1])  # key=... to sort acc to the movie similarity rather than
    movies_list = entire_movie_list[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching movie poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


def fetch_movie_details(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data = response.json()
    details = {
        'title': data['title'],
        'overview': data['overview'],
        'release_date': data['release_date'],
        'rating': data['vote_average'],
        'genres': ', '.join([genre['name'] for genre in data['genres']])
    }
    return details

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i, col in enumerate(columns):
        with col:
            st.image(posters[i])
            st.markdown(f"<h4 style='text-align: center; font-weight: bold;'>{names[i]}</h4>",
                        unsafe_allow_html=True)  # Bold and slightly larger text
            movie_id = movies[movies['title'] == names[i]].iloc[0].movie_id
            movie_details = fetch_movie_details(movie_id)

            # Add an expander for movie details
            # Place the expander in a wider column
            with st.expander("Show Details",expanded=False):
                # Adjust the width of the expander content
                with st.container():
                    st.write(f"**Title:** {movie_details['title']}")
                    st.write(f"**Overview:** {movie_details['overview']}")
                    st.write(f"**Release Date:** {movie_details['release_date']}")
                    st.write(f"**Rating:** {movie_details['rating']}")
                    st.write(f"**Genres:** {movie_details['genres']}")