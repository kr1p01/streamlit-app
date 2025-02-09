import streamlit as st
import random
if 'sum' not in st.session_state:
    st.session_state.sum = 0
uranai = {1 : "凶",
          2 : "吉",
          3 : "大吉"}
random_view = False

st.title("乱数生成")
count = st.number_input('生成回数',step=1)
min_number = -100
max_number = 100
start_number,end_number = st.slider('範囲',min_value=min_number,max_value=max_number,value=(min_number,max_number))
if st.checkbox('結果をひとつづつ表示'):
    random_view = True
sum_mini = 0
if st.button("生成"):
    for i in range(count):
        random_num = random.randint(start_number,end_number)
        if random_view:
            st.write(random_num)
        sum_mini += random_num
    st.write(f"合計：{sum_mini}")
st.session_state.sum += sum_mini
st.write(f"積算合計：{st.session_state.sum}")

if st.button("おみくじ"):
    uranai_num = random.randint(1,3)
    st.write(uranai[uranai_num])