當然可以！以下是幫你整理的 Python 課程筆記，用國小學生也能看懂的方式寫出來：

---

# 🐍 今天的 Python 學習筆記 ✨

## 🔢 數數看：用 `len()`

- `len([])` 會得到 `0`，因為裡面沒有東西。
- `len(["a", "b"])` 結果是 `2`，因為有兩個東西。
- `len([1, 2, 3])` 是 `3`。

---

## 📢 用 `print()` 把東西顯示出來

```python
print("蘋果")
```

顯示的結果會是：蘋果

---

## ➰ 用 `for` 和 `range()` 一個一個顯示

```python
l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])
```

會依序顯示：

```
1
2
3
```

---

## ➰ 更簡單的寫法！

```python
for item in l:
    print(item)
```

也是一樣會印出每一個項目。

---

## ✍️ 改掉串列（List）裡的東西

```python
l[0] = "A"
l[2] = "C"
print(l)
```

結果會變成：`["A", 2, "C"]`

---

## 📛 變數也有「分身」

```python
a = [10, 20, 30]
b = a
b[1] = 200
print(a)
```

結果會是 `[10, 200, 30]`，因為 b 是 a 的「分身」，改 b 也會改到 a！

---

## 🧪 複製一份出來就不會互相影響！

```python
c = [40, 50, 60]
d = c[:]
d[1] = 500
print(c)
```

這時候 c 會保持不變，還是 `[40, 50, 60]`！

---

## 📦 把東西加進串列用 `append()`

```python
l1 = [1, 2, 3]
l1.append(4)
print(l1)  # [1, 2, 3, 4]
```

---

## 🧽 移除東西用 `remove()` 和 `pop()`

```python
l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")
print(l2)  # 只會移除第一個出現的 "b"
```

```python
l3 = [1, 2, 3]
l3.pop()
print(l3)  # 會移除最後一個
```

```python
l4 = [1, 2, 3]
l4.pop(1)
print(l4)  # 會移除第 2 個（數字 2）
```

---

## 🧑‍🍳 排序用 `sort()`

```python
l6 = ["banana", "cherry", "apple"]
l6.sort()
print(l6)  # 會按照字母順序排好
```

---

## 🎮 `while` 迴圈一直做

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

會印出 0 到 4。

---

## ⛔ 加入 `break` 可以中斷！

```python
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
```

會在印出 0, 1, 2 之後停止。

---

## 🎲 `random` 隨機數

```python
import random
print(random.randrange(0, 10, 2))  # 0, 2, 4, 6, 8 中的隨機一個
```

---

## 🎯 猜數字小遊戲！

```python
target = random.randint(1, 100)
while True:
    guess = int(input("請輸入你的數字: "))
    if guess < target:
        print("再大一點")
    elif guess > target:
        print("再小一點")
    else:
        print("猜中了!")
        break
```

---

## 🧧 一番賞抽獎遊戲

```python
table = [0] * 100
target = random.randint(1, 100)
table[target - 1] = 1
count = 0

while True:
    pick = random.randint(1, 100)
    if table[pick - 1] == 2:
        print("已經抽過了")
    elif table[pick - 1] == 1:
        print("恭喜你抽中了一番賞！")
        break
    else:
        print("沒有中獎，繼續抽")
    table[pick - 1] = 2
    count += 1

print(f"總共抽了 {count} 次，花了 {count * 200} 元")
```

---

## 🖼️ 用 Streamlit 做互動式網頁

### 🔘 按鈕和欄位

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

### 📝 文字輸入

```python
text = st.text_input("請輸入文字")
st.write("你輸入的文字是:", text)
```

### ➕ 加一功能

```python
ans = 1
if st.button("加1"):
    ans += 1
st.write(f"ans={ans}")
```

### 📦 用 session_state 記住資料

```python
if "varl" not in st.session_state:
    st.session_state.varl = 1

if st.button("add one to varl"):
    st.session_state.varl += 1
    st.rerun()
```

---

## 🍔 點餐機小專案

- 使用欄位、按鈕、文字輸入
- 將輸入的餐點加入購物籃
- 按下「刪除」可把餐點移除
- 使用 `st.session_state` 記住訂單內容

---

如果你看得懂這些筆記，就代表你已經是個會寫程式的小高手了！🎉
繼續加油，Python 的世界還有好多好玩的東西等你來探索哦！🚀

需要我幫你畫圖解釋其中某個概念嗎？😊
