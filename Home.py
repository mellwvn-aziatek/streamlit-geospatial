import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("About")
st.sidebar.info(
    """
    Web App URL: <https://mellwvn-aziatek-streamlit-geospatial-streamlit-app-k2aufj.streamlit.app>
    
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Mellwvn: <mellwvn.aziatek@gmail.com>
    Izlan: <izlan.aziatek@gmail.com>
    """
)

st.sidebar.title("Support")
st.sidebar.info(
    """
    Data Data Data.  Data is our food.
    """
)


st.title("IX Geospatial Applications")

st.markdown(
    """
    This multi-page web app demonstrates various interactive geospatial web apps.

    """
)

st.info("Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/spain.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/las_vegas.gif")

with row1_col2:
    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
