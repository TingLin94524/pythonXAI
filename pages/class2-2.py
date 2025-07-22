import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)

st.write(f"你輸入的數字是: {number}")

score = st.number_input("請輸入分數", step=1, min_value=0, max_value=100)
if score >= 90:
    st.write("A")
elif score >= 80 and score < 90:
    st.write("B")
elif score >= 70 and score < 80:
    st.write("c")
elif score >= 60 and score < 70:
    st.write("D")
elif score < 60:
    st.write_stream("F")

st.button("點我")

if st.button("點我5"):
    st.balloons()
