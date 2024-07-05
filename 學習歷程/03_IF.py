# if 判斷
if True:
    print('true')
else:
    print('false')

# 四則運算
n1 = int(input('請輸入數字'))
n2 = int(input('請輸入數字'))
op = input('請輸入運算符號 : + or - or * or / :')

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print('不支援運算')


# if 判斷 & While 迴圈搭配
# while True:
#     try:
#         x = input('請輸入數字')
#         x = int(x)
#         if x > 200:
#             print('大於200')
#         elif x > 100:
#             print('大於100,小於200')
#         else:
#             print('小於100')
#         break
#     except:  # pylint: disable=bare-except
#         print("Error , Please Enter an integer")
#         continue
