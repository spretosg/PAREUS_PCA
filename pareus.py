import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load the NUTS3 shapefile
selected_regions = gpd.read_file("./data/study_areas.shp")

# Filter to get three specific NUTS3 regions (replace with actual NUTS codes)
#selected_regions = nuts3[nuts3['NUTS_ID'].isin(['DE600', 'FRH01', 'ES300'])]

st.set_page_config(layout="wide")

st.image("./data/logo.png", width=200)

st.markdown("### Providing Adaptive knowledge for Ratcheting up the EU Biodiversity strategy for Sustainable landscapes and protected areas")
st.info("Click on the left sidebar menu to navigate through the project work packages and explore the developed tools")

st.write("Some text here")
st.markdown("### Main objectives")
st.write("Some text")


st.markdown("### Glossary & concepts")
# Accordion using st.expander
with st.expander("**Other Effective area-based Conservation Measures (OECM)**"):
    st.write("Definitions of OECMs")
    st.write("[OECM: A new paradigm for area-based conservation?](https://www.nina.no/english/About-NINA/News/article/oecm-a-new-paradigm-for-area-based-conservation)")
    

# Another accordion
with st.expander("**Protected areas**"):
    st.write("This is another section of content.")

with st.expander("**Conservation**"):
    st.write("This is another section of content.")



st.sidebar.title("Contact")
st.sidebar.info(
    
    """
    Project lead: Roel May
    [Norwegian Institute for Nature Research (NINA)](https://www.nina.no)
    *Trondheim, Norway*
    
    """
)

st.sidebar.title("Project partners")
st.sidebar.info(
    
    """
    
    [Institut National de Recherche pour l’Agriculture l’Alimentation et l’Environnement (INRAE)](https://www.inrae.fr/)
    *Aix-en-Provence, France* 
    
    [Institute of Landscape Ecology, Slovak Academy of Sciences (ILE-SAS)](https://www.sav.sk/?lang=en&doc=ins-org-ins&institute_no=50) 
    *Bratislava, Slovakia*
    """
)

st.sidebar.title("Resources")
st.sidebar.info(
    """
    - [Web App](https://pareus.streamlit.app/)
    - [GitHub repository](https://github.com/spretosg/PAREUS_pca)
    """
)

