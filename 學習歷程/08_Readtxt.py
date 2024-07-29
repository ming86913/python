class Readfile():
    fileaddress = 'd:/text.txt'
    mode = 'r'

    def __init__(self, f, m):
        self.fileaddress = str(f)
        self.mode = str(m)

    def read(self):
        with open(self.fileaddress, self.mode, encoding='utf-8') as file:
            data = file.read()
            print(data)
        # return data

# ------------------    第一種   -------------------- open() 搭配 close()
# file = open('data.txt', mode='w', encoding='utf-8')  # 開啟
# file.write('Hello File\nAAAAA\n好棒棒')  # 寫入
# file.close()  # 關閉

# ------------------    第二種   -------------------- with open() 不用搭配 close()
# 使用with開啟檔案時，會將檔案放在file變數中,file只能在with範圍內使用，離開就會被自動關閉
# with open('data.txt', mode='r', encoding='utf-8') as file:
#     data = file.read()
# print(data)

# for line in lines:
#     print(line, end='')
# f.close()


# ------------------    第三種  -------------------- class
fileaddress = 'data.txt'
mode = 'r'
i = Readfile(fileaddress, mode)
i.read()
