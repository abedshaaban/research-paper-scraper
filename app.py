# import streamlit as st
# import pandas as pd
# import numpy as np
# from func import get_google_data

# col1, col2 = st.columns([9, 1])
# col_fill = st.columns(2)

# def search():

#     data = get_google_data(search_text)

#     for article in data:
#         st.subheader(f"[{article['title']}]({article['link']})")
#         st.markdown(f"""
#             *Authors:* {' - '.join(article['authors'])} | *Citations:* {article['citations_number']}
#         """)
#         st.write(article["abstract"])
#         pdf_download_button = st.button("Download PDF", key=f"download_button_{article['title']}")

# col1.header('My Search', divider='rainbow')



# col2.button("Reset", type="primary")

# search_text = col1.text_input(
#         'Search Label',
#         '( TITLE ( "MLOps" ) OR ABS ( "MLOps" ) AND LANGUAGE ( english ) OR TITLE ( "Machine Learning DevOps" ) OR ABS ( "Machine Learning DevOps" ) OR TITLE ( "ML-Ops" ) OR ABS ( "ML-Ops" ) OR TITLE ( "ML-DevOps" ) OR ABS ( "ML-DevOps" ) ) AND PUBYEAR > 2014 AND ( LIMIT-TO ( DOCTYPE , "cp" ) OR LIMIT-TO ( DOCTYPE , "ar" ) )',
#         label_visibility='collapsed'
#     )

# # search()

from flask import Flask
from views import views

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=true)