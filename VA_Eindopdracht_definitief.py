#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
import folium
import streamlit as st
import statsmodels.api as sm


# # GDP Data inladen

# In[2]:


#Inlezen GDP data
GDPData = pd.read_csv("gdp-per-capita-worldbank.csv")


# In[3]:


GDPData2 = pd.read_csv("gdp-per-capita-worldbank.csv")


# In[4]:


GDPData2.rename(columns={'Entity': 'Country'}, inplace = True)


# In[5]:


#Date kolom aanpassen zodat alleen het jaar er staat 
GDPData["Year1"] = pd.to_datetime(GDPData["Year"]).apply(lambda x: x.strftime('%Y'))
print(GDPData["Year1"])


# In[6]:


GDPData['Year'] = GDPData['Year'].astype(int)


# In[7]:


GDPData.rename(columns={'Entity': 'Country'}, inplace = True)


# In[8]:


GDPData.head(10)


# # Big Mac data inladen

# In[9]:


#Inlezen BigMac data

BigMacData = pd.read_csv("BigmacPrice.csv")


# In[10]:


BigMacData.head()


# In[11]:


BigMacData.rename(columns={'name': 'Country', 'dollar_price': 'Dollar price'}, inplace = True)


# In[12]:


#Date kolom aanpassen zodat alleen het jaar er staat
BigMacData["Year"] = pd.to_datetime(BigMacData["date"]).apply(lambda x: x.strftime('%Y'))
print(BigMacData["Year"])


# In[13]:


BigMacData['Year'] = BigMacData['Year'].astype(int)


# In[14]:


BigMacData.rename(columns={'name': 'Country'}, inplace = True)


# In[15]:


BigMacData.info()


# In[16]:


BigMacData.isna().sum().sum()


# In[17]:


BigMacData.set_index('Year')


# In[18]:


GDPData2['Year'].max()


# In[19]:


GDPData2['Year'].min()


# In[20]:


BigMacData['date'].max()


# In[21]:


BigMacData['date'].min()


# # Geodata inladen

# In[22]:


#Inlezen GDP data
GeoData = pd.read_csv("world_country_and_usa_states_latitude_and_longitude_values.csv")


# In[23]:


GeoData.rename(columns={'country': 'Country'}, inplace = True)


# # GDP en BigMac data merge

# In[24]:


#Merge van de GDP en Bigmac datasets
GDPBigMacMerge = GDPData.merge(BigMacData, on = 'Country')


# In[ ]:





# In[ ]:





# In[ ]:





# # GeoData merge

# In[25]:


GDPGeoBigMacMerged = GDPBigMacMerge.merge(GeoData, on = 'Country')


# In[26]:


GDPGeoBigMacMerged.columns


# In[27]:


GDPGeoBigMacMerged = GDPGeoBigMacMerged[['Country','Code', 'GDP per capita, PPP (constant 2017 international $)', 'local_price', 'Year_y', 'Dollar price', 'latitude', 'longitude']]


# # plots

# In[28]:


BigMacData.Country.unique()


# In[29]:


value_list = ["United States", "Belgium", "Netherlands", "Mexico", "Brazil", "China"]
boolean_series = GDPGeoBigMacMerged.Country.isin(value_list)
filtered_GDPGeoBigMacMerged = GDPGeoBigMacMerged[boolean_series]
filtered_GDPGeoBigMacMerged.rename(columns={'Year_y': 'Year', 'GDP per capita, PPP (constant 2017 international $)': 'GDP per capita'}, inplace = True)


# In[30]:


filtered_GDPGeoBigMacMerged_sorted = filtered_GDPGeoBigMacMerged.sort_values('Year', ascending=True)


# In[ ]:





# In[ ]:





# In[31]:


fig100 = px.bar(
data_frame = filtered_GDPGeoBigMacMerged_sorted,
y = 'Dollar price',
x = 'Country',
title = 'Big Mac prijs per land',
color = 'Dollar price',
animation_frame = 'Year',
animation_group = 'Country')
fig100.update_layout(yaxis_range=[0,12])
fig100.update_xaxes(categoryorder='array', categoryarray= ["United States", "Belgium", "Netherlands", "Mexico", "Brazil", "China"])
fig100['layout'].pop('updatemenus')


