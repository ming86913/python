# 練習1. 華氏溫度轉換攝氏溫度  $C=(F - 32) \div 1.8$。
print('-' * 25, '練習1. 華氏溫度轉換攝氏溫度', '-' * 25)
f = float(input('請輸入華氏溫度 : '))
c = (f - 32)/1.8
print('攝氏溫度 = ', c)
print('攝氏溫度 = %.1f' % c)  # %.1f是一個佔位浮 與 %d 概念相同，使用 %.1f 是限制 float 只有1位數
print(f'{f:.1f}華氏度 = {c:.1f}攝氏度')


# 練習2. 圓周長=直徑 * 圓周率,圓面積=半徑*半徑*圓周率
print('-' * 25, '練習2. 圓的計算', '-' * 25)
radius = float(input('請輸入半徑 :'))
perimeter = radius * 2 * 3.14
area = radius * radius * 3.14
print('圓周長 = %.2f' % perimeter)
print('圓面積 = %.2f' % area)

# 練習3. 平方根 for & if
print('-' * 25, '練習3. 平方根', '-' * 25)
n = int(input('請輸入整數'))  # 使用者輸入資料且轉換成整數，不使用int()轉換會是type str, (假設都是輸入整數)
for i in range(n):
    if i*i == n:
        print('平方根 = ', i)
        break  # 用 break 強制結束迴圈時,不會執行 else 區塊
else:
    print('沒有整數平方根')


# 建立簡易計算機

num1 = float(input('請輸入數字1 : '))
operator = str(input('請輸入運算符號(限定 + , - , * , / ): '))
num2 = float(input('請輸入數字2 : '))
num = 0
flag = ''

match operator:
    case '+':
        num = num1 + num2
    case '-':
        num = num1 - num2
    case '*':
        num = num1 * num2
    case '/':
        num = num1 / num2
    case _:  # 如果上面的case 都沒有命中，則執行這行，類似於Switch的default
        flag = 'X'
        print('輸入錯誤')

if flag != 'X':
    print(num)
