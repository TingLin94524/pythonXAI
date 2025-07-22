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

修正後、適合小學生的版本
python
複製
編輯
import streamlit as st

st.title("🎯 分數等級小工具")

# 輸入一個數字（範例練習）
number = st.number_input("請輸入一個數字（0~100）", step=1, min_value=0, max_value=100)
st.write(f"你輸入的數字是：{number}")

# 分隔線
st.markdown("---")

# 輸入分數
score = st.number_input("請輸入你的分數", step=1, min_value=0, max_value=100, key="score")

# 判斷分數等級
if score >= 90:
    st.write("你的等級是：🅰️ A（超棒！）")
elif score >= 80:
    st.write("你的等級是：🅱️ B（很不錯！）")
elif score >= 70:
    st.write("你的等級是：🅲 C（加油～）")
elif score >= 60:
    st.write("你的等級是：🅳 D（要努力囉）")
else:
    st.write("你的等級是：❌ F（不要氣餒，再試一次！）")

# 分隔線
st.markdown("---")

# 按鈕：點我
if st.button("點我"):
    st.write("你點了按鈕 👍")

# 按鈕：點我5（有氣球特效）
if st.button("點我5 🎈"):
    st.balloons()
    st.write("🎉 你觸發了氣球特效！")
🧠 小學生也能懂的說明
這個小程式會做什麼？
輸入一個數字（像是 10、20…）

輸入一個分數（例如 85）

它會告訴你成績是：

A：超棒！

B：不錯喔

C：還行，要努力

D：再加油

F：沒關係，再挑戰！

還有按鈕可以玩！ 有一個按下會冒出🎈氣球！

🛠️ 修正重點
原來的寫法	問題	修正建議
st.write_stream("F")	❌ st.write_stream() 是不存在的函數	✅ 改為 st.write("F")
"c" 小寫	不一致的格式	改成 "C" 統一為大寫
沒有加說明	小學生看不懂	加上中文提示與 emoji 提高親和力