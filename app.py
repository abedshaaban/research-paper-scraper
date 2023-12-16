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



st.header('My Search', divider='rainbow')

search_text = st.text_input(
    'search label',
    '( TITLE ( "MLOps" ) OR ABS ( "MLOps" ) AND LANGUAGE ( english ) OR TITLE ( "Machine Learning DevOps" ) OR ABS ( "Machine Learning DevOps" ) OR TITLE ( "ML-Ops" ) OR ABS ( "ML-Ops" ) OR TITLE ( "ML-DevOps" ) OR ABS ( "ML-DevOps" ) ) AND PUBYEAR > 2014 AND ( LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "ar" ) )',
    label_visibility='collapsed'
    )


sample_data = {
    "title": "Mlp-mixer: An all-mlp architecture for vision",
    "abstract": "This is a sample abstract for the MLP-Mixer paper.",
    "authors": ["IO Tolstikhin", "N Houlsby", "A Kolesnikov"],
    "citations_number": 1657,
    "year": 2021,
    "link": "https://proceedings.neurips.cc/paper/2021/hash/cba0a4ee5ccd02fda0fe3f9a3e7b89fe-Abstract.html",
    "pdf_link": "https://proceedings.neurips.cc/paper/2021/file/cba0a4ee5ccd02fda0fe3f9a3e7b89fe-Paper.pdf",
}


st.subheader(f"[{sample_data["title"]}]({sample_data["link"]})")
st.markdown(f"""
    *Authors:* {' - '.join(sample_data['authors'])} | *Citations:* {sample_data['citations_number']}
    """)
st.write(sample_data["abstract"])
pdf_download_button = st.button("Download PDF")
