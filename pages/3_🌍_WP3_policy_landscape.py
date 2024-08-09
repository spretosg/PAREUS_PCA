import streamlit as st
import geemap.foliumap as geemap

Map = geemap.Map(center=[55, 15], zoom=3)

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


# Streamlit app

st.title("Policy landscape")

st.markdown(
    "Within WP3 of the project, the project partner [ILEA SAS](https://www.sav.sk/?lang=en) analyses the policy landscape regarding protected areas and potential OECM. This is done using spatially explicit policy coherence analysis."
)



