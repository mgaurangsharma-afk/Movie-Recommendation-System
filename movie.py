# import streamlit as st
# import pickle
# import time
# import requests

# # ---------------- PAGE CONFIG ---------------- #

# st.set_page_config(
#     page_title="🎬 CineMatch",
#     page_icon="🎬",
#     layout="wide"
# )

# # ---------------- LOAD DATA ---------------- #

# new_df = pickle.load(open("new_df.pkl", "rb"))
# similarity = pickle.load(open("similarity.pkl", "rb"))


# # ---------------- RECOMMEND FUNCTION ---------------- #

# def recommend(movie):

#     movie_index = new_df[new_df['title'] == movie].index[0]

#     distances = similarity[movie_index]

#     movies_list = sorted(
#         list(enumerate(distances)),
#         reverse=True,
#         key=lambda x: x[1]
#     )[1:6]

#     recommendations = []

#     for i in movies_list:
#         recommendations.append(new_df.iloc[i[0]].title)

#     return recommendations


# # ---------------- TMDB API FUNCTION ---------------- #

# @st.cache_data(ttl=86400)
# def fetch_movie_details(movie_title, api_key):

#     url = "https://api.themoviedb.org/3/search/movie"

#     params = {
#         "api_key": api_key,
#         "query": movie_title,
#         "language": "en-US",
#         "include_adult": False
#     }

#     try:

#         response = requests.get(
#             url,
#             params=params,
#             timeout=10
#         )

#         response.raise_for_status()

#         data = response.json()

#         results = data.get("results", [])

#         if not results:
#             return None

#         # Find exact movie title

#         movie = next(
#             (
#                 item for item in results
#                 if item.get("title", "").lower()
#                 == movie_title.lower()
#             ),
#             results[0]
#         )

#         poster_path = movie.get("poster_path")

#         poster_url = None

#         if poster_path:
#             poster_url = (
#                 "https://image.tmdb.org/t/p/w500"
#                 + poster_path
#             )

#         return {
#             "poster": poster_url,
#             "overview": movie.get("overview"),
#             "rating": movie.get("vote_average"),
#             "release_date": movie.get("release_date")
#         }

#     except requests.exceptions.RequestException:
#         return None


# # ---------------- CUSTOM CSS ---------------- #

# st.markdown("""
# <style>

# .stApp {
#     background-color: #0E1117;
# }

# h1 {
#     color: #E50914;
#     text-align: center;
# }

# .movie-title {
#     color: white;
#     font-size: 17px;
#     font-weight: bold;
#     text-align: center;
# }

# footer {
#     visibility: hidden;
# }

# header {
#     visibility: hidden;
# }

# #MainMenu {
#     visibility: hidden;
# }

# </style>
# """, unsafe_allow_html=True)


# # ---------------- SIDEBAR ---------------- #

# st.sidebar.title("🎬 CineMatch")

# st.sidebar.markdown("""
# ### About

# This recommendation system uses:

# ✅ Content Based Filtering

# ✅ CountVectorizer

# ✅ Cosine Similarity

# ---

# ### Technologies

# - Python
# - Pandas
# - Scikit-Learn
# - Streamlit
# - TMDB API
# """)

# # API KEY INPUT

# st.sidebar.markdown("---")

# st.sidebar.subheader("TMDB Configuration")

# api_key = st.sidebar.text_input(
#     "Enter TMDB API Key",
#     type="password",
#     placeholder="Your TMDB API Key"
# )

# st.sidebar.caption(
#     "Your API key is used to fetch movie posters."
# )

# st.sidebar.markdown("---")

# st.sidebar.markdown("""
# ### Movie Data Credits

# This product uses the TMDB API
# but is not endorsed or certified by TMDB.
# """)


# # ---------------- TITLE ---------------- #

# st.title("🎬 CineMatch")

# st.markdown(
#     """
#     <h4 style='text-align:center;color:white;'>
#     Discover Movies Similar To Your Favorites
#     </h4>
#     """,
#     unsafe_allow_html=True
# )

# st.write("")


# # ---------------- SELECT MOVIE ---------------- #

# selected_movie = st.selectbox(
#     "🎥 Choose a Movie",
#     sorted(new_df["title"].unique())
# )

# st.write("")


# # ---------------- RECOMMEND BUTTON ---------------- #

# if st.button(
#     "🍿 Recommend Movies",
#     use_container_width=True
# ):

#     if not api_key:

#         st.warning("Please enter your TMDB API Key in the sidebar.")

#     else:

#         with st.spinner("Finding Similar Movies..."):

#             time.sleep(1)

#             recommendations = recommend(selected_movie)

#             movie_details = []

#             for movie in recommendations:

#                 details = fetch_movie_details(
#                     movie,
#                     api_key
#                 )

#                 movie_details.append(details)

#         st.success("Top Recommendations")

#         # Display five movie columns

#         cols = st.columns(5)

#         for col, movie, details in zip(
#             cols,
#             recommendations,
#             movie_details
#         ):

#             with col:

#                 # Movie poster

#                 if details and details["poster"]:

#                     st.image(
#                         details["poster"],
#                         use_container_width=True
#                     )

