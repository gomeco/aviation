#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[110]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_aircraft_passenger_mixed.csv'


# In[111]:


aircraf_movements_passenger_mixed = pd.read_csv(url)


# In[112]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_aircraft_cargo.csv'


# In[113]:


aircraft_movements_cargo = pd.read_csv(url)


# In[114]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_european.csv'


# In[115]:


movements_main_european = pd.read_csv(url)


# In[116]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_intercontinental.csv'


# In[117]:


movements_main_intercontinental = pd.read_csv(url)


# In[118]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_airlines.csv'


# In[119]:


movements_main_airlines = pd.read_csv(url)


# In[122]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/air_traffic.csv'


# In[123]:


air_traffic = pd.read_csv(url)


# In[125]:


#Hoofdtitel


# In[126]:


st.title('Schiphol Data Analyse')


# In[127]:


#introductie


# In[128]:


st.write('In deze data analyse gaan we in op de volume en CO2-uitstoot van vluchten bij Schiphol')


# In[129]:


#Eerste titel


# In[130]:


st.title('Dataverkenning')


# In[131]:


#Stukje begeleiding


# In[132]:


st.write('We beginnen eerst met een stukje dataverkenning')


# In[133]:


#grafiek 


# In[ ]:





# In[ ]:





# In[134]:


#conclusie


# In[135]:


keuze = air_traffic.columns


# In[136]:


keuze = keuze[2:]


# In[137]:


st.title("Selecteer categorie")
line = st.selectbox("Kies categorie:", keuze)
jaar = "Air Transport Movements year"
maand = "Air Transport Movements month"
kleurkeuze = st.radio("Visualisatie op baseren op:", [jaar, maand])
fig = px.line(air_traffic, x="Air Transport Movements year", y=line, color=kleurkeuze
                ,
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(line))
st.plotly_chart(fig, use_container_width=True)


# In[ ]:




