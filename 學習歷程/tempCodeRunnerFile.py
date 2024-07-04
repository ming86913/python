n = int(input('請輸入整數'))  # 使用者輸入資料且轉換成整數，不使用int()轉換會是type str, (假設都是輸入整數)
for i in range(n):
    if i*i == n:
        print('平方根 = ', i)
        break  # 用 break 強制結束迴圈時,不會執行 else 區塊
else:
    print('沒有整數平方根')
