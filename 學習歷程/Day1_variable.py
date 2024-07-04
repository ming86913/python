########          變數       ############
# 變數 - 無指派類型
"""
x = 5
"""
# 變數 - 指派類型
"""
x1 = str(3)
y1 = int(3)
z1 = float(3)
print("x1 = ", x1, "; x1 type = ", type(x1))
print("x1 = ", y1, "; y1 type = ", type(y1))
print("x1 = ", z1, "; z1 type = ", type(z1))
"""
# 字串可以使用單引號 or 雙引號
"""
x = "Sally"
y = 'Jeffrey'
print(x)
print(y)
"""


# 變數大小寫是否有區別? 有大小寫是不同變數
a = 4
A = "big A"
print(a)
print(A)

# 變數命名規則 1.必須字母 OR 底線為開頭 2.變數不可以數字為開頭 3.變數名稱只能包含字母數字和底線 4.變數區分大小寫 5.變數不能是Py關鍵字
"""
myvar = 'John'
my_var = 'John'
_my_var = 'John'
myVar = 'John'
MYVAR = 'John'
Myvar = 'John'
myvar2 = 'John'
"""

# 分配多個值
# 1.多個值到多個變數
x, y, z = "Orange", "Banana", "Cherry"
# 2.一個值對應多個變數,多變數要以 = 為媒介 不可用 ,
var1 = var2 = var3 = "Orange"
print(var1)

# ----集合解壓縮  List[0 , 1 , 2....]
# 獲取
fruits = ['apple', 'banana', 'orange', 'grape']
print(fruits[0])  # 輸出：'apple'
# 修改
fruits[1] = 'pear'
print(fruits[1])
fruits[1] = 'modify'
print(fruits[1])
# 增加
fruits.append('watermlon')
print(fruits)
print(fruits[4])
# 刪除
del fruits[1]
print(fruits)
# ----集合解壓縮
# ----切片 [0,1,2,3] = [-4,-3,-2,-1]
fruits = ['1', '2', '3', '4']
slice_fruits = fruits[0:2]
print("0:2 = ", slice_fruits)  # 輸出:b1,o2
# print(fruits[-4])


fruits = ['1', '2', '3', '4']
slice_fruits = fruits[1:3]
print("1:3 = ", slice_fruits)  # 輸出：['banana', 'orange']
# ----切片

# 全域變數
x = 'awesome'


def myfunc():
    x = 'fantastic'
    print(x)


myfunc()
print(x)

a = 1
b = 2

num99 = 1
num98 = 1


def myfm(a, b):
    num99 = 5
    num98 = 5
    a1 = 5
    b1 = 5
    print(a + b)
    print('myfm num98 + num99 = ', num98 + num99)
    print('myfm a1 +b1 = ', a1 + b1)
    print('global = ', a+b)
    a = 100
    b = 40
    print('myfm a + b = ', a + b)


myfm(a, b)
print('a + b = ', a + b)
print('not myfm = ', num98 + num99)
########          變數       ############

########          資料類型       ############
z = -1123123
print(type(z))
########          資料類型       ############
