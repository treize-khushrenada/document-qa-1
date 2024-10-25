import streamlit as st
import time
import pandas as pd

import os
import numpy as np

df = pd.read_csv("./BreakingBadNews.csv")


if st.button("Start"):

    col1, col2 = st.columns(2)
    with col1:

        st.video("https://socialanalyticsplus.net/demo/SKH/videos/Breakingbadnews.mp4", format="video/mp4", autoplay=True)
    
    with col2:
        
        series = df.iloc[0, :].to_frame().T
        my_data_element = st.line_chart(series)

        for tick in range(117):
            time.sleep(1)
            add_df = df.iloc[tick, :].to_frame().T
            my_data_element.add_rows(add_df)