import streamlit as st
import pickle
import numpy as np
from PIL import Image
import os

# Load model
rfc = pickle.load(open('rfc.pkl', 'rb'))

# Title and banner image
st.title('🌲 Forest Cover Type Prediction')
main_image_path = 'image/img.jpg'
if os.path.exists(main_image_path):
    st.image(Image.open(main_image_path), caption="Forest Cover Types", use_container_width=True)
else:
    st.warning("Main image not found in 'image/' folder.")

# Input field
user_input = st.text_input('🔢 Enter features (comma-separated):')

# Predict button
if st.button('Predict'):
    if user_input:
        try:
            features = np.array([list(map(float, user_input.split(',')))])
            prediction = rfc.predict(features)[0]

            # Cover type dictionary
            cover_type_dict = {
                1: {"name": "Spruce/Fir", "image": "img_1.jpg"},
                2: {"name": "Lodgepole Pine", "image": "img_2.png"},
                3: {"name": "Ponderosa Pine", "image": "img_3.png"},
                4: {"name": "Cottonwood/Willow", "image": "img_4.jpg"},
                5: {"name": "Aspen", "image": "img_5.jpg"},
                6: {"name": "Douglas-fir", "image": "img_6.png"},
                7: {"name": "Krummholz", "image": "img_7.png"}
            }

            forest_details = {
    1: "🌲 **Spruce/Fir Forests**:\n"
       "- **Location**: Found at high elevations in the Rocky Mountains and northern latitudes.\n"
       "- **Climate**: Cold and moist; average temperatures range from -5°C to 10°C (23°F to 50°F).\n"
       "- **Soil**: Acidic, well-drained soils.\n"
       "- **Features**: Dense coniferous trees like Engelmann Spruce and Subalpine Fir; adapted to snow-heavy conditions.\n"
       "- **Wildlife**: Supports moose, elk, lynx, and various bird species.",

    2: "🌲 **Lodgepole Pine Forests**:\n"
       "- **Location**: Widespread across the western U.S., especially Yellowstone and the Rockies.\n"
       "- **Climate**: Cool, dry summers and snowy winters; temperature from -10°C to 20°C (14°F to 68°F).\n"
       "- **Soil**: Nutrient-poor, well-drained soils.\n"
       "- **Features**: Tall, slender pines; highly fire-adapted; often regenerate after wildfires.\n"
       "- **Wildlife**: Habitat for black bears, squirrels, woodpeckers.",

    3: "🌲 **Ponderosa Pine Forests**:\n"
       "- **Location**: Found in drier mountain areas of the western U.S., like Colorado Plateau and Arizona.\n"
       "- **Climate**: Warm summers, mild winters; 5°C to 25°C (41°F to 77°F).\n"
       "- **Soil**: Sandy or gravelly soils with good drainage.\n"
       "- **Features**: Fire-resistant bark; widely spaced trees with grassy understory.\n"
       "- **Wildlife**: Supports mule deer, turkeys, and bats.",

    4: "🌳 **Cottonwood/Willow Forests**:\n"
       "- **Location**: Along rivers, streams, and wetlands in the western U.S.\n"
       "- **Climate**: Temperate; 0°C to 25°C (32°F to 77°F).\n"
       "- **Soil**: Moist, alluvial soils.\n"
       "- **Features**: Deciduous trees; flood-tolerant; important for riparian ecosystems.\n"
       "- **Wildlife**: Attracts beavers, herons, songbirds, and amphibians.",

    5: "🍂 **Aspen Forests**:\n"
       "- **Location**: High altitudes in the Rockies, Sierra Nevada, and northern states.\n"
       "- **Climate**: Cool climates; -5°C to 20°C (23°F to 68°F).\n"
       "- **Soil**: Loamy and moist soils.\n"
       "- **Features**: White bark; known for fall color; regenerate via root suckers forming clones.\n"
       "- **Wildlife**: Elk, deer, and ruffed grouse thrive here.",

    6: "🌲 **Douglas-Fir Forests**:\n"
       "- **Location**: Pacific Northwest, northern California, and inland U.S. Rockies.\n"
       "- **Climate**: Mild, wet winters and warm, dry summers; 5°C to 20°C (41°F to 68°F).\n"
       "- **Soil**: Fertile, volcanic or glacial soils.\n"
       "- **Features**: Tall evergreen trees; important timber species; cones have unique three-pointed bracts.\n"
       "- **Wildlife**: Owls, squirrels, and woodpeckers commonly inhabit these forests.",

    7: "🌲 **Krummholz** (German for 'twisted wood'):\n"
       "- **Location**: Alpine tree line zones in high mountains like the Rockies.\n"
       "- **Climate**: Harsh, windy, and cold; -20°C to 10°C (-4°F to 50°F).\n"
       "- **Soil**: Shallow, rocky, and nutrient-poor soils.\n"
       "- **Features**: Stunted, twisted trees shaped by wind and ice; often includes dwarf spruce and fir.\n"
       "- **Wildlife**: Limited but includes ptarmigans and mountain goats adapted to high altitudes."
}


            # Display result
            cover = cover_type_dict.get(prediction)
            if cover:
                col1, col2 = st.columns([2, 3])
                with col1:
                    st.markdown("### 🌿 Predicted Cover Type:")
                    st.markdown(f"<h2 style='color: green;'>{cover['name']}</h2>", unsafe_allow_html=True)

                with col2:
                    cover_image_path = os.path.join("image", cover["image"])
                    if os.path.exists(cover_image_path):
                        st.image(Image.open(cover_image_path), caption=cover['name'], use_container_width=True)
                    else:
                        st.warning("Cover type image not found.")

                st.markdown("---")
                st.markdown(f"### 📘 About {cover['name']} Forest")
                st.markdown(forest_details.get(prediction, "No details available."))
            else:
                st.error("Prediction failed. Unknown cover type.")

        except Exception as e:
            st.error(f"Error processing input: {e}")
    else:
        st.warning("Please enter input features before predicting.")
