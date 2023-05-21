import streamlit as st 
import pandas as pd
import pickle
import requests
import time


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))

    data = response.json()
    #st.image("https://image.tmdb.org/t/p/w500" + data['poster_path'])
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']



#content based

def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    # st.write(movies_list)
    
    recommend_movies=[]
    recommend_movies_poster=[]
    content_mean=0

    for i in movies_list:
        movie_id=movies.iloc[i[0]]['id']
        content_mean+=i[1]*100

        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
        
    
    return (recommend_movies,recommend_movies_poster,round((content_mean)/5, 2))


#collaborative

def recommend_col(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[10:21:2]
    # st.write(movies_list)
    
    
    recommend_movies=[]
    recommend_movies_poster=[]
    content_mean=0

    for i in movies_list:
        movie_id=movies.iloc[i[0]]['id']
        content_mean+=i[1]*100

        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
        
    
    return (recommend_movies,recommend_movies_poster,round((content_mean)/5, 2))





movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))



st.title("Movie Recommender System")

selected_movie_name=st.selectbox(
    'How would like to be contacted?',
    movies['title'].values
)



start_time = time.time()

if st.button('Recommend for content based'):
    #print(recommend(selected_movie_name))
    (names,posters,content_mean)=recommend(selected_movie_name)
    # st.write(names)
    st.text('Content Based Recommendation with the accuracy is ' + str(content_mean) + '%')

    

    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])

end_time = time.time()
total_time = end_time - start_time

st.write("Total time:", total_time, "seconds")


# exit()


# movies1=pd.DataFrame(movies_dict)

# selected_movie=st.selectbox(
#     'How would like to be contacted?',
#     movies1['title'].values
# )



# if st.button('Recommend for collaborative'):
#     #print(recommend(selected_movie_name))
#     (names,posters,content_mean)=recommend_col(selected_movie_name)
#     # st.write(names)
#     st.text('Collaborative Based Recommendation with the accuracy is ' + str(content_mean) + '%')

    

#     col1,col2,col3,col4,col5=st.columns(5)

#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#         st.write(posters[1])
    
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
    
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
    
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
    
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])