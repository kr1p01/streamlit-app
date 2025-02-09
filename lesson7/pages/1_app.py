import streamlit as st
import random 

num_count = st.number_input('繰り返し回数',min_value = 0)

if st.button('generate number'):
    for i in range(num_count):
        random_num = random.randint(1,100)
        st.write(random_num)