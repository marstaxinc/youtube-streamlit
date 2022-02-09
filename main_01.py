from multiprocessing import Condition
from socket import J1939_PGN_ADDRESS_CLAIMED
from turtle import width

from click import style
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd


st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=200, height=300)
# st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

"""
```python
print('Hello')
```
"""

# 折れ線グラフ
if st.checkbox('Show graphs'):
    df = pd.DataFrame(
        np.random.rand(20, 3),
        columns=['a', 'b', 'c'])
    if st.checkbox('Show line chart'):
        st.line_chart(df)
    elif st.checkbox('Show area chart'):
        st.area_chart(df)
    elif st.checkbox('Show bar chart'):
        st.bar_chart(df)

# Map
if st.checkbox('Show map'):
    df = pd.DataFrame(
        np.random.rand(100, 2)/[50, 50]+[+35.69, +139.70],
        columns=['lat', 'lon'])
    st.map(df)

# st.pydeck_chart(pdk.Deck(
#      map_style='mapbox://styles/mapbox/light-v9',
#      initial_view_state=pdk.ViewState(
#          latitude=+35.69,
#          longitude=+139.70,
#          zoom=11,
#          pitch=50,
#      ),
#      layers=[
#          pdk.Layer(
#             'HexagonLayer',
#             data=df,
#             get_position='[lon, lat]',
#             radius=200,
#             elevation_scale=4,
#             elevation_range=[0, 1000],
#             pickable=True,
#             extruded=True,
#          ),
#          pdk.Layer(
#              'ScatterplotLayer',
#              data=df,
#              get_position='[lon, lat]',
#              get_color='[200, 30, 0, 160]',
#              get_radius=200,
#          ),
#      ],
#  ))

# 画像表示(ウィジェット：チェックボックス)
if st.checkbox('Show image'):
    st.write('Display image')
    img = Image.open('./00001.jpg')
    st.image(img, caption='label:1, 00001.jpg')#, use_column_width=True)

# セレクトボックス
option = st.selectbox(
    'あなたの好きな数字を入力してください。',
    list(range(1, 11))
)
'あなたの好きな数字は', option, 'です。'
# テキストボックス
text = st.text_input('あなたの趣味を入力してください。')
'あなたの趣味は', text, 'です。'

# スライダー
condition = st.slider('あなたの調子は？', 0, 100, 90)
'コンディション', condition

