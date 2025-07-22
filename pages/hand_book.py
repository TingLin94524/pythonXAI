import streamlit as st

with st.expander("class 1 課堂筆記"):
    st.write(
        """
    當然可以！以下是把你今天上課學到的 Python 指令內容，用國小學生也能懂的方式整理成的筆記：

    🐍 Python 簡單筆記：讓電腦聽你的話！
    💬 什麼是「註解」？
    有時候我們寫程式時，會想加一點說明文字，這樣別人（或以後的自己）才看得懂！

    單行註解：在前面加 #

    python
    複製
    編輯
    # 這是單行註解
    多行註解：用三個雙引號 \""" 把中間的文字包起來

    python
    複製
    編輯
    \"""
    這是多行註解
    可以寫很多行～
    \"""
    📢 輸出東西：讓電腦說出來！
    python
    複製
    編輯
    print(123)           # 顯示數字
    print(3.14)          # 顯示小數
    print("Hello!")      # 顯示文字
    print(True)          # 顯示布林值（True 表示「對」，False 表示「錯」）
    ➕ ➖ ➗ ➕ 算數好朋友
    python
    複製
    編輯
    print(7 + 3)     # 加法：10
    print(7 - 3)     # 減法：4
    print(7 * 3)     # 乘法：21
    print(7 / 3)     # 除法：2.333...
    print(7 // 3)    # 整數除法（只要整數）：2
    print(7 % 3)     # 餘數：1
    print(7 ** 3)    # 次方（7 的 3 次方）：343
    🧮 變數是裝東西的小盒子
    python
    複製
    編輯
    x = 4
    x = x + 3  # 現在 x 變成 7
    x = x * 2  # 現在 x 變成 14
    print(x)
    ✨ 文字的魔法：字串
    python
    複製
    編輯
    s1 = "Hello"
    s2 = "World"
    s3 = s1 + " " + s2  # 用 + 把字串接在一起
    print(s3)  # 結果是 Hello World
    🙋‍♂️ 自我介紹（用 f-string）
    python
    複製
    編輯
    name = "Python"
    age = 31
    print(f"我是{name}，今年{age}")  # f-string 可以插入變數
    📏 量一量：字串長度
    python
    複製
    編輯
    print(len(""))         # 結果是 0
    print(len("Hello"))    # 結果是 5
    🔍 這是什麼類型？
    python
    複製
    編輯
    print(type(True))      # 顯示 bool（布林值）
    print(type(123))       # 顯示 int（整數）
    print(type(123.0))     # 顯示 float（小數）
    🔄 轉來轉去（型別轉換）
    python
    複製
    編輯
    print(float(True))     # 把 True 變成小數 → 1.0
    print(float(123))      # 把整數變小數 → 123.0

    print(bool(0))         # False（0 代表沒有）
    print(bool(1))         # True
    print(bool(-2))        # True
    print(bool(""))        # False（空字串是 False）
    print(bool("hello"))   # True（有字就是 True）

    print(str(True))       # 變成字串 "True"
    print(str(1000))       # 變成字串 "1000"
    ⚠️ 注意：不能亂轉！

    python
    複製
    編輯
    print(float("hello"))  # 這樣會錯誤喔！
    🧑‍🎓 讓使用者輸入內容
    python
    複製
    編輯
    get = input("請輸入一些內容: ")
    print(get)              # 顯示你剛剛輸入的內容
    print(type(get))        # 顯示它是字串
    🎯 小挑戰：計算圓的面積！
    python
    複製
    編輯
    r = float(input("請輸入圓的半徑: "))
    area = 3.14 * r ** 2
    print(f"圓的面積為: {area}")            # 用 f-string
    print("圓的面積為:" + str(area))        # 用字串相加
    🎉 恭喜你學會了這些！
    你今天學會了：

    怎麼註解

    怎麼輸出東西

    算數的基本用法

    字串、變數、型別轉換

    怎麼讓使用者輸入內容

    計算圓面積的小練習！

    加油，小小程式設計師！🚀

    需要我幫你把它變成漂亮的 PDF 嗎？或想加上一些圖示和練習題也可以喔！




    詢問 ChatGPT
    你說：
    phython
    print9("Hello World!")

    # 這是標題1
    ## 這是標題2
    ### 這是標題3
    #### 這是標題4
    """
    )

with st.expander("class 2 課堂筆記"):
    st.write(
        """
一、比較運算子：比一比，看誰大誰小！
比較方式    意思是？	範例	結果
==	        一樣嗎？	1 == 2	❌ False
!=	        不一樣嗎？	1 != 2	✅ True
>	        比它大？	1 > 2	❌ False
<	        比它小？	1 < 2	✅ True
>=	        大或一樣？	1 >= 2	❌ False
<=	        小或一樣？	1 <= 2	✅ True

🔴 二、邏輯運算子：真的還是假的？
運算子	中文意思	範例	結果
not	不是	not True	❌ False
and	而且	True and False	❌ False
or	或是	True or False	✅ True

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
    print("歡迎Ray")
elif password == "5678":
    print("歡迎Mike")
elif password == "abcd":
    print("歡迎Alise")
else:
    print("密碼錯誤")
💡 不同密碼代表不同的人，像是：

輸入 1234 ➜ 歡迎Ray

輸入 abcd ➜ 歡迎Alise

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

判斷方法	是不是閏年？
被 4 整除	可能是閏年 ✅
被 100 整除	不一定 ❌
被 400 整除	一定是閏年 ✅

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
    f\"""
```
箭頭金字塔:
{arrow}
```
\"""
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

"""
    )
