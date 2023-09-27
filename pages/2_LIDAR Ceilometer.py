import streamlit as st

st.header("LIDAR Ceilometer")

col1, col2, col3 = st.columns([1,1,2])

with col1:
    st.image("./LIDAR Ceilometer (BL View)/CM.jpeg")
    
with col2:
    st.image("/Users/snande/Personal/Projects/dataDisplay/LIDAR Ceilometer (BL View)/PXL_20230310_080803224.jpeg")
    
with col3:
    st.write("""Ceilometer is a remote sensing instrument used for measuring the height and extent of clouds and aerosols in the atmosphere. It operates using the principle of light detection and ranging (LIDAR), which involves emitting pulses of laser light and measuring the time it takes for the light to reflect back from atmospheric particles.
             """)    
    
st.write("")
st.subheader("Near Real Time Data Display")

st.write("image generation ka time")

st.image("/Users/snande/Personal/Projects/dataDisplay/CL_SS.png")
