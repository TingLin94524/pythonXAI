以下是把你今天學到的 Python 課程內容整理成國小學生看得懂的筆記，用簡單的方式來說明每個指令和概念哦！

---

# 🐍 Python 小學生筆記 ✨

## 📦 一、字典 Dictionary

字典就像一本中英對照小字典，我們可以用一個「關鍵字」來查出對應的「值」。

### 🔸 建立字典

```python
d1 = {}  # 空字典
d2 = {"apple": "蘋果"}
d3 = {"banana": "香蕉", 2: "二", 3: "三"}
```

### 🔸 查詢資料

```python
print(d2["apple"])  # 印出 "蘋果"
print(d3["banana"])  # 印出 "香蕉"
```

### 🔸 用 for 來看字典裡有什麼

```python
for key in d2:
    print(key)  # 印出 apple

for key, value in d2.items():
    print(key, value)  # 印出 apple 蘋果
```

### 🔸 新增、修改和刪除資料

```python
d3[2] = "二"  # 加入或修改 2 對應的值
print(d3)

v = d3.pop(2)  # 刪除 key 為 2 的資料
print("刪除的值:", v)
```

### 🔸 其他有用的字典功能

```python
print(len(d3))  # 看字典有幾筆資料

print(2 in d3)  # 看 key 2 有沒有在字典裡
```

---

## 🍎 二、List 列表（像水果籃）

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # True，有香蕉
print("orange" in fruits)  # False，沒有橘子
```

---

## 🛍️ 三、購物平台小遊戲（用 Streamlit 做的網頁）

你學會了用 `streamlit` 做出一個簡單的購物平台！

### 功能有：

1. ✅ 顯示商品圖片、名字、價格、庫存
2. 🛒 可以按「購買」按鈕買東西，庫存會減少
3. ➕ 可以新增商品的庫存數量
4. 📦 查看每個商品還剩幾個

### 小小重點：

- `st.image()` → 顯示圖片
- `st.write()` → 顯示文字
- `st.button()` → 按鈕
- `st.number_input()` → 數字輸入框
- `st.selectbox()` → 下拉選單

---

## 🎲 四、擲骰子模擬器

你做了一個可以擲骰子的程式！

```python
import random

def roll_dice(num):
    list_value = []
    for i in range(num):
        x = random.randint(1, 6)  # 隨機產生 1~6 的數字
        list_value.append(x)
    return list_value
```

接下來你用迴圈計算每個點數出現的次數：

```python
n1 = 0
n2 = 0
...
n6 = 0

for num in outcome:
    if num == 1:
        n1 += 1
    elif num == 2:
        n2 += 1
    ...
```

最後印出統計結果：

```
1出現 3 次
2出現 2 次
...
```

---

## ✨ 結語

今天你學到很多 Python 的內容，包括：

- 字典的基本用法
- 怎麼查資料、修改、刪除
- 列表和字典的比較
- 用 `streamlit` 做出購物平台
- 還做了一個擲骰子的小遊戲！

---

如果你記不起來某段程式碼，回來這份筆記看看就可以囉！加油～你正在變成小小程式高手 🧠💻🎉

---

需要我幫你做成圖表或加插圖的版本也可以說喔！
