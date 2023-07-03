import numpy as np
import requests
import streamlit as st

#  ENDPOINT = "https://cataas.com/cat"

# with st.sidebar:
#     st.header("Configuration")
#     with st.form(key="grid_reset"):
#         n_photos = st.slider("Number of cat photos:", 4, 128, 16)
#         n_cols = st.number_input("Number of columns", 2, 8, 4)
#         st.form_submit_button(label="Reset images and layout")
#     with st.expander("About this app"):
#         st.markdown("It's about cats :cat:!")
#     st.caption("Source: https://cataas.com/#/")

st.title("Birdseye - Unit Monitoring")
# st.caption(
#     "You can display the image in full size by hovering it and clicking the double arrow"
# )

# cat_images = [
#     requests.get(f"{ENDPOINT}?width=1200&height=1200").content for i in range(n_photos)
# ]

# units = get_all_units()
unit_count = 31#len(units)
n_cols = 10 # 10 columns wide
n_rows = 1 + unit_count // int(n_cols)

rows = [st.container() for _ in range(n_rows)]
cols_per_row = [r.columns(n_cols) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, cat_image in enumerate(cat_images):
    a = cols[image_index].empty()
    a.text("a")