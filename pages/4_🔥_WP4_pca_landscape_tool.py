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
    
    [Institute of Landscape Ecology, Slovak Academy of Sciences (ILE-SAS)](https://www.uke.sav.sk/en/) 
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

st.title("PCA landscape tool - Coherent PA and OECM siting.")

st.markdown(
    "A core functionality of the PAREUS PCA landscape tool is the optimal siting and connection of PA and OECM areas. Optimal siting of PA/OECMs is a task within conservation planning, defined as the designation of new protected areas and OECM`s to meet conservation measures (Margules & Pressey 2000). This work package uses inputs from WP2 and WP3 and applies a spatial optimization model to identify potential OECM areas."
)


st.markdown("### Spatial optimization")
# Accordion using st.expander
with st.expander("**Planning units PU**"):
    st.write("Planning units (PU) are the subdivision of the study area. The size of the PU`s are determined by the input data of the optimization. As a result of the Planning unit, each data can either be a protected area, a OECM or non of them.")
        

# Another accordion
with st.expander("**Features**"):
    st.write("The conservation features serve as a first input to the conservation planning problem, representing features that are aimed to be more protected. These could be species, habitats or ecosystem services (Fang et al., 2022; Ferrier et al., 2002, Knight et al., 2010, Schröter et al., 2014). For biodiversity, joint species distribution models can account for species presence-absence across taxa within multivariate habitat configurations (Warton et al., 2015; Tikhonov et al., 2020)")

with st.expander("**Costs**"):
    st.write("The costs can broadly be distinguished between opportunity costs and costs to establish and manage the protected area (e.g. ). Opportunity costs reflect on the potential foregone revenues through the establishment of a PA. Frequently, these costs are estimated using spatial proxies (Tab 2) of e.g., gross domestic product (Fang et al., 2022), net revenue of forest logging (Schröter et al., 2014) or recreational values, industrial development, and agricultural revenues (Margules & Pressy 2000; Strassburg et al., 2018). **With the PAREUS project, we aim to make a step beyond monetary costs by using policy coherence or ecosystem services to derive cost layers.**")

with st.expander("**Constraints**"):
    st.write("The  constraints narrow the decision space of the optimization. As an example the 30x30 target can be implemented as a constraint that rejects optimal solutions that protect less then 30% of a specific area.")

with st.expander("**Scenarios**"):
    st.write("The stakeholders within the stakeholder group can formulate different scenarios which can then be translated to a new optimization problem.")

