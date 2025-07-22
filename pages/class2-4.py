import streamlit as st

st.write("##數字金字塔")
num1 = st.number_input("請輸入一個數字", step=1, min_value=1, max_value=100)
# for i in range(1, num1 + 1):
#     for i in range(1, i + 1):
#         st.write(str(i), end=" ")

st.write("### 這是數字金字塔")
for i in range(1, num1 + 1):
    st.write(str(i) * i)

st.write("##箭頭金字塔")
arrow = ""
num2 = st.number_input("請輸入箭頭的層數", step=1, min_value=1)
# for i in range(1, num2 + 1):
# print(" " * (num2 - i) + "*" * (i * 2 - 1))
for i in range(1, num2 + 1):
    # print(" " * (num2 - 1) + "*")
    arrow = arrow + (" " * (num2 - i) + "*" * (i * 2 - 1) + "\n")
for i in range(num2):
    arrow = arrow + (" " * (num2 - 1) + "*" + "\n")
st.write(
    f"""
```
箭頭金字塔:
{arrow}
```
"""
)

L = [1, 2, 3, 4, 5]
