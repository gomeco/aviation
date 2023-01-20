#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_aircraft_passenger_mixed.csv'


# In[3]:


aircraf_movements_passenger_mixed = pd.read_csv(url)


# In[4]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_aircraft_cargo.csv'


# In[5]:


aircraft_movements_cargo = pd.read_csv(url)


# In[6]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_european.csv'


# In[7]:


movements_main_european = pd.read_csv(url)


# In[8]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_intercontinental.csv'


# In[9]:


movements_main_intercontinental = pd.read_csv(url)


# In[10]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/movements_main_airlines.csv'


# In[11]:


movements_main_airlines = pd.read_csv(url)


# In[12]:


url = 'https://raw.githubusercontent.com/gomeco/aviation/main/air_traffic.csv'


# In[13]:


air_traffic = pd.read_csv(url)


# In[14]:


#Hoofdtitel


# In[15]:


st.title('Schiphol Data Analyse')


# In[16]:


#introductie


# In[17]:


st.write('In deze data analyse gaan we in op de volume en CO2-uitstoot van vluchten bij Schiphol')


# In[18]:


#Eerste titel


# In[19]:


st.title('Dataverkenning')


# In[20]:


#Stukje begeleiding


# In[21]:


st.write('We beginnen eerst met een stukje dataverkenning')


# In[ ]:





# In[ ]:





# In[22]:


#grafiek 


# In[23]:


keuze = air_traffic.columns


# In[24]:


keuze = keuze[3:]


# In[25]:


air_traffic = air_traffic[air_traffic["Air Transport Movements month"]!='Total']


# In[26]:


#df = df[df.line_race != 0]


# In[27]:


line = st.selectbox("Kies categorie:", keuze)
options = st.multiselect('Kies jaar', air_traffic['Air Transport Movements year'].unique())
#options = st.multiselect('Kies land',movements_main_european['country'].unique())

