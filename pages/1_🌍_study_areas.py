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

# Sidebar info
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

# Add the geojson to the folium map
geojson.add_to(m)

# Capture map interaction with st_folium
map_output = st_folium(m, width=900, height=700)

# Extract clicked region information
if map_output and 'last_active_drawing' in map_output and map_output['last_active_drawing']:
    clicked_region = map_output['last_active_drawing']['properties']

    # Get clicked region info from selected_regions GeoDataFrame
    region_info = selected_regions[selected_regions['NUTS_ID'] == clicked_region['NUTS_ID']].iloc[0]
    region_details = get_region_info(region_info)

        # Load additional information from the text file
    additional_info = load_additional_info(region_info['NUTS_ID'])

        # Load image based on NUTS_ID
    image_path = load_image(region_info['NUTS_ID'])

    for key, value in region_details.items():
        st.write(f"**{key}:** {value}")

        # Display additional information
    #st.subheader("Additional Information")
    st.markdown(additional_info)

        # Display the image if available
    if image_path:
        #st.sidebar.subheader("Region Image")
        st.sidebar.image(image_path, use_column_width=True)
    else:
        st.sidebar.write("No image available for this region.")
