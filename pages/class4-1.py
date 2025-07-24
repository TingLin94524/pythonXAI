d1 = {}
d2 = {"apple": "蘋果"}
d3 = {"banana": "香蕉", 2: "二", 3: "三"}

print(d2["apple"])
print(d3["banana"])

print("_" * 20)

for key in d2:
    print(key)

print("_" * 20)

for key in d3:
    print(key)

print("_" * 20)

for key, value in d2.items():
    print(key, value)

print("_" * 20)

d3[2] = "二"
print(d3)
d3[3] = "三"
print(d3)
v = d3.pop(2)
print(d3)
print(f"刪除的值: {v}")
v = d3.pop(3)
v = d3.pop(5, "不存在的值")
print(d3)
print(f"刪除的值: {v}")
print("d3的長度", len(d3))

print("_" * 20)

print(2 in d3)
print(3 in d3)
print("three" in d3)

print("_" * 20)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("orange" in fruits)
