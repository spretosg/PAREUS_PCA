import streamlit as st
import geemap.foliumap as geemap

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

st.title("Policy landscape")

st.markdown(
    "Within WP3 of the project, the project partner [ILEA SAS](https://www.sav.sk/?lang=en) analyses the policy landscape regarding protected areas and potential OECM. WP3 will perform an in-depth evaluation into the policy landscape regarding the cumulative effects of current land-use planning practice and how the 30x30 target may be reached under current circumstances, how current PA management as well as OECM in the wider countryside may be improved and how to create a coherent network of PAs."
)

with st.expander("**Policy inventory**"):
    st.write("This is another section of content.")

with st.expander("**Policy coherence**"):
    st.write("This is another section of content.")



