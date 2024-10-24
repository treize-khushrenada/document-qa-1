import streamlit as st
from openai import OpenAI
from openai import AzureOpenAI
import os
# comment
# Show title and description.
if st.button("Start"):
    st.video("https://socialanalyticsplus.net/demo/SKH/videos/Breakingbadnews.mp4", format="video/mp4", autoplay="true")