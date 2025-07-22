# 一、比較運算子：比一比，看誰大誰小！
# 比較方式    意思是？	範例	結果
# ==	        一樣嗎？	1 == 2	❌ False
# !=	        不一樣嗎？	1 != 2	✅ True
# >	        比它大？	1 > 2	❌ False
# <	        比它小？	1 < 2	✅ True
# >=	        大或一樣？	1 >= 2	❌ False
# <=	        小或一樣？	1 <= 2	✅ True

# 🔴 二、邏輯運算子：真的還是假的？
# 運算子	中文意思	範例	結果
# not	不是	not True	❌ False
# and	而且	True and False	❌ False
# or	或是	True or False	✅ True

# 🎯 小提醒：

# and 是「而且」：兩個都要對，才是真的。

# or 是「或是」：有一個對，就是真的。

# not 是「反過來」：原本對的就變錯，原本錯的就變對。

# 🔐 三、練習：密碼驗證遊戲
# python
# 複製
# 編輯
# password = input("請輸入密碼: ")

# if password == "1234":
#     print("密碼正確")
# else:
#     print("密碼錯誤")
# 📌 如果你輸入 1234，會出現「密碼正確」，否則會說「密碼錯誤」。

# 🧑‍💻 四、歡迎不同的人
# python
# 複製
# 編輯
# if password == "1234":
#     print("歡迎Ray")
# elif password == "5678":
#     print("歡迎Mike")
# elif password == "abcd":
#     print("歡迎Alise")
# else:
#     print("密碼錯誤")
# 💡 不同密碼代表不同的人，像是：

# 輸入 1234 ➜ 歡迎Ray

# 輸入 abcd ➜ 歡迎Alise

# 輸入錯誤 ➜ 密碼錯誤

# 📅 五、閏年判斷小幫手
# python
# 複製
# 編輯
# year = int(input("請輸入年份: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} 是閏年")
#         else:
#             print(f"{year} 不是閏年")
#     else:
#         print(f"{year} 是閏年")
# else:
#     print(f"{year} 不是閏年")
# 🌟 什麼是閏年？
# 每 4 年會多一天（2 月 29 日），叫做「閏年」！

# 判斷方法	是不是閏年？
# 被 4 整除	可能是閏年 ✅
# 被 100 整除	不一定 ❌
# 被 400 整除	一定是閏年 ✅

# 🧪 範例：

# 2000 是閏年 ✅

# 1900 不是閏年 ❌

# 2024 是閏年 ✅
