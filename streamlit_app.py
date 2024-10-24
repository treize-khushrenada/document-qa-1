import streamlit as st
from openai import OpenAI
from openai import AzureOpenAI
import os
# comment
# Show title and description.

video_file = open("https://socialanalyticsplus.net/demo/SKH/videos/Breakingbadnews.mp4", format="video/mp4")
video_bytes = video_file.read()

st.video(video_bytes)