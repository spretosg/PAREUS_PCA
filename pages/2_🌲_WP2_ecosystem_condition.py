import streamlit as st
import geemap.foliumap as geemap
import ee


geemap.ee_initialize(token_name="EARTHENGINE_TOKEN")

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


TRD_es = ee.Image('projects/pareus/assets/WP2/ES_cond_state_TRD')
SVK_es = ee.Image('projects/pareus/assets/WP2/TRNAVA_ES_cond')
FRA_es = ee.Image('projects/pareus/assets/WP2/PACA_ES_cond')

# Streamlit app

st.title("Ecosystem condition")
st.markdown(
    "Within WP2 of the project, the project partner [INRAE](https://www.inrae.fr/en) models ecosystem condition. The condition modeling is based on standardised NDVI per world cover type, soil carbon content, biodiversity intactness index and natural land cover types. The index is just valid within a case study area and can`t be compared across different areas."
)

st.markdown("""
- What are the ecostem extents and conditions within the case study areas?

- Map the ecosystem services (nature values) in the case study areas

""")

vis_params = {
    'min': 0,
    'max': 1,
    'palette': ['red', 'orange','yellow', 'green','darkgreen'],
}
#Map.addLayer(TRD_es, vis_params, 'Ecosystem condition Trøndelag', shown=False)
#Map.addLayer(SVK_es, vis_params, 'Ecosystem condition Trnava Region', shown=False)
#Map.addLayer(FRA_es, vis_params, 'Ecosystem condition PACA', shown=False)

selected_layer = st.radio("Select Image Layer", ["Ecosystem condition Trøndelag", "Ecosystem condition Trnava Region", "Ecosystem condition PACA"])


# Update the visibility of the layers based on user selection
if selected_layer == "Ecosystem condition Trøndelag":
    Map.addLayer(TRD_es, vis_params, 'Ecosystem condition Trøndelag', shown=True)
    Map.add_colorbar(
    vis_params,
    label="Ecosystem condition",
    layer_name="Ecosystem condition Trøndelag",
    orientation="horizontal",
    transparent_bg=True,
    )
    Map.centerObject(TRD_es)
 
elif selected_layer == "Ecosystem condition Trnava Region":

    Map.addLayer(SVK_es, vis_params, 'Ecosystem condition Trnava Region', shown=True)
    Map.add_colorbar(
    vis_params,
    label="Ecosystem condition",
    layer_name="Ecosystem condition Trnava Region",
    orientation="horizontal",
    transparent_bg=True,
    )
    Map.centerObject(SVK_es)

else:

    Map.addLayer(FRA_es, vis_params, 'Ecosystem condition PACA', shown=True)
    Map.add_colorbar(
    vis_params,
    label="Ecosystem condition",
    layer_name="Ecosystem condition PACA'",
    orientation="horizontal",
    transparent_bg=True,
    )
    Map.centerObject(FRA_es)

    # Display the map in Streamlit

Map.to_streamlit(height=600)

