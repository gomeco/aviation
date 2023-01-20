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


# In[191]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_aircraft_cargo.csv'


# In[192]:


aircraft_movements_cargo = pd.read_csv(url)


# In[160]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_european.csv'


# In[169]:


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


# In[ ]:





# In[ ]:





# In[133]:


#grafiek 


# In[135]:


keuze = air_traffic.columns


# In[140]:


keuze = keuze[3:]


# In[147]:


air_traffic = air_traffic[air_traffic["Air Transport Movements month"]!='Total']


# In[148]:


#df = df[df.line_race != 0]


# In[205]:


line = st.selectbox("Kies categorie:", keuze)
#options = st.multiselect('Kies jaar', air_traffic['Air Transport Movements year'].unique())
line2 = st.selectbox("Kies jaar:", air_traffic['Air Transport Movements year'].unique())


fig = px.line(air_traffic[air_traffic['Air Transport Movements year']==line2], x="Air Transport Movements month", y=line, color='Air Transport Movements year'
                ,
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(line))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[134]:


#conclusie


# In[ ]:


st.write('we kunnen hier verschillende soorten conclusies uit trekken in een oogopslag. Zoals het effect van de Corona pandemie.')


# In[ ]:


#Titel


# In[156]:


st.title('Bewegingen per land (Europa)')


# In[ ]:


#grafiek


# In[177]:


line = st.selectbox("Kies land:", movements_main_european['country'].unique())

fig = px.bar(movements_main_european[movements_main_european['country']==line],x='country', y='total_movements', color='country',
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(line))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[ ]:


#conclusie


# In[178]:


st.write('Hier kunnen we zien wat de jaarlijkse aantal vluchten waren voor elk van de hoofdlanden binnen de EU')


# In[ ]:


#grafiek


# In[202]:


line = st.selectbox("Kies land:", movements_main_intercontinental['country'].unique())

fig = px.bar(movements_main_intercontinental[movements_main_intercontinental['country']==line],x='country', y='total_movements', color='country',
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(line))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[181]:


st.title('Aantal bewegingen per vliegtuigtype (passagiers)')


# In[188]:


line = st.selectbox("Kies type:", aircraf_movements_passenger_mixed['type'].unique())

fig = px.bar(aircraf_movements_passenger_mixed[aircraf_movements_passenger_mixed['type']==line],x='type', y='total_movements', color='type',
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(line))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[196]:


st.title('Aantal bewegingen per vliegtuigtype (cargo)')


# In[193]:


line = st.selectbox("Kies type:", aircraft_movements_cargo['type'].unique())

fig = px.bar(aircraft_movements_cargo[aircraft_movements_cargo['type']==line],x='type', y='total_movements', color='type',
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(line))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[206]:


#line = st.selectbox("Kies vliegmaatschappij:", movements_main_airlines['airline'].unique())
options = st.multiselect(
    'What are your favorite colors',movements_main_airlines['airline'].unique())

if options == []:
    fig = px.bar(movements_main_airlines,x='airline', y='total', color='airline',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(movements_main_airlines[movements_main_airlines['airline']==[options]],x='airline', y='total', color='airline',
                   #labels={
                    #        "salary_in_euro": "Salaris in Euro",
                     #       "experience_level": "Werkervaring"                       #  },
                      title="Grafiek voor %s"%(line))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[ ]:




