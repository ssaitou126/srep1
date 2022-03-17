import pandas as pd
# import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
# import io


st.subheader('年間水位CSV→HTML変換（単ファイル用）')
# 入力
title = st.text_input('タイトル入力', '')
# アップロード
uploaded_file = st.file_uploader("ファイル選択")
if uploaded_file is not None:
    dfs = pd.read_csv(uploaded_file)
    xaxs = dfs['date']
    ygrf = dfs['suii']
    # 代表値設定
    dfmx = ygrf.max()
    dfme = round(ygrf.mean(),2)
    dfmd = ygrf.quantile(0.5)
    dfmo = ygrf.mode()[0]
    dfqt = ygrf.quantile(0.25)
    dfmn = round(ygrf.min(),2)
    # グラフ描画
    fig = make_subplots(rows=1, cols=2,column_widths=[0.9,0.1],shared_yaxes=True, horizontal_spacing=0.01)
    fig.update_layout(showlegend=False,title=f'{title}水位推移図                  最大値={dfmx}    平均値={dfme}    中間値={dfmd}    最頻値={dfmo}    1stQ={dfqt}    最小値={dfmn}')
    fig.add_trace(go.Scatter(x=xaxs,y=ygrf,name=f'{title}'),row=1,col=1)
    fig.add_trace(go.Violin(y=ygrf, box_visible=True, line_color='blue',meanline_visible=True, fillcolor='deepskyblue', opacity=0.6,name=f'{title}'),row=1,col=2)
    fig.update_xaxes(rangeslider={"visible":True})
    # HTML書き出し
    fig.write_html(f'..//desktop/{title}.html')