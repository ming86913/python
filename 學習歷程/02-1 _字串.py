# 字串 & index[0] 指定輸出 類似ABAP str+0(2)
print('-' * 25, '字串應用', '-' * 25)
name = 'Jeffrey'
message = '嗨嗨!!'
today = '禮拜一'
articles = '今天請假人數 2 ,一個確診躺在家休養'

# index 抓字元
print(name[1])
print(message[2])
print(today[-1])
print(articles[0:5])
print(articles[5:10])


# 輸入字串相加
print('-' * 25, '字串相加', '-' * 25)
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))   # % 操作符被用來進行格式化帶入
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# 字串相關處理 & 應用
print('-' * 25, '字串處理 & 應用', '-' * 25)
# .format  字符串模板,使用變數合成字串
name2 = 'Keven'
message2 = '嗨嗨 ,我是{}'.format(name2)  # 在{}中塞 format 傳入值
print(message2)

today1 = '星期1'
weather1 = '晴天'
message3 = '今天 {},天氣 {}'.format(today1, weather1)  # 在{}中塞 format 傳入值
print(message3)
print('-' * 100)
# [:] 利用字串index 取值
print(message3[1:5])
print('-' * 100)
# .split 字串分割
message4 = '今天天氣是晴天 , 可是辦公室有點冷 , 有點適合睡覺'
print(message4.split(' , '))

test1 = 'aa-bb-cc-dd'
test2 = 'll;bod;adsk;lio+asd'
print(test1.split('-'))
print(test2.split(';'))
print('-' * 100)
# .join字串合併
text1 = test1.split('-')
text2 = 'ABCD123'
print('-'.join(text1))

print(text2.split())
print(','.join(text2))
print('-' * 100)
