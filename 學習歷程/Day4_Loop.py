### while 練習: 若布林值為True , 執行命令 , 回到上方做下一次迴圈判斷 ###
# print('-'*25, ' While 迴圈 ', '-'*25)
# 累加 1 ~ 4
# n = 1
# sum = 0  # 紀錄總數
# while n < 5:
#     sum = sum + n
#     n += 1
# print('n = %d ' % sum)  # ==  print('n = ' n)
# print(sum)

### for 練習: ###
# print('-'*25, ' for 迴圈 ', '-'*25)
# for x in [4, 1, 2]:
#     print('列印出 x = ', x)

# range(5) -> 會產生列表，不包含5 [0,1,2,3,4]  ; range(5,10) -> 產生列表 [5,6,7,8,9]
# print(range(5))
# for x in range(11):
#     print(x)
# for x in range(5, 10):
#     print('range(5,10) = ', x)

# 累加 1~10 , +1 +2 +3...+10
# sum = 0
# for x in range(1, 11):
#     print('x = ', x)
#     sum += x
# print(sum)


# break 簡易範例
# n = 0
# while n < 5:
#     if n == 3:
#         break
#     n += 1
#     print('列印while迴圈中的n', n)
# print('列印while迴圈最後的n', n)

# n = 0
# for n in range(5):
#     if n == 3:
#         break
#     n += 1
#     print('列印for迴圈中的n', n)
# print('列印for迴圈最後的n', n)

# Continue 簡易範例
# n = 0
# x = 0
# while x < 4:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)
#     n += 1
# print('while 最後的 n = ', n)

# n = 0
# for x in [0, 1, 2, 3]:
#     if x % 2 == 0:  # x是偶數(餘數 = 0)
#         continue  # 直接執行下一個迴圈
#     print(x)
#     n += 1
# print('for 最後的n = ', n)

# else 簡易範例
# sum = 0
# n = 1
# while n <= 10:
#     sum += n
#     n += 1
# else:
#     print('while 迴圈加總', sum)
# sum = 0
# for n in range(11):  # 1~10
#     sum += n
# else:
#     print('for 迴圈加總', sum)  # 印出 +1 +2 +3...+10 的結果

# 綜合練習 , 使用者輸入數字 得出平方根。 輸入 9  輸出 "平方根 = 3" , 輸入 11 輸出 "沒有"
print('-'*25, ' 綜合練習 ', '-'*25)
n = int(input('請輸入整數'))  # 使用者輸入資料且轉換成整數，不使用int()轉換會是type str, (假設都是輸入整數)
for i in range(n):
    if i*i == n:
        print('平方根 = ', i)
        break  # 用 break 強制結束迴圈時,不會執行 else 區塊
else:
    print('沒有整數平方根')
