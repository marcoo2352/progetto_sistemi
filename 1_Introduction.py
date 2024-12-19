
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
st.markdown("<h1 style='font-size: 25px;'>1.1 Gender and Geographical Area", unsafe_allow_html=True)
st.markdown("""As we can see from the graph below,  we are considering peaple of both genders, as well as non-binary people, nearly in equal numbers:""")



color_Gender = {
    "Female" : "pink", 
    "Male" : "blue",
    "Non-binary" : "yellow",
    "Prefer not to say" : "grey"

}


pie_graph = (alt.Chart(data)
    .mark_arc(
        radius = 70,
        stroke='white',        # Colore del contorno
        strokeWidth=1
        )
    .encode(
        alt.Color("Gender").scale(domain=list(color_Gender.keys()), range=list(color_Gender.values())),
        alt.Theta("count(Gender):Q"))
    .properties(height = 200, width = 300))




pie_graph2 = (
    alt.Chart(data)
    .mark_arc(
        radius=70,
        stroke='white',        # Colore del contorno
        strokeWidth=1          # Spessore del contorno
    )
    .encode(
        alt.Color("Region", scale=alt.Scale(scheme='magma')),
        alt.Theta("count(Region):Q")
    )
    .properties(height=200, width=300)
)

# Calcolo della posizione delle etichette e aggiunta
labels = (
    alt.Chart(data)
    .mark_text(radius=90, fontSize=12)  # Posizione e dimensione del testo
    .encode(
        theta=alt.Theta("count(Region):Q"),  # Stessa codifica angolare
        text=alt.Text("count(Region):Q"),   # Valori da mostrare
        color=alt.value("black")            # Colore del testo
    )
)

# Unione del grafico e delle etichette
final_chart2 = pie_graph2 + labels


col1, col2 = st.columns(2)

with col1:
    st.write("Grafico a torta 1")
    st.altair_chart(pie_graph, use_container_width=True)

with col2:
    st.write("Grafico a torta 2")
    st.altair_chart(final_chart2, use_container_width=True)



tot = (
    alt.Chart(data)
    .mark_text(radius=0, size=30, color= "Black")
    .encode(alt.Text("count(Gender):Q"))   #conta il numero di elementi per ciascuna categoria
    .properties(height=300, width=600)
)



#grafico sui diversi tipi di lavori
st.markdown("<h1 style='font-size: 25px;'>1.2 Industry and Job Role", unsafe_allow_html=True)
st.markdown("""Now let's have a look at the different Industry and different Job Role we are considering, we have to keep in mind that 
            one Job Role can be part of many Industry(exemple: a HR human resaurce can work both for IT and Finance):""")
color_Industry = {
    "Consulting": "#9575cd",   # Viola medio
    "Finance": "#e57373",      # Rosso medio
    "Healthcare": "#81c784",   # Verde medio
    "IT": "#78909c",           # Grigio-blu medio
    "Manufacturing": "#ffb74d", # Arancione medio
    "Retail": "#fff176",       # Giallo medio
    "Education": "#64b5f6"     # Blu medio
}
color_Job_Role = {
    "HR": "#b388eb",               # Viola intenso
    "Data Scientist": "#ff6f61",   # Corallo brillante
    "Sales": "#4db6ac",            # Verde acqua
    "Software Engineer": "#7986cb",# Blu violaceo
    "Project Manager": "#ffb74d",  # Arancione brillante
    "Designer": "#ffd54f",         # Giallo dorato
    "Marketing": "#64b5f6"         # Blu cielo
}


st.markdown("""  """)


Industry_Chart = alt.Chart(data).mark_bar().encode(
                alt.Color("Industry").scale(domain=list(color_Industry.keys()), range=list(color_Industry.values())).legend(None),
                alt.X("count(Industry)"),
                alt.Y("Industry")).properties(height=300, width=600)
Job_Role_Chart = alt.Chart(data).mark_bar().encode(
                alt.Color("Job_Role").scale(domain=list(color_Job_Role.keys()), range=list(color_Industry.values())).legend(None),
                alt.X("count(Job_Role)"),
                alt.Y("Job_Role")).properties(height=300, width=600)
st.altair_chart(Industry_Chart)

st.altair_chart(Job_Role_Chart)


st.markdown("<h1 style='font-size: 25px;'>1.3 Age ", unsafe_allow_html=True)
st.markdown("We are also considering a wide range of ages:")

st.altair_chart(
alt.Chart(data).mark_bar().encode(
    alt.X("Age:Q", bin = True, title= "Age Class"),
    alt.Y("count()", title = "Number of people sampled "),
)
)


st.markdown("<h1 style='font-size: 25px;'>1.4 Intercatcive Dataset Interrogation", unsafe_allow_html=True)
st.markdown("If you wanna know other things about this dataset you can look down here")


# Estrarre valori unici come liste
Gender = data["Gender"].unique().to_list()
Region = data["Region"].unique().to_list()
Industry = data["Industry"].unique().to_list()

# Selectbox per Gender con checkbox per disabilitare
disable_gender = st.checkbox("Disable selectbox Gender", key="disabled1")
option_Gender = st.selectbox(
    "Select a Gender",
    Gender,
    index=None,
    placeholder="Select a Gender...",
    disabled=disable_gender
)
st.write("You selected:", option_Gender)
st.text("        ")

# Selectbox per Region con checkbox per disabilitare
disable_region = st.checkbox("Disable selectbox Region", key="disabled2")
option_Region = st.selectbox(
    "Select a Region",
    Region,
    index=None,
    placeholder="Select a Region...",
    disabled=disable_region
)
st.write("You selected:", option_Region)
st.text("        ")

# Selectbox per Industry con checkbox per disabilitare
disable_industry = st.checkbox("Disable selectbox Industry", key="disabled3")
option_Industry = st.selectbox(
    "Select an Industry",
    Industry,
    index=None,
    placeholder="Select an Industry...",
    disabled=disable_industry
)
st.write("You selected:", option_Industry)

# Filtrare il DataFrame in base alle selezioni
filtered_data = data

if option_Gender:
    filtered_data = filtered_data.filter(pl.col("Gender") == option_Gender)

if option_Region:
    filtered_data = filtered_data.filter(pl.col("Region") == option_Region)

if option_Industry:
    filtered_data = filtered_data.filter(pl.col("Industry") == option_Industry)

# Convertire il DataFrame filtrato in un formato compatibile con Altair (Pandas)
filtered_df = filtered_data.to_pandas()

# Creare e mostrare il grafico filtrato con Altair
if not filtered_df.empty:
    chart = alt.Chart(filtered_df).mark_bar().encode(
        alt.X("Age:Q", bin=True, title="Age Class"),
        alt.Y("count()", title="Number of people sampled")
    )
    st.altair_chart(chart)
else:
    st.write("No data matches the selected filters.")

st.markdown("<h1 style='font-size: 25px;'>1.5 Conclusion", unsafe_allow_html=True)
st.markdown("""These are caratheristics of our sample. We saw that the data are very spread for each variables. 
            Weeknesses: 
            We have no information about the sample mathod and criterian, for this reason could be rappresent NOT well the general population.
            We are considering just 8 Jobs Role that could be not enough to rappresent the general Trend.
            For these reason every conclusion of these analisys can NOT be generalized for the whole population, but just for the subjects of the study.""")