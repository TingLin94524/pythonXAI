一、比較運算子：比一比，看誰大誰小！
比較方式 意思是？ 範例 結果
== 一樣嗎？ 1 == 2 ❌ False
!= 不一樣嗎？ 1 != 2 ✅ True

>             比它大？	1 > 2	❌ False
>
> < 比它小？ 1 < 2 ✅ True
> = 大或一樣？ 1 >= 2 ❌ False
> <= 小或一樣？ 1 <= 2 ✅ True

🔴 二、邏輯運算子：真的還是假的？
運算子 中文意思 範例 結果
not 不是 not True ❌ False
and 而且 True and False ❌ False
or 或是 True or False ✅ True

🎯 小提醒：

and 是「而且」：兩個都要對，才是真的。

or 是「或是」：有一個對，就是真的。

not 是「反過來」：原本對的就變錯，原本錯的就變對。

🔐 三、練習：密碼驗證遊戲
python
複製
編輯
password = input("請輸入密碼: ")

if password == "1234":
print("密碼正確")
else:
print("密碼錯誤")
📌 如果你輸入 1234，會出現「密碼正確」，否則會說「密碼錯誤」。

🧑‍💻 四、歡迎不同的人
python
複製
編輯
if password == "1234":
print("歡迎 Ray")
elif password == "5678":
print("歡迎 Mike")
elif password == "abcd":
print("歡迎 Alise")
else:
print("密碼錯誤")
💡 不同密碼代表不同的人，像是：

輸入 1234 ➜ 歡迎 Ray

輸入 abcd ➜ 歡迎 Alise

輸入錯誤 ➜ 密碼錯誤

📅 五、閏年判斷小幫手
python
複製
編輯
year = int(input("請輸入年份: "))

if year % 4 == 0:
if year % 100 == 0:
if year % 400 == 0:
print(f"{year} 是閏年")
else:
print(f"{year} 不是閏年")
else:
print(f"{year} 是閏年")
else:
print(f"{year} 不是閏年")
🌟 什麼是閏年？
每 4 年會多一天（2 月 29 日），叫做「閏年」！

判斷方法 是不是閏年？
被 4 整除 可能是閏年 ✅
被 100 整除 不一定 ❌
被 400 整除 一定是閏年 ✅

🧪 範例：

2000 是閏年 ✅

1900 不是閏年 ❌

2024 是閏年 ✅
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

if st.button("點我 5"):
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

# 按鈕：點我 5（有氣球特效）

if st.button("點我 5 🎈"):
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

還有按鈕可以玩！ 有一個按下會冒出 🎈 氣球！

🛠️ 修正重點
原來的寫法 問題 修正建議
st.write_stream("F") ❌ st.write_stream() 是不存在的函數 ✅ 改為 st.write("F")
"c" 小寫 不一致的格式 改成 "C" 統一為大寫
沒有加說明 小學生看不懂 加上中文提示與 emoji 提高親和力
import streamlit as st

st.write("##數字金字塔")
num1 = st.number_input("請輸入一個數字", step=1, min_value=1, max_value=100)

# for i in range(1, num1 + 1):

# for i in range(1, i + 1):

# st.write(str(i), end=" ")

st.write("### 這是數字金字塔")
for i in range(1, num1 + 1):
st.write(str(i) \* i)

st.write("##箭頭金字塔")
arrow = ""
num2 = st.number_input("請輸入箭頭的層數", step=1, min_value=1)

# for i in range(1, num2 + 1):

# print(" " _ (num2 - i) + "_" _ (i _ 2 - 1))

for i in range(1, num2 + 1): # print(" " _ (num2 - 1) + "_")
arrow = arrow + (" " _ (num2 - i) + "_" _ (i _ 2 - 1) + "\n")
for i in range(num2):
arrow = arrow + (" " _ (num2 - 1) + "_" + "\n")
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
spaces = " " _ (num2 - i)
stars = "_" _ (i _ 2 - 1)
arrow += spaces + stars + "\n"

# 下半部直線箭頭柄

for \_ in range(num2):
spaces = " " _ (num2 - 1)
arrow += spaces + "_\n"

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

-

---

---

-
-
- 🧩 小任務（可以加入遊戲感）：
  試試看輸入不同的數字會產生什麼圖案？

看你能不能畫出最高的金字塔！

換成別的符號會怎樣？（例如 #、$）
