import streamlit as st
import os
import time
# comment
# Show title and description.

if st.button("Start"):

    col1, col2 = st.columns(2)
    with col1:

        st.video("https://socialanalyticsplus.net/demo/SKH/videos/Breakingbadnews.mp4", format="video/mp4", autoplay=True)
    
    with col2:

        for tick in range(118):
            time.sleep(1)
            st.text("tick")