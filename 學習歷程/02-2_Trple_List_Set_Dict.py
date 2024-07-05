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

# 數組 Tuple () ,  列表 List [] ,  集合 Set , 字典 Dict {} .  前三種非常相似，不同的點在於 [集合不會包含重複資料]

# ----數組
print('-' * 25, '數組 Tuple', '-' * 25)
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 2, 3)  # 重複值，會顯示
print(tuple1)
print(tuple2)

# ----列表
print('-' * 25, '列表 List', '-' * 25)
list01 = [0, 1, 1]  # 重複值，會顯示
print('List : ', list01)
print('List[1] : ', list01[1])

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

dict01 = {'name': 'jeffrey', 'age': '26'}
print(dict01['name'])

# 集合運算 , 交集 & , 聯集 | , 減集 -  , 反交集 ^ ,  測試左集合是否為右集合的父集 > , 測試左集合是否為右集合的子集 <
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

# 集合函數
# set1.clear()
set1 = {2, 4, 6, 8}
print(len(set1))  # 長度 1 開始計算
print(min(set1))  # 最小值
print(max(set1))  # 最大值
print(sum(set1))  # 集合加總

# 集合判斷
set1 = {2, 4, 6, 8}
print(2 in set1)
print(3 in set1)
print(2 not in set1)
print(3 not in set1)

# 集合for迴圈列印 , *集合和串列數組不同, 不可以使用索引來擷取特定元素*
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
