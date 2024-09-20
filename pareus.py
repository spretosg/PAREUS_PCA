import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load the NUTS3 shapefile
selected_regions = gpd.read_file("./data/study_areas.shp")

# Filter to get three specific NUTS3 regions (replace with actual NUTS codes)
#selected_regions = nuts3[nuts3['NUTS_ID'].isin(['DE600', 'FRH01', 'ES300'])]

st.set_page_config(layout="wide")

# Display the map in the Streamlit app
st.sidebar.image("./data/logo.png", width=200)
st.title('PAREUS PCA landscape tool')


st.sidebar.info(
    """
    - Web App URL: <https://pareus.streamlit.app/>
    - GitHub repository: <https://github.com/spretosg/PAREUS_pca>
    """
)
st.info("Click on the left sidebar menu to navigate to the different apps.")

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Reto Spielhofer: <https://www.nina.no>
    #PAREUS2024
    """
)
#st_folium(m, width=900, height=700)
