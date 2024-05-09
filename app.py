import streamlit as st
import pandas as pd
from cachetools import cached

from sqlalchemy import create_engine

conn_string_imdb = 'mysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'.format(
    user='students',
    password='0b+5bJWvXoA',
    host = 'jsedocc7.scrc.nyu.edu',
    port=3306,
    db='imdb',
    encoding = 'utf-8'
)
engine_imdb = create_engine(conn_string_imdb)

PAGE_CONFIG = {"page_title":"More Examples","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def hist_all_movies(sql, engine):
    df_movies = pd.read_sql_query(sql, con=engine)
    fig = df_movies.rating.hist().get_figure()
    st.pyplot(fig)

def main():
    st.title("Awesome Streamlit for ML")
    st.subheader("How to run streamlit from colab")
    menu = ["Page 1","Page 2", "Page 3"]
    choice = st.sidebar.selectbox('Menu',menu)
    if choice == 'Page 1':
        st.subheader("Streamlit From Colab")
        text = "this is some text that my code made"
        st.write(text)
    elif choice == 'Page 2':
        SQL_script = st.text_area(label='SQL Input', value='select rating from movies LIMIT 100')
        hist_all_movies(SQL_script, engine_imdb)
    elif choice == 'Page 3':
        slider_value = st.slider('Number of rows', min_value=3, max_value=1000)

        df_movies = pd.read_sql("select * from movies LIMIT " + str(slider_value), con=engine_imdb)
        fig = df_movies.rating[~df_movies.rating.isna()].plot().get_figure()
        st.pyplot(fig)
        show_dataframe = st.checkbox('Display Dataframe')
        if show_dataframe:
            df_movies

if __name__ == '__main__':
    main()
