#importiamo le librerie 
import polars as pl  
import streamlit as st
import altair as alt
import numpy as np

st.markdown("<h1 style='font-size: 40px;'>2. Data analysis</h1", unsafe_allow_html=True)
st.markdown("""In this paragraph, we will analyze the data.
             Our main goal is to better understand remote work and 
             its correlation with mental health. The questions we aim to answer 
             with this analysis are: Is there any connection between remote work and 
             stress, depression, or other mental health conditions?
               Is remote work physically and mentally healthier compared to traditional work settings?
                 Is conventional work or a hybrid model more beneficial?
                   Are there specific jobs or industries where remote work is healthier?""")

st.markdown("<h1 style='font-size: 25px;'>2.1 Is the Mental Health Condition worst or better in Remote worker?", unsafe_allow_html=True)
st.markdown("""We know for every subject if they suffer from Anxiety, Depression or Bornout; in this case we will assign the value 1 and 0 otherwise.
            We start by considering the null hypotesis H0: mur = muh = muo against the hypotesis H1: ¬H0. Where mur, muh, muo; rappresents the mean of the person that work respectevly from Remote, Hybrid, Onside.
            We can test this hypotesis simply with an omogenity test.""")
################################################################################################################################################
#                                                    Test eseguito su R(1)                                                                    #
###############################################################################################################################################à

