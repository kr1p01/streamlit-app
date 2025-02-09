import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv('toshokan.csv')
#wide表示
st.set_page_config(layout="wide")
#csvをheaderありで読み込む
df= load_data()

#dfのyearの最小値と最大値を取得
min_year = df['year'].min()
max_year = df['year'].max()

start_year,end_year = st.slider('年度',min_value=min_year,max_value=max_year,value=(min_year,max_year))

#yearでフィルタリング
df = df[(df['year'] >=start_year) & (df['year'] <= end_year)]

#年度でグループ化
df_grouped = df.groupby('year').size().reset_index(name='count')

#線グラフを表示
st.line_chart(df_grouped.set_index('year'))
#データフレームを表示
st.write(df)