import streamlit as st
import pickle


movies_list = pickle.load(open("movies_list.pkl", "rb"))
movies=movies_list["title"].values

similarity = pickle.load(open("similarity.pkl", "rb"))
# st.write(similarity)
# st.write(movies_list)


st.header("Movie Recommender System")
movie = st.selectbox("Select a movie", movies)

# st.write(movies_list[movies_list['title'] == movie]['tags'].values[0])
# st.write('Movie Index: ' + str(movies_list[movies_list['title'] == movie]['tags'].index[0]))
# st.write(type(index))


# if st.button("Get Recommendations"):
#     get_recommendations(movie)
     
  


def get_recommendations(movie):
    id = movies_list[movies_list['title'] == movie].index[0]
    # st.write(movies_list[movies_list['title'] == movie].index[0])
    # print(index)
   
    
    distances = sorted(
        list(enumerate(similarity[id])), reverse=True, key=lambda x: x[1]
    )
    # st.write(id_list)
    recommended_movie_names=[]
    for i in distances[1:6]:
        # fetch the movie poster
        # movie_id = movies_list.iloc[i[0]].movie_id
        
        recommended_movie_names.append(movies_list.iloc[i[0]].title)
    return recommended_movie_names

# # st.write(f"You selected: {movie}")

if st.button("Get Recommendations"):
    # st.write(movie)
    recommendations= get_recommendations(movie)
    # st.write("Recommended Movies:") 
    for i in recommendations:
         st.write(i)

 