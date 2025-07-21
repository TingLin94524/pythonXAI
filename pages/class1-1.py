# # """
# # 這
# # 是
# # 多
# # 行
# # 註
# # 解
# # """

# # # 這是單行註解

# # print(123)  # 輸出整數
# # print(3.14159265)  # 輸出浮點數
# # print(True)  # 輸出布林值
# # print(False)  # 輸出布林值
# # print("Hello World!")  # 輸出字串
# # print("tinglin94524" + "666")  # 輸出字串
# # x = 4
# # x = x + 3
# # print(x)
# # x = x * 2
# # print(x)

# print(7 + 3)  # 加法
# print(7 - 3)  # 減法
# print(7 * 3)  # 乘法
# print(7 / 3)  # 除法
# print(7 // 3)  # 整數除法
# print(7 % 3)  # 取餘數
# print(7**3)  # 7的3次方

# v1 = 0.1
# v2 = 0.2
# print(v1 + v2)

# s1="Hello"
# s2="World"
# s3=s1 + " " +s2  # 字串連接
# print(s1+s2)
# print(s3)  # 輸出字串

name = "Phython"
age = 31
new_str = f"我是{name}，今年{age}"
print(new_str)

print(len(""))
print(len("Hello"))

print(type(True))
print(type(123))
print(type(123.0))
# print(type("hello"))#這行會報錯,因為無法將字串轉換為整數

print(float(True))  # 將布林值轉換為浮點數
print(float(123))  # 將整數轉換為浮點數
print(float("hello"))

print(bool(0))  # False
print(bool(1))  # True
print(bool(-2))  # True
print(bool("hello"))  # False
print(bool(""))  # False

print(str(True))
print(str(1000))
print(str("yes"))

get = input("請輸入一些內容: ")
print(get)
print(type(get))

r = input("請輸入圓的半徑: ")
area = 3.14 * r**2  # 計算圓的面積
print(f"圓的面積為: {area}")
print(f"圓的面積為:" + str(area))  # 使用str字串連結
