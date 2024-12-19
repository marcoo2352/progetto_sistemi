
#importiamo le librerie 
import polars as pl  
import streamlit as st
import altair as alt
import numpy as np

data =  pl.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv") #importo il file csv
print(data)

#i dati sono già tidy 
#per le analisi future trasformiamo il dataset in una matrice nunpy
md = data.to_numpy()

#vediamo le variabili presenti nel dataset

#costruiamo il titolo e l'introduzione
st.markdown("<h1 style='font-size: 45px;'>Remote Work & Mental Health</h1", unsafe_allow_html=True)
st.markdown("""As remote work becomes the new norm, it's essential to understand 
       its impact on employees' mental well-being. This dataset dives into
        how working remotely affects stress levels, work-life balance, and mental
        health conditions across various industries and regions.With 5,000 records
        collected from employees worldwide, this dataset provides valuable insights 
        into key areas like work location (remote, hybrid, onsite), stress levels,
        access to mental health resources, and job satisfaction. It’s designed to help researchers,
          HR professionals, and businesses assess the growing influence of remote work on productivity and well-being.""")

#prima introduzione sui dati

st.markdown("<h1 style='font-size: 40px;'>1. Overview of our Sample</h1", unsafe_allow_html=True)

#descrizione gender
#intro
st.markdown("""As we can see from the graph below,  we are considering peaple of both genders, as well as non-binary people, nearly in equal numbers:""")
color_Gender = {
    "Female" : "pink", 
    "Male" : "blue",
    "Non-binary" : "yellow",
    "Prefer not to say" : "grey"

}


pie_graph = (alt.Chart(data)
    .mark_arc(
        cornerRadius=8,
        radius=120,
        radius2=80)
    .encode(
        alt.Color("Gender").scale(domain=list(color_Gender.keys()), range=list(color_Gender.values())),
        alt.Theta("count(Gender):Q"))
    .properties(height = 300, width = 600))


l_data = len(data)    #chiedere al prof come aggiungere  al grafico

tot = (
    alt.Chart(data)
    .mark_text(radius=0, size=30, color= "white")
    .encode(alt.Text("count(Gender):Q"))   #conta il numero di elementi per ciascuna categoria
    .properties(height=300, width=600)
)

st.altair_chart(
    pie_graph + tot,
    use_container_width=True
)


#grafico sui diversi tipi di lavori
st.markdown("""Now let's have a look at the different Industry we are considering:""")
color_Industry = {
    "Consulting" : "purple", 
    "Finance" : "red",
    "Healthcare" : "green",
    "IT" : "black",
    "Manufacturing" :"orange",
    "Retail" : "yellow",
    "Education" : "blue"

}

st.altair_chart(
    alt.Chart(data).mark_bar().encode(
    alt.Color("Industry").scale(domain=list(color_Industry.keys()), range=list(color_Industry.values())).legend(None),
    alt.X("count(Industry)"),
    alt.Y("Industry")
).properties(height=300, width=600)
    )



st.markdown("We are also considering a wide range of ages:")

st.altair_chart(
alt.Chart(data).mark_bar().encode(
    alt.X("Age:Q", bin = True, title= "Age Class"),
    alt.Y("count()", title = "Number of people sampled "),
)
)


st.markdown("We thought that there could be differences among the regions, for this reason we decided to sample from different regions in the world:")







st.markdown("<h1 style='font-size: 40px;'>2. Data analysis</h1", unsafe_allow_html=True)
st.markdown("""In this paragraph, we will analyze the data.
             Our main goal is to better understand remote work and 
             its correlation with mental health. The questions we aim to answer 
             with this analysis are: Is there any connection between remote work and 
             stress, depression, or other mental health conditions?
               Is remote work physically and mentally healthier compared to traditional work settings?
                 Is conventional work or a hybrid model more beneficial?
                   Are there specific jobs or industries where remote work is healthier?""")


