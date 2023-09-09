import streamlit as st

st.header("Laser Precipitation Monitor (LPM)")

col1, col2 = st.columns([1,2])

with col1:
    st.image("/Users/snande/Personal/Projects/dataDisplay/Laser Precipitation Monitor (LPM)/LPMImage.jpeg")
    
with col2:
    st.write("""Laser Precipitation Monitor (LPM) with a wind sensor is an advanced instrument that is used to measure and monitor precipitation. It works on the principle of laser scattering, which is used to detect the presence of precipitation particles in the atmosphere. The wind sensor measures the speed and direction of the wind, which is necessary for the accurate measurement of precipitation. 

It provides high-resolution measurements of precipitation, including the size, shape, and velocity of individual particles which is useful in understanding the physical processes that govern precipitation, and in predicting the impact of precipitation on the environment.""")    
st.subheader("Near Real Time Data Display")

st.write("image generation ka time")

st.image("/Users/snande/Personal/Projects/dataDisplay/CL_SS.png")
