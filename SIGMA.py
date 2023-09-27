import streamlit as st

# Set the page width to full
st.markdown(
    """
    <style>
    .reportview-container {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a logo at the top left corner
st.sidebar.image("Indian_Institute_of_Technology,_Indore_Logo.png", width=150)  # Replace "logo.png" with the path to your logo image

st.title("SIGMA Research Lab")
st.header("DAASE, IIT Indore")
st.write("Space Science ||  Climate Informatics  ||   GPS/GNSS  ||   Radar Meteorology ||  Atmospheric Remote Sensing")

st.write("""Welcome to SIGMA Research Lab, Department of Astronomy, Astrophysics and Space Engineering, Indian Institute of Technology Indore, a dynamic and innovative research group dedicated to advancing knowledge and innovation in Radiowave Propagation and Satellite Communication, Microwave Remote Sensing, Radar Meteorology, Satellite-based Navigation, Space Weather and Ionosphere, Climate Change and Tropical Rain, and Machine Learning and Data Science in Atmospheric and Space Science Problems. At SIGMA Research Lab, our team of researchers, students are passionate about exploring new frontiers in these exciting and rapidly evolving fields. We are committed to conducting cutting-edge research that addresses some of the most pressing challenges facing our planet and contributes to the sustainable development of our society. For more details on the current research by the group members, click here.""")

st.header("Data Portal")

st.write("""The SIGMA Research Lab at IIT Indore is equipped with a range of state-of-the-art research instruments that are used to conduct cutting-edge research in the field of Space and Atmosphere. These instruments include a Laser Precipitation Monitor, a Lidar Ceilometer, an Electric Field Monitor, a Lightning Sensor, and a GPS/GNSS receiver. The SIGMA Lab is also open for active collaboration with researchers and industry partners.""")

st.markdown("""
        - Laser Precipitation Monitor (LPM)
        - LIDAR Ceilometer (BL View)
        - LIDAR Ceilometer (CL View)
        """
)
