
import streamlit as st
import time

st.title('streamlit 超入門')
st.write('プログレスバー表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムを押しました!')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander1 = st.beta_expander('問い合わせ2')
expander1.write('問い合わせ2の回答')
expander1 = st.beta_expander('問い合わせ3')
expander1.write('問い合わせ3の回答')
