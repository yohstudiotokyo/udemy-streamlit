import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.dataframe(df.style.highlight_max(axis=0))
# st.write(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))
# st.bar_chart(df)
# st.map(df)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# st.write('Display Image')

# option = st.selectbox(
#     '好きな数字',
#     list(range(1, 11))
# )

# 'あなたが好きな数字は、', option, 'です'

# text = st.sidebar.text_input('あなたの趣味は？')
# 'あなたの趣味は、', text, 'です'

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション: ', condition


st.write('プログレスバーの表示')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')


# if st.checkbox('Show Image'):
#     img = Image.open('carp.png')
#     st.image(img, caption='carp boy', use_column_width=True)
