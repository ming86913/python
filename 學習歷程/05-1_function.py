import Fumciot_module as module
# 函式 : 沒有retrun 程式會在最後一行自行編譯，return 沒給值會回傳 None & 沒有 return 會回傳 None
# 定義函式 -> def 函式名稱() or def 函式名稱(參數,參數...) & 呼叫函式 -> 函式名稱()

# https://www.youtube.com/watch?v=OOJmhezLd4o&list=PL-g0fdC5RMboYEyt6QS2iLb_1m7QcgfHk&index=10

# 定義函式


def myfm01():
    print('a')


def say(msg):  # 需要帶入參數
    print('函式內層 : ', msg)
    return 'sss'  # 沒有給值就會回傳 None


def addition(a, b):
    c = a + b
    return c  # 沒有return 也是回傳 None


def multiply(n1, n2):
    # print('multiply = ', n1 * n2)
    return n1*n2


# add(a=0,b=0.c=0) 明確定義，其實有更好的方案。因為可能會有0個或多個進行運算，具體是多少由調用者決定，程式設計者是一無所知的
# 不確定參數個數時，可使用 "可變參數" add(*參數)。參考add2()
def add(a=0, b=0, c=0):
    print(a, b, c)
    return a + b + c


def add2(*args):
    for_reps = 0
    totle = 0
    for val in args:
        for_reps += 1
        totle += val
        print('第', for_reps, '次參數 = ', val)
    return totle


# 一般累加寫法
def calculate01(max):  # (1) = 1 or range(1,5) = 0~4 or (1,5,2) = 1,3
    sum = 0
    for i in range(1, max+1):
        sum += i
        print('i=', i)
    return sum


# 一般累加寫法 - 特殊用法 -> 給3個參數會變成 (起,迄,步數)
def calculate02(*i0):  # (1) = 1 or range(1,5) = 0~4 or (1,5,2) = 1,3
    sum = 0
    print('i0 = ', i0)
    for i in range(*i0):
        sum += i
        print('i=', i)
    return sum


# 開次方，預設值
def power(base, exp=0):  # 任何數的0次方都是 1
    print(base, '的', exp, '次方 = ', base ** exp)  # A ** B = A的次方


# 除法
def divide(n1, n2):
    print(n1 / n2)


# 無限/不定 參數 , 運用 Tuple & for & len
def avg(*val):
    sum = 0
    for i in val:
        sum += i
    print('平均 = ', sum/len(val))


# ------------------ 呼叫函式 ------------------
# print('還沒呼叫函式')
# myfm01()
# value = say('123')
# print('函式外層 say 回傳 : ', value)
# value = addition(3, 4)
# print('函式外層 addition 回傳值 : ', value)
value = multiply(3, 4) + multiply(10, 5)
if value != 'none':
    print('呼叫函式結果 multiply 回傳值 : ', value)
else:
    print('回傳值 None =', value)

# print('add() = ', add())
# print('add(1) = ', add(1))
# print('add(2) = ', add(1, 2))
# print('add(3) = ', add(1, 2, 3))
# print('加總:', add2(1, 2, 2))


# 呼叫函式庫 透過 import , 將函式存在函式庫中呼叫，透過 import filename.py 才可呼叫
# module.Hello()


# 重複程式包裝 : 同樣邏輯可重複利用
print('-' * 25, '重複程式包裝', '-' * 25)
# 兩個迴圈的程式相差無幾，僅是range 的差異。可以透過函式將似的程式包裝起來，以參數設定就可以重複使用不必重複寫
# 1. 1~10 累加
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)
# 2. 1~20 累加
# sum = 0
# for i in range(1, 21):
#     sum += i
# print(sum)

# 重複程式包裝寫成函式後
print('1 ~ 10 累加 = ', calculate01(10))
# print('1 ~ 20累加 = ', calculate(1, 21))
# 如何知道range(*i0)的值?  -> 參考 *range  &  list(range)
print('1 ~ 5 奇數累加 = ', calculate02(1, 6, 2))
# 解壓縮range : *range   = list(range(1, 10, 2)) 轉換List , 差別一個是
print('*range = ', * range(1, 6, 2))  # 1 ,3 不包含5
print('list range = ', list(range(1, 6, 2)))


# 函式預設參數、名稱對應、任意長度參數
print('-' * 25, '函式預設參數、名稱對應、任意長度參數', '-' * 25)

# 預設參數值
power(3, 2)
power(4)  # 如果未在函式設定預設值，會出錯

# 名稱對應
divide(2, 4)  # 0.5
divide(n2=2, n1=4)  # 2 , n1不管放在哪個位子都會傳入函式(n1)的位子

# 無限/不定 參數
avg(1, 4)
avg(1, 5, 2)
avg(1, 2, -2, 6)