# In[32]:


fig101 = px.scatter(
data_frame = filtered_GDPGeoBigMacMerged_sorted,
y = 'Dollar price',
x = 'Country',
title = 'Big Mac prijs per land',
animation_frame = 'Year',
animation_group = 'Country', 
width=1100, height=600)
fig101.update_layout(yaxis_range=[0,12])
fig101.update_xaxes(categoryorder='array', categoryarray= ["United States", "Belgium", "Netherlands", "Mexico", "Brazil", "China"])
fig101['layout'].pop('updatemenus')


# In[33]:


fig102 = px.choropleth(
    GDPGeoBigMacMerged, 
    locations="Code",
    color="Dollar price", 
    hover_name="Country", 
    color_continuous_scale=px.colors.sequential.Plasma,
    animation_frame = 'Year_y',
    animation_group = 'Country')
fig102['layout'].pop('updatemenus')


# # Figuur maken

# In[34]:


fig104 = px.scatter(filtered_GDPGeoBigMacMerged_sorted, x='GDP per capita', y ='Dollar price', color='Country', trendline="ols",
animation_frame = 'Year',
animation_group = 'Year') 
fig104.update_layout(yaxis_range=[0,12])


# In[35]:


fig105 = px.scatter(filtered_GDPGeoBigMacMerged_sorted, x='GDP per capita', y ='Dollar price', trendline="ols",
animation_frame = 'Year',
animation_group = 'Country') 
fig105.update_layout(yaxis_range=[0,12])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[36]:


fig103 = px.line(
data_frame = BigMacData,
x = 'Year',
y = 'Dollar price',
title = 'Big Mac price ($) in US', color='Country')


# In[ ]:





# In[ ]:





# # Streamlit 

# In[37]:


header = st.container()


# In[38]:


with header:
    st.title('BigMac data blog')
    st.text('In deze blog gaan wij kijken naar de prijs van een BigMac uitgezet over tijd en of er een correlatie is met GDP per capita')


# In[56]:


BigMac_data_streamlit_table = BigMacData[['date', 'currency_code', 'Country', 'local_price', 'dollar_ex', 'Dollar price', 'Year']]
BigMac_data_streamlit_table.columns = ['Date', 'Currency code', 'Country', 'Local price', 'Dollar ex', 'Dollar price', 'Year']
value_list = [2000, 2001, 2002, 2003, 2004, 2005,2006, 2007, 2008, 2009, 2010, 2011,2012, 2013, 2014, 2015, 2016,2017, 2018, 2019,2020, 2021, 2022]
boolean_series = BigMac_data_streamlit_table.Year.isin(value_list)
BigMac_data_streamlit_table = BigMac_data_streamlit_table[boolean_series]
BigMac_data_streamlit_table.head(30)


# In[57]:


st.header('Een eerste kijk in de data')
st.text("Deze eerste dataset zijn de BigMac prijzen per land per jaar")
st.dataframe(BigMac_data_streamlit_table)


# In[ ]:





# In[ ]:





# In[ ]:





# # GDP tabel naar st

# In[41]:


st.subheader('GDP dataset')
st.text("Deze dataset bevat de GDP per capita van verschillende landen")


# In[42]:


st.dataframe(GDPData)


# # Geo data naar st

# In[43]:


st.subheader('Geo  dataset')
st.text("Deze dataset bevat de latitudes en longitudes van verschillende landen")


# In[44]:


st.dataframe(GeoData)


# # Gemergde data

# In[58]:


st.subheader('Gemergde dataset')
st.text("Deze dataset bevat de BigMac, GDP en Geo data")


# In[46]:


st.dataframe(GDPGeoBigMacMerged)


# # Plots in st

# In[47]:


st.plotly_chart(fig100)


# In[48]:


st.plotly_chart(fig101)


# In[49]:


st.plotly_chart(fig102)


# In[50]:


st.plotly_chart(fig103)


# In[51]:


st.plotly_chart(fig104) 


# In[52]:


st.plotly_chart(fig105) 


# In[ ]:





# In[ ]:





# In[ ]:




