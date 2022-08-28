import streamlit as st
import pandas as pd

# make title and header
st.title(" Open Pubs Nearby")
st.header("Data details: ")

# import the modified data 
df = pd.read_csv("data/cleaned_open_pubs_data.csv")

st.text('''Let’s assume you are on a Vacation in the United Kingdom with your friends. Just for 
some fun, you decided to go to the Pubs nearby for some drinks. Google Map 
is down because of some issues. 
While searching the internet, you came across https://www.getthedata.com/open-pubs. 
On this website, you found all the pub locations (Specifically Latitude 
and Longitude info). 
In order to impress your friends, you decided to create a Web Application 
with the data available in your hand. 
''')
st.header("Available Data: ")


# print the data frame
st.dataframe(df.head(11))
st.subheader('The total number of rows in the data are :') 
total = df.count()[0]
st.text(total)
