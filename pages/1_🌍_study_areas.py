import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load the NUTS3 shapefile
selected_regions = gpd.read_file("./data/study_areas.shp")

# Filter to get three specific NUTS3 regions (replace with actual NUTS codes)
#selected_regions = nuts3[nuts3['NUTS_ID'].isin(['DE600', 'FRH01', 'ES300'])]

# Create a Folium map centered on Europe
m = folium.Map(location=[54, 15], zoom_start=4)

# Add the selected regions to the map
for _, row in selected_regions.iterrows():
    folium.GeoJson(row['geometry'],
                   name=row['NUTS_NAME'],
                   tooltip=row['NUTS_NAME'],
                   ).add_to(m)

    folium.Marker(
        location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
        popup=f"<strong>{row['NUTS_NAME']}</strong><br>"
              f"NUTS ID: {row['NUTS_ID']}<br>"
              f"Population: {row['POP'] if 'POP' in row else 'N/A'}<br>"
              f"Area [km2]: {row['AREA'] if 'AREA' in row else 'N/A'}<br>"
              f"{row['PROT_REL'] if 'PROT_REL' in row else 'N/A'} % of the study area is protected",
    ).add_to(m)

# Display the map in the Streamlit app
st.set_page_config(layout="wide")
st.title('PAREUS study areas')


st.sidebar.info(
    """
    - Web App URL: <https://pareus.streamlit.app/>
    - GitHub repository: <https://github.com/spretosg/PAREUS_pca>
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Reto Spielhofer: <https://www.nina.no>
    #PAREUS2024
    """
)
st_folium(m, width=900, height=700)
