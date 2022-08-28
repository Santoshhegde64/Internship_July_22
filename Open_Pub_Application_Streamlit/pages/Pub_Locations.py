import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pub_Locations"
)

df = pd.read_csv("data/cleaned_open_pubs_data.csv")

# make header
st.header("Location of all Bars in UK based on the Local Authority")
# enter either postal code or local authority

local_auth = st.selectbox('The Local Authority of the Area which you want to search', set(df['Local_Authority']))
button_1 = st.button("Submit")

if button_1:
    df_new = df.loc[(df['Local_Authority'] == local_auth)]
    st.text("The Pubs in this Region are:")
    st.dataframe(df_new)
    st.map(df_new)