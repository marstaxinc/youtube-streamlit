from multiprocessing import Condition
from socket import J1939_PGN_ADDRESS_CLAIMED
from turtle import width

from click import style
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd


st.title('streamlit 超入門')

st.write('Interactive widgets')
st.sidebar.write('Side bar')

# レイアウト*********************************************************************
# テキストボックス
text_s = st.sidebar.text_input('あなたの趣味を入力してください。')
'あなたの趣味は', text_s, 'です。'

# スライダー
condition_s = st.sidebar.slider('あなたの調子は？', 0, 100, 90)
'コンディション', condition_s