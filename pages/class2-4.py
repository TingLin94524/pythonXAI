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



小學生看得懂的 Streamlit 程式
python
複製
編輯
import streamlit as st

st.title("🎉 數字金字塔 & 箭頭金字塔 小遊戲 🎉")

# 區塊：數字金字塔
st.header("📐 數字金字塔")

num1 = st.number_input("請輸入你想要的金字塔層數（1~10）", min_value=1, max_value=10, step=1)

st.write("你選了", num1, "層金字塔！")
st.write("👇 這是你的數字金字塔：")

# 顯示數字金字塔
for i in range(1, num1 + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(j) + " "
    st.text(line)

st.markdown("---")

# 區塊：箭頭金字塔
st.header("🎯 箭頭金字塔")

num2 = st.number_input("請輸入箭頭的層數（1~10）", min_value=1, max_value=10, step=1, key="arrow")

st.write("你選了", num2, "層箭頭！")
st.write("👇 這是你的箭頭金字塔：")

arrow = ""

# 上半部三角形
for i in range(1, num2 + 1):
    spaces = " " * (num2 - i)
    stars = "*" * (i * 2 - 1)
    arrow += spaces + stars + "\n"

# 下半部直線箭頭柄
for _ in range(num2):
    spaces = " " * (num2 - 1)
    arrow += spaces + "*\n"

# 顯示圖形
st.code(arrow)

st.markdown("✨ 做得好！你完成了兩個金字塔！✨")
🧠 小朋友也能懂的說明
✅ 數字金字塔
這是一座用數字排成的金字塔：

輸入層數 4 時：

複製
編輯
1
1 2
1 2 3
1 2 3 4
✅ 箭頭金字塔
這是一個像箭頭的圖案：

輸入層數 3 時：

markdown
複製
編輯
  *
 ***
*****
  *
  *
  *
🧩 小任務（可以加入遊戲感）：
試試看輸入不同的數字會產生什麼圖案？

看你能不能畫出最高的金字塔！

換成別的符號會怎樣？（例如 #、$）