# 簡易判斷
print('-' * 25, '簡易判斷', '-' * 25)
f0 = 1 == 1
f1 = 3 > 2
f2 = 2 < 1
f3 = f1 and f2
f4 = f1 or f2
f5 = not (1 != 2)
print('f0 = ', f0)  # true
print('f1 = ', f1)  # true
print('f2 = ', f2)  # false
print('f3 = ', f3)  # false
print('f4 = ', f4)  # true
print('f5 = ', f5)  # false


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

# 數組 Tuple () ,  列表 List [] ,  集合 Set , 字典 Dict {} .  前三種非常相似，不同的點在於 [集合不會包含重複資料]
# ----集合 , 各種建立方式Set operation
print('-' * 25, '集合建立方式', '-' * 25)
set0 = set()              # 建立空集合
set1 = set('abracadabra')
set2 = {1, 2, 3, 4, 5, 5}  # 集合不會包含重複的資料，列印出來就知道
set3 = set([i for i in range(20, 30)])  # 從串列(List)建立集合
set4 = set((10, 20, 30, 40))  # 從數組(Tuple)建立集合
print(set1)
print(set2)
print(set3)
print(set4)

# 運算 , 交集 & , 聯集 | , 減集 -  , 反交集 ^ ,  測試左集合是否為右集合的父集 > , 測試左集合是否為右集合的子集 <
print('-' * 25, '集合運算', '-' * 25)
s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}
# print(10 not in s1)
# s3 = s1 & s2 #交集，取兩個集合中，相同的資料 {4,5}
# s3 = s1 | s2 #連集，取兩個集合中所有資料，但不重複 {3,4,5,6,7}
# s3 = s1 - s2 #差集，從s1 中，減去和 s2 重疊的值 {3} , 若 s2 - s1 , 則從 s2 中，減去和 s1 重疊的值 {6,7}
# s3 = s1 ^ s2 #反交集，取兩個集合中，不重疊的部分
# s3 = s1 < s2
# print(s3)

# 函數
# set1.clear()
set1 = {2, 4, 6, 8}
print(len(set1))  # 長度 1 開始計算
print(min(set1))  # 最小值
print(max(set1))  # 最大值
print(sum(set1))  # 集合加總

# 判斷
set1 = {2, 4, 6, 8}
print(2 in set1)
print(3 in set1)
print(2 not in set1)
print(3 not in set1)

# for迴圈列印集合 , *集合和串列數組不同, 不可以使用索引來擷取特定元素*
set1 = {2, 4, 6, 8}
for i in set1:
    print(i, end=' ')

# ----字典---- 創建字典 {} or dict() 兩者都可
print('-' * 25, '字典', '-' * 25)
emptydict1 = {'Name': 'jeffrey', 'Age': 5, 'Sex': 'man'}
emptydict2 = dict()
print(emptydict1['Name'])

emptydict1['City'] = 'New York'  # 新增鍵值
print(emptydict1)

for key in emptydict1:
    if "City" in emptydict1:
        print()
    print('鍵值:', key)

print('-'*50)
emptydict1['Name'] = 'Emm'
emptydict1['Age'] = 20
print(emptydict1['Name'])
print(emptydict1['Age'])