#                 else:

#                     st.info("Poster not available")

#                 # Movie title

#                 st.markdown(
#                     f"<div class='movie-title'>{movie}</div>",
#                     unsafe_allow_html=True
#                 )

#                 # Movie rating and release date

#                 if details:

#                     if details["rating"] is not None:

#                         st.caption(
#                             f"⭐ Rating: {details['rating']:.1f}/10"
#                         )

#                     if details["release_date"]:

#                         st.caption(
#                             f"📅 {details['release_date']}"
#                         )

#                     # Movie description

#                     if details["overview"]:

#                         with st.expander("About Movie"):

#                             st.write(details["overview"])


# # ---------------- FOOTER ---------------- #

# st.write("")
# st.write("")

# st.markdown("---")

# st.markdown(
#     """
#     <center>
#     <font color='gray'>
#     Movie Recommendation System • Built with Streamlit
#     </font>
#     </center>
#     """,
#     unsafe_allow_html=True
# )





import streamlit as st
import pickle
import time
import requests

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🎬 CineMatch",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

new_df = pickle.load(open("new_df.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


# ---------------- RECOMMEND FUNCTION ---------------- #

def recommend(movie):

    movie_index = new_df[new_df['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:
        recommendations.append(new_df.iloc[i[0]].title)

    return recommendations


# ---------------- TMDB API FUNCTION ---------------- #

@st.cache_data(ttl=86400)
def fetch_movie_details(movie_title, api_key):

    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": api_key,
        "query": movie_title,
        "language": "en-US",
        "include_adult": False
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        results = data.get("results", [])

        if not results:
            return None

        # Find exact movie title

        movie = next(
            (
                item for item in results
                if item.get("title", "").lower()
                == movie_title.lower()
            ),
            results[0]
        )

        poster_path = movie.get("poster_path")

        poster_url = None

        if poster_path:
            poster_url = (
                "https://image.tmdb.org/t/p/w500"
                + poster_path
            )

        return {
            "poster": poster_url,
            "overview": movie.get("overview"),
            "rating": movie.get("vote_average"),
            "release_date": movie.get("release_date")
        }

    except requests.exceptions.RequestException:
        return None


# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

h1 {
    color: #E50914;
    text-align: center;
}

.movie-title {
    color: white;
    font-size: 17px;
    font-weight: bold;
    text-align: center;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🎬 CineMatch")

st.sidebar.markdown("""
### About

This recommendation system uses:

✅ Content Based Filtering

✅ CountVectorizer

✅ Cosine Similarity

---

### Technologies

- Python
- Pandas
- Scikit-Learn
- Streamlit
- TMDB API
""")

# API KEY INPUT

st.sidebar.markdown("---")

st.sidebar.subheader("TMDB Configuration")

api_key = st.sidebar.text_input(
    "Enter TMDB API Key",
    type="password",
    placeholder="Your TMDB API Key"
)

st.sidebar.caption(
    "Your API key is used to fetch movie posters."
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### Movie Data Credits

This product uses the TMDB API
but is not endorsed or certified by TMDB.
""")


# ---------------- TITLE ---------------- #

st.title("🎬 CineMatch")

st.markdown(
    """
    <h4 style='text-align:center;color:white;'>
    Discover Movies Similar To Your Favorites
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")


# ---------------- SELECT MOVIE ---------------- #

selected_movie = st.selectbox(
    "🎥 Choose a Movie",
    sorted(new_df["title"].unique())
)

st.write("")


# ---------------- RECOMMEND BUTTON ---------------- #

if st.button(
    "🍿 Recommend Movies",
    use_container_width=True
):

    if not api_key:

        st.warning("Please enter your TMDB API Key in the sidebar.")

    else:

        with st.spinner("Finding Similar Movies..."):

            time.sleep(1)

            recommendations = recommend(selected_movie)

            movie_details = []

            for movie in recommendations:

                details = fetch_movie_details(
                    movie,
                    api_key
                )

                movie_details.append(details)

        st.success("Top Recommendations")

        # Display five movie columns

        cols = st.columns(5)

        for col, movie, details in zip(
            cols,
            recommendations,
            movie_details
        ):

            with col:

                # Movie poster

                if details and details["poster"]:

                    st.image(
                        details["poster"],
                        use_container_width=True
                    )

                else:

                    st.info("Poster not available")

                # Movie title

                st.markdown(
                    f"<div class='movie-title'>{movie}</div>",
                    unsafe_allow_html=True
                )

                # Movie rating and release date

                if details:

                    if details["rating"] is not None:

                        st.caption(
                            f"⭐ Rating: {details['rating']:.1f}/10"
                        )

                    if details["release_date"]:

                        st.caption(
                            f"📅 {details['release_date']}"
                        )

                    # Movie description

                    if details["overview"]:

                        with st.expander("About Movie"):

                            st.write(details["overview"])


# ---------------- FOOTER ---------------- #

st.write("")
st.write("")

st.markdown("---")

st.markdown(
    """
    <center>
    <font color='gray'>
    Movie Recommendation System • Built with Streamlit
    </font>
    </center>
    """,
    unsafe_allow_html=True
)





















