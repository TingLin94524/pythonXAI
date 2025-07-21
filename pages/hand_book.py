import streamlit as st

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
