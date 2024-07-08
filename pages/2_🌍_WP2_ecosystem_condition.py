import streamlit as st
import geemap.foliumap as geemap
import ee


geemap.ee_initialize(token_name="EARTHENGINE_TOKEN")

#def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
#    geemap.ee_initialize(token_name=token_name)
Map = geemap.Map(center=[65, 15], zoom=4)

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - Web App URL: <https://pareus.streamlit.app/>
    - GitHub repository: <https://github.com/spretosg/PAREUS_pca>>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Reto Spielhofer: <https://www.nina.no>
     #PAREUS2024
    """
)



TRD_es = ee.Image('projects/pareus/assets/WP2/ES_cond_state_TRD') 

# Streamlit app

st.title("Ecosystem condition")


    # Create a map

Map.addLayer(TRD_es, {'min': 0, 'max': 1, 'palette': ['red', 'orange','yellow', 'green','darkgreen']}, 'Ecosystem condition Trondheim')

    # Display the map in Streamlit
st.write("Based on standardised NDVI per world cover type, soil carbon content, biodiversity intactness index and natural land cover types")
Map.to_streamlit(height=600)

