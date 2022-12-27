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

# Customize page title
st.title("IX Geospatial Applications")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps.
    """
)

st.header("Instructions")

markdown = """
Pages show the capabilities of this library, not actual data.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
