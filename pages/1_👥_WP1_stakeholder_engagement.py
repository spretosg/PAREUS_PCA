import streamlit as st
import geemap.foliumap as geemap


#def ee_authenticate(token_name="EARTHENGINE_TOKEN"):
#    geemap.ee_initialize(token_name=token_name)
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
    
    [Institute of Landscape Ecology, Slovak Academy of Sciences (ILE-SAS)](https://www.uke.sav.sk/en/ ) 
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



st.title("Stakeholder engagement")
st.markdown(
    "This work packages onboards the stakeholder groups in all the three case study areas. The follwing three research questions are adressed."
)
st.markdown("""
- Q1: Current state of PA --> What is the strength / weakness of the current PA network (in quantity(area) and quality) what are potential opportunities for the region, and what are potential challenges/trade-offs?

- Q2: Given the 30x30 target, how can the OECM concept be useful to reach the target? Or if not how should the OECM concept be adjusted to contribute?

- Q3: What are potential OECMs in the study area, and what are their main characteristics  (social, environment and economic perspectives)?
""")


st.markdown("### Definitions in the three case studies")
# Another accordion
with st.expander("**Protected areas**"):
    st.write("This is another section of content.")

with st.expander("**Conservation**"):
    st.write("This is another section of content.")

with st.expander("**Conservation**"):
    st.write("This is another section of content.")