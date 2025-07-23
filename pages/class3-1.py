print(len([]))  # 結果是 0
print("蘋果")  # 結果是 '蘋果'
print(len(["a", "b"]))
print(len([1, 2, 3]))  # 結果是 3

print("-" * 20)  # 分隔線

l = [1, 2, 3]
for i in range(len(l)):
    print(l[i])

print("-" * 20)  # 分隔線

for element in l:
    print(element)  # 直接取得每個元素

print("-" * 20)  # 分隔線

l[0] = "A"
l[2] = "C"
print(l)  # 修改後的串列

print("-" * 20)  # 分隔線

a = [10, 20, 30]
b = a
b[1] = 200
print(a)  # a 也會變成 [10, 200, 30]，因為 b 是 a 的別名

print("-" * 20)  # 分隔線

c = [40, 50, 60]
d = c[:]
d[1] = 500
print(c)  # c 還是 [40, 50, 60]，因為 d 是 c 的複製

print("-" * 20)  # 分隔線

l1 = [1, 2, 3]
l1.append(4)
print(l1)

print("-" * 20)  # 分隔線

l2 = ["a", "b", "c", "b", "a"]
l2.remove("b")  # 移除第一個 "b"
print(l2)

print("-" * 20)  # 分隔線

l3 = [1, 2, 3]
l3.pop()
print(l3)

print("-" * 20)  # 分隔線

print("-" * 20)  # 分隔線

l4 = [1, 2, 3]
l4.pop(1)
print(l4)

# l5 =


l6 = ["banana", "cherry", "apple"]
l6.sort()
print(16)
