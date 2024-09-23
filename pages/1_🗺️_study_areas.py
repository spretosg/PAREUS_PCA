import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from folium.features import GeoJson
import os

# Load the NUTS3 shapefile
selected_regions = gpd.read_file("./data/study_areas.shp")

# Ensure geometries are in WGS84 (latitude/longitude)
selected_regions = selected_regions.to_crs(epsg=4326)

# Create a Folium map centered on Europe
m = folium.Map(location=[54, 15], zoom_start=4)

# Function to generate region information
def get_region_info(row):
    return {
        "NUTS Name": row['NUTS_NAME'],
        "NUTS ID": row['NUTS_ID'],
        "Population": row.get('POP', 'N/A'),
        "Area [km²]": row.get('AREA', 'N/A'),
        "Protected Area [%]": row.get('PROT_REL', 'N/A')
    }
# Function to load additional information from a text file
def load_additional_info(nuts_id):
    file_path = f"./data/{nuts_id}.txt"  # Adjust path as necessary
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return "No additional information available."

# Function to load image based on NUTS_ID
def load_image(nuts_id):
    image_path = f"./data/{nuts_id}.jpg"  # Adjust path and format as necessary
    if os.path.exists(image_path):
        return image_path
    return None

# Add the selected regions to the map
geojson = GeoJson(
    selected_regions,
    name='NUTS Regions',
    tooltip=folium.GeoJsonTooltip(fields=['NUTS_NAME'], aliases=['Region']),
)

# Display the map in the Streamlit app
st.set_page_config(layout="wide")

st.title('PAREUS Study Areas')
st.info("Click on the region you are interested to learn more about")

# Create two columns: one for the map and another for details
col1, col2 = st.columns([2, 1])  # Adjust ratio for width

# Display the map in the left column
with col1:
    # Add the geojson to the folium map
    geojson.add_to(m)
    map_output = st_folium(m, width=900, height=700)
    
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



# Capture map interaction with st_folium
#map_output = st_folium(m, width=900, height=700)

# Extract clicked region information
with col2:
    if map_output and 'last_active_drawing' in map_output and map_output['last_active_drawing']:
        clicked_region = map_output['last_active_drawing']['properties']

        # Get clicked region info from selected_regions GeoDataFrame
        region_info = selected_regions[selected_regions['NUTS_ID'] == clicked_region['NUTS_ID']].iloc[0]
        region_details = get_region_info(region_info)

        image_path = load_image(region_info['NUTS_ID'])

        # Load additional information from the text file
        additional_info = load_additional_info(region_info['NUTS_ID'])

            # Load image based on NUTS_ID
        

        for key, value in region_details.items():
            st.write(f"**{key}:** {value}")

        if image_path:
            #st.sidebar.subheader("Region Image")
            st.image(image_path, use_column_width=True)
        else:
            st.write("No image available for this region.")

            # Display additional information
        #st.subheader("Additional Information")
        st.markdown(additional_info)


        