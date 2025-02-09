import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv('edible_plant.csv')
#wide表示
st.set_page_config(layout="wide")
#csvをheaderありで読み込む
df= load_data()

#yearでフィルタリング
df = df[(df['spe'] == "ナミアゲハ") | (df['spe'] == "キアゲハ(日本亜種)")]

df = pd.DataFrame(df)
#年度でグループ化
#df_grouped = df.groupby('year').size().reset_index(name='count')

#線グラフを表示
#st.line_chart(df_grouped.set_index('year'))
#データフレームを表示
new_df = df[['spe', 'plant_spe']]
st.write(new_df)