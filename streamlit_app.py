import streamlit
streamlit.title('My Moms new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣avalakki')
streamlit.text('🥗uppittu')
streamlit.text('🐔dosa')
streamlit.text('🥑edli')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
