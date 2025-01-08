#importiamo le librerie 
import polars as pl  
import streamlit as st
import altair as alt
import numpy as np


data =  pl.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv") #importo il file csv

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




data_dispersion_table = {
    " ": ["Hybrid", "Onsite", "Remote"],  
    "Without Mental Disease": [0.243, 0.230, 0.245],
    "With Mental Disease": [0.757, 0.770, 0.755]
}

# Creazione del DataFrame Polars
d = pl.DataFrame(data_dispersion_table)

# Mostrare la tabella in Streamlit
st.table(d.to_pandas())
st.markdown("""The Pearson's Chi-squared test result is a p-value of 0.5385. There are not enough evidence against the null hypotesis """)

#################################################à

option = st.selectbox(
    "What do you want to compare?",
    ("Job_Role", "Industry"),
)
st.write("You selected:", option)
data2 = data.with_columns([
    pl.when(pl.col("Mental_Health_Condition") == "None").then(0)
      .when(pl.col("Mental_Health_Condition").is_in(["Depression", "Anxiety"])).then(1)
      .alias("Mental_Health_Condition"),
    
    pl.when(pl.col("Stress_Level") == "Low").then(1)
      .when(pl.col("Stress_Level") == "Medium").then(2)
      .when(pl.col("Stress_Level") == "High").then(3)
      .alias("Stress_Level"),
])



# Visualizza il risultato
print(data2)
boxplot_Job_Role = alt.Chart(data).mark_boxplot().encode(
    x=alt.X("Work_Location:N", title="Work Location", axis=alt.Axis(labelAngle=-45)),  # Asse X per appaiamento
    y=alt.Y("Hours_Worked_Per_Week:Q", title="Hours Worked Per Week"),  # Valori numerici sull'asse Y
    color=alt.Color("Work_Location:N", title="Work Location"),  # Colori distintivi per appaiamento
    column=alt.Column("Job_Role:N", title="Job Role")  # Boxplot separati per ogni ruolo
).properties(
    title="Boxplot Appaiati: Hours_Worked_Per_Week per Job Role e Work Location",
    width=150,  # Larghezza di ogni boxplot
    height=400  # Altezza
)
#st.altair_chart(boxplot_Job_Role)

# Calcolo delle percentuali
data_counts = (
    data.group_by(["Job_Role", "Work_Location", "Sleep_Quality"])
    .agg(pl.count())  # Conta le righe
    .rename({"count": "Count"})
)

# Calcolo del totale per ogni combinazione di Job_Role e Work_Location
data_counts = data_counts.join(totals, on=["Job_Role", "Work_Location"])

# Calcola la percentuale
data_counts = data_counts.with_columns(
    (pl.col("Count") / pl.col("Total") * 100).alias("Percentage"))

# Selettore di Job_Role
job_role_selector = alt.selection_multi(fields=["Job_Role"])

# Grafico a barre appaiate
chart = alt.Chart(data_counts).mark_bar().encode(
    x=alt.X("Work_Location:N", title="Work Location"),
    y=alt.Y("Percentage:Q", title="Percentage (%)"),
    color=alt.Color("Sleep_Quality:N", title="Sleep Quality"),
    column=alt.Column("Job_Role:N", title="Job Role", spacing=10),
    tooltip=["Job_Role", "Work_Location", "Sleep_Quality", "Percentage"]
).add_selection(
    job_role_selector
).transform_filter(
    job_role_selector
).properties(
    title="Percentuali di Sleep Quality per Job Role e Work Location",
    width=150,  # Larghezza di ogni barra
    height=400  # Altezza
)