if options == []:

    fig = px.line(air_traffic, x="Air Transport Movements month", y=line, color='Air Transport Movements year'
                    ,
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.line(air_traffic[air_traffic["Air Transport Movements year"].isin(options)], x="Air Transport Movements month", y=line, color='Air Transport Movements year'
                    ,
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor %s"%(options))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[28]:


#conclusie


# In[29]:


st.write('we kunnen hier verschillende soorten conclusies uit trekken in een oogopslag. Zoals het effect van de Corona pandemie.')


# In[30]:


#Titel


# In[31]:


st.title('Bewegingen per land (Europa)')


# In[32]:


#grafiek


# In[33]:


options2 = st.multiselect('Kies land',movements_main_european['country'].unique())

if options2 == []:
    fig = px.bar(movements_main_european,x='country', y='total_movements', color='country',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(movements_main_european[movements_main_european['country'].isin(options2)],x='country', y='total_movements', color='country',
                #labels={
                 #        "salary_in_euro": "Salaris in Euro",
                  #       "experience_level": "Werkervaring"
                   #  },
                    title="Grafiek voor %s"%(options2))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[34]:


#conclusie


# In[35]:


st.write('Hier kunnen we zien wat de jaarlijkse aantal vluchten waren voor elk van de hoofdlanden binnen de EU')


# In[36]:


#grafiek


# In[37]:


st.title('Bewegingen per land (Intercontinentaal)')


# In[38]:


options3 = st.multiselect(
    'Kies land',movements_main_intercontinental['country'].unique())

if options3 == []:
    fig = px.bar(movements_main_intercontinental,x='country', y='total_movements', color='country',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(movements_main_intercontinental[movements_main_intercontinental['country'].isin(options3)],x='country', y='total_movements', color='country',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor %s"%(options3))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[39]:


st.title('Aantal bewegingen per vliegtuigtype (passagiersvoertuigen)')


# In[40]:


options4 = st.multiselect(
    'Kies type',aircraf_movements_passenger_mixed['type'].unique())

if options4 == []:
    fig = px.bar(aircraf_movements_passenger_mixed,x='type', y='total_movements', color='type',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(aircraf_movements_passenger_mixed[aircraf_movements_passenger_mixed['type'].isin(options4)],x='type', y='total_movements', color='type',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor %s"%(options4))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[41]:


st.title('Aantal bewegingen per vliegtuigtype (cargo)')


# In[42]:


options5 = st.multiselect(
    'Kies type',aircraft_movements_cargo['type'].unique())

if options5 == []:

    fig = px.bar(aircraft_movements_cargo,x='type', y='total_movements', color='type',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(aircraft_movements_cargo[aircraft_movements_cargo['type'].isin(options5)],x='type', y='total_movements', color='type',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor %s"%(options5))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[43]:


st.title('Aantal bewegingen per vliegmaatschappij')


# In[44]:


#line = st.selectbox("Kies vliegmaatschappij:", movements_main_airlines['airline'].unique())
options6 = st.multiselect(
    'Kies vliegmaatschappij',movements_main_airlines['airline'].unique())

if options6 == []:
    fig = px.bar(movements_main_airlines,x='airline', y='total', color='airline',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(movements_main_airlines[movements_main_airlines['airline'].isin(options6)],x='airline', y='total', color='airline',
                   #labels={
                    #        "salary_in_euro": "Salaris in Euro",
                     #       "experience_level": "Werkervaring"                       #  },
                      title="Grafiek voor %s"%(options6))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[45]:


st.title('CO2 verbruik per voertuigtype (passagiersvoertuigen)')


# In[46]:


st.write('''Aannames: 
- Om 1 kg massa voor 1000km te kunnen laten vliegen, is er 0,2kg brandstof nodig.
(Bron: https://digitalcollection.zhaw.ch/bitstream/11475/1896/6/Steinegger_Fuel_Economy_as_a_Function_of_Weight_and_Distance_v1-1.pdf
)
- Er zijn gemiddeld 174 passagiers per vliegtuig.
(Bron: https://www.schiphol.nl/en/download/b2b/1646906945/3RCcnR7Wb7Pmouwd1qZnEB.pdf)
- "3The combustion of 1 kilogram (kg) of jet fuel in an aircraft engine produces 3.16 kg of carbon dioxide (CO2)."
(Bron: https://www.iata.org/contentassets/922ebc4cbcd24c4d9fd55933e7070947/icop_faq_general-for-airline-participants.pdf
         ''')


# In[47]:


test = 0,2*aircraf_movements_passenger_mixed['average_mtow_ton']*1000*3


# In[48]:


aircraf_movements_passenger_mixed['CO2 1000km'] = test[1]


# In[49]:


test2 = 0,2*aircraf_movements_passenger_mixed['average_mtow_ton']*1000*3*2


# In[50]:


aircraf_movements_passenger_mixed['CO2 2000km'] = test2[1]


# In[51]:


test3 = 0,2*aircraf_movements_passenger_mixed['average_mtow_ton']*1000*3*3


# In[52]:


aircraf_movements_passenger_mixed['CO2 3000km'] = test3[1]


# In[53]:


test4 = 0,2*aircraf_movements_passenger_mixed['average_mtow_ton']*1000*3*4


# In[54]:


aircraf_movements_passenger_mixed['CO2 4000km'] = test4[1]


# In[55]:


test5 = 0,2*aircraf_movements_passenger_mixed['average_mtow_ton']*1000*3*5


# In[56]:


aircraf_movements_passenger_mixed['CO2 5000km'] = test5[1]


# In[57]:


options7 = st.multiselect(
    'Kies type vliegtuig',aircraf_movements_passenger_mixed['type'].unique())

if options7 == []:
    fig = px.bar(aircraf_movements_passenger_mixed,x='type', y='CO2 1000km', color='type',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor alle")
else:
    fig = px.bar(aircraf_movements_passenger_mixed[aircraf_movements_passenger_mixed['type'].isin(options7)],x='type', y='CO2 1000km', color='type',
                    #labels={
                     #        "salary_in_euro": "Salaris in Euro",
                      #       "experience_level": "Werkervaring"
                       #  },
                        title="Grafiek voor %s"%(options7))
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[58]:


st.title('CO2 calculator per type(passagiersvliegtuigen)')


# In[59]:


line2 = st.selectbox("Kies type:", aircraf_movements_passenger_mixed['type'].unique())
selection = aircraf_movements_passenger_mixed[aircraf_movements_passenger_mixed['type']==line2]

number = st.number_input('Insert a number')
calculation = (selection['CO2 1000km']/1000*number/174).to_list()
if calculation != []:
    st.write('Uw CO2 uitstoot door het vliegen voor %s km met de %s is: %s kg CO2 per persoon'%(number, line2, calculation[0]))


# In[60]:


st.title('CO2 calculator per type(cargovliegtuigen)')


# In[61]:


test_cargo = 0,2*aircraf_movements_passenger_mixed['average_mtow_ton']*1000*3
aircraft_movements_cargo['CO2 1000km'] = test_cargo[1]


# In[62]:


line3 = st.selectbox("Kies type:", aircraft_movements_cargo['type'].unique())
selection = aircraft_movements_cargo[aircraft_movements_cargo['type']==line3]

number = st.number_input('Insert a number')
calculation = (selection['CO2 1000km']/1000*number/174).to_list()
if calculation != []:
    st.write('Uw CO2 uitstoot door het vliegen voor %s km met de %s is: %s kg CO2 per persoon'%(number, line3, calculation[0]))


# In[63]:


st.title('CO2 calculator per bestemming (passagiers en cargo) europa')


# In[64]:


vliegtuig_gemiddelde = pd.DataFrame()


# In[65]:


vliegtuig_gemiddelde['verbruik per km'] = aircraf_movements_passenger_mixed['CO2 1000km']/1000
vliegtuig_gemiddelde['type'] = aircraf_movements_passenger_mixed['type']
vliegtuig_gemiddelde['aantal keer'] = aircraf_movements_passenger_mixed['total_movements']
weighted_average_passenger = (vliegtuig_gemiddelde['verbruik per km']*aircraf_movements_passenger_mixed['total_movements']).sum()/aircraf_movements_passenger_mixed['total_movements'].sum()


# In[66]:


vliegtuig_gemiddelde['verbruik per km'] = aircraft_movements_cargo['CO2 1000km']/1000
vliegtuig_gemiddelde['type'] = aircraft_movements_cargo['type']
vliegtuig_gemiddelde['aantal keer'] = aircraft_movements_cargo['total_movements']
weighted_average_cargo = (vliegtuig_gemiddelde['verbruik per km']*aircraft_movements_cargo['total_movements']).sum()/aircraft_movements_cargo['total_movements'].sum()


# In[67]:


print(weighted_average_passenger)
print(weighted_average_cargo)


# In[68]:


line4 = st.selectbox("Selecteer een bestemming:", movements_main_european['country'].unique())
selection = movements_main_european[movements_main_european['country']==line4]
selection_passenger = selection['distance'].to_list()
selection_cargo = selection['distance'].to_list()
#number = st.number_input('Insert a number')
#calculation = (selection['CO2 1000km']/1000*number/174).to_list()
if selection_passenger and selection_cargo != []:
    st.write('''Uw CO2 uitstoot door het vliegen naar %s is: 
             -Passagier %s kg CO2 per persoon
             -Cargo %s kg CO2 per persoon'''%(line4, selection_passenger[0]*weighted_average_passenger/174, selection_cargo[0]*weighted_average_cargo/174))
    


# In[69]:


st.title('CO2 calculator per bestemming (passagiers en cargo) Intercontinentaal')


# In[71]:


st.title('CO2 calculator per bestemming (passagiers en cargo) Intercontinentaal')


# In[70]:


line5 = st.selectbox("Selecteer een bestemming:", movements_main_intercontinental['country'].unique())
selection = movements_main_intercontinental[movements_main_intercontinental['country']==line5]
selection_passenger = selection['distance'].to_list()
selection_cargo = selection['distance'].to_list()
#number = st.number_input('Insert a number')
#calculation = (selection['CO2 1000km']/1000*number/174).to_list()
if selection_passenger and selection_cargo != []:
    st.write('''Uw CO2 uitstoot door het vliegen naar %s is: 
             -Passagier %s kg CO2 per persoon
             -Cargo %s kg CO2 per persoon'''%(line4, selection_passenger[0]*weighted_average_passenger/174, selection_cargo[0]*weighted_average_cargo/174))
    

