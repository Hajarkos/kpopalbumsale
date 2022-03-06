import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
st.title('4th Gen Kpop Group Album Sale')

st.header("Who is Kpop 4th Generation?")

st.caption("Kpop 4th Generation refer to those korean idol group who made their debut around 2018 until now. These groups are shinning under the influence of Internet storm in kpop plus they are actually a bit noticeable also in the international market way faster than 3rd gen kpop groups. The group involve in this study are IZONE, Loona, ITZY,Stray Kids, TXT, Ateez, Everglow, (G)I-dle, Treasure, Cravity and Verivery")

df = pd.read_csv('Kpop group album sales.csv') 
df['sales'].replace(',','',regex= True,inplace=True)
df['sales']= pd.to_numeric(df['sales'])
df['peak_chart'] = df['peak_chart'].astype(object)
df_sale= df.groupby(['Artist','country','title'])['sales'].sum()
bg = df[(df['Artist'] == "Ateez" )| (df['Artist'] == "Cravity" )| (df['Artist'] == "TXT" )| (df['Artist'] == "Stray Kids" )| (df['Artist'] == "Treasure" )| (df['Artist'] == "Verivery" )]
gg = df[(df['Artist'] == "IZONE" )| (df['Artist'] == "Everglow" )| (df['Artist'] == "ITZY" )| (df['Artist'] == "Loona" )| (df['Artist'] == "(G)I-dle" )]
sale_gg = gg.groupby(['Artist','country','title'])['sales'].sum()
sale_bg = bg.groupby(['Artist','country','title'])['sales'].sum()
kor_bg_album = bg[bg['country']=='KOR']
kor_gg_album = gg[gg['country']=='KOR']
jpn_bg_album = bg[bg['country']=='JPN']
jpn_gg_album = gg[gg['country']=='JPN']

option = st.sidebar.selectbox(
     'Select Boy/Girl group',
     ('Choose here....','Boy group','Girl group'))

st.write('Result show total sale for:', option)

if option =='Choose here....': 
  st.write('Please select group in the sidebar')

elif option =='Boy group': 
  sale_bg = bg.groupby(['Artist','country','title'])['sales'].sum()
  st.dataframe(sale_bg)

elif option =='Girl group': 
  sale_gg = gg.groupby(['Artist','country','title'])['sales'].sum()
  st.dataframe(sale_gg)

option = st.sidebar.selectbox(
     'Select country',
     ('Choose here....','Boy Group/Korean Album','Boy Group/Japan Album','Girl Group/Korean Album','Girl Group/Japan Album'))

st.write('Result show total sale for:', option)

if option =='Choose here....': 
  image2 = Image.open('arrow.jpg')
  st.image(image2)

elif option =='Boy Group/Korean Album': 
  kor_bg_album = bg[bg['country']=='KOR']
  st.dataframe(kor_bg_album)

elif option =='Boy Group/Japan Album': 
  jpn_bg_album = bg[bg['country']=='JPN']
  st.dataframe(jpn_bg_album)

elif option =='Girl Group/Korean Album': 
  kor_gg_album = gg[gg['country']=='KOR']
  st.dataframe(kor_gg_album)

elif option =='Girl Group/Japan Album': 
  jpn_gg_album = gg[gg['country']=='JPN']
  st.dataframe(jpn_gg_album)