import streamlit as st
import geemap.foliumap as geemap
import streamlit.components.v1 as components

Map = geemap.Map(center=[55, 15], zoom=3)

st.set_page_config(layout="wide")

st.sidebar.image("./data/logo.png", width=200)
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


# Streamlit app

st.title("PCA landscape tool")

st.markdown(
    "This work package uses inputs from WP2 and WP3 and applies a spatial optimization model to identify potential OECM areas."
)


st.markdown("### Spatial optimization")
# Accordion using st.expander
with st.expander("**Planning units PU**"):
    st.write("Planning units are...")
    
    

# Another accordion
with st.expander("**Features**"):
    st.write("This is another section of content.")

with st.expander("**Costs**"):
    st.write("This is another section of content.")

with st.expander("**Constraints**"):
    st.write("This is another section of content.")

with st.expander("**Scenarios**"):
    st.write("This is another section of content.")

