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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on page 
streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])




