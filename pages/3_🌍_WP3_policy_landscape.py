import geemap
import ee
import pandas as pd
import geemap.colormaps as cmaps
import streamlit as st

# Initialize Google Earth Engine
ee.Initialize()

# Define CORINE Land Cover Image
def get_corine_landcover():
    corine = ee.Image("COPERNICUS/CORINE/V20/100m/2018").select('landcover')
    return corine

# Define region geometries
regions = {
    "Trøndelag": ee.Geometry.Polygon([[[10.0, 64.0], [12.5, 64.0], [12.5, 63.2], [10.0, 63.2]]]),
    "Trnava": ee.Geometry.Polygon([[[17.25, 48.5], [17.75, 48.5], [17.75, 48.0], [17.25, 48.0]]]),
    "PACA (France)": ee.Geometry.Polygon([[[5.0, 44.0], [6.5, 44.0], [6.5, 43.0], [5.0, 43.0]]])
}

# Land cover classes and colors (simplified version)
landcover_classes = {
    1: "Artificial surfaces",
    2: "Agricultural areas",
    3: "Forest and seminatural areas",
    4: "Wetlands",
    5: "Water bodies"
}
landcover_colors = ['#e31a1c', '#ff7f00', '#33a02c', '#1f78b4', '#a6cee3']

# Map each landcover class to its label and color
class_colors = {k: landcover_colors[i] for i, k in enumerate(landcover_classes.keys())}

# Get land cover area in km²
def calculate_area(region_geom, landcover_image):
    stats = landcover_image.reduceRegion(
        reducer=ee.Reducer.frequencyHistogram(),
        geometry=region_geom,
        scale=2000,
        maxPixels=1e6
    ).getInfo()
    
    # Calculate area in km²
    class_areas = {landcover_classes[int(k)]: v * 0.01 for k, v in stats['landcover'].items()}
    return pd.DataFrame.from_dict(class_areas, orient='index', columns=['Area (km²)'])

# Streamlit App

st.title("Policy landscape")

st.markdown(
    "Within WP3 of the project, the project partner [ILEA SAS](https://www.uke.sav.sk/en/) analyses the policy landscape regarding protected areas and potential OECM. WP3 will perform an in-depth evaluation into the policy landscape regarding the cumulative effects of current land-use planning practice and how the 30x30 target may be reached under current circumstances, how current PA management as well as OECM in the wider countryside may be improved and how to create a coherent network of PAs."
)

with st.expander("**Policy inventory**"):
    st.write("For each country a selection of international, national and regional policies, relevant for nature protection and OECM definition has been made.")

with st.expander("**Policy coherence**"):
    st.write("Policy coherence looks at the interplay between policies and land use / land cover. In addition, a policy coherence assess to which extent different policies favour or hinder each other towards nature protection and OECM.")
    st.subheader("Land cover")
    st.write("The following main land cover classes have been integrated into the policy coherence analysis")

#st.title("CORINE Land Cover for Selected Regions")
st.sidebar.title("Select Region")
region = st.sidebar.radio("Region", list(regions.keys()))

# Get CORINE data and selected region
corine_image = get_corine_landcover()
region_geom = regions[region]

# Display Map
st.subheader(f"Land Cover Map of {region}")
Map = geemap.Map(center=[50, 15], zoom=5)
Map.addLayer(corine_image.clip(region_geom), {}, "Land Cover")
Map.centerObject(region_geom, 9)
Map.to_streamlit(height=500)

# Display summary graph
st.subheader("Land Cover Area Summary")
area_df = calculate_area(region_geom, corine_image)

# Bar chart for area summary
st.bar_chart(area_df)

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


# Streamlit app


