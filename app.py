import streamlit as st
import pandas as pd
import numpy as np


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Done! (using st.cache_data)")

# st.subheader('Raw data')
# st.write(data)

st.header('My Search', divider='rainbow')

search_text = st.text_input(
    'search label',
    '( TITLE ( "MLOps" ) OR ABS ( "MLOps" ) AND LANGUAGE ( english ) OR TITLE ( "Machine Learning DevOps" ) OR ABS ( "Machine Learning DevOps" ) OR TITLE ( "ML-Ops" ) OR ABS ( "ML-Ops" ) OR TITLE ( "ML-DevOps" ) OR ABS ( "ML-DevOps" ) ) AND PUBYEAR > 2014 AND ( LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "ar" ) )',
    label_visibility='collapsed'
    )

