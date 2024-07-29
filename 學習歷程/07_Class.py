# 定義Class類別
class FirstClass(object):  # 繼承 python 最上層的object類別
    def __init__(self, name):  # constuctor
        print('Hello , ' + str(name))

    # 函數(def)第一個參數必須加上self，表示是用這個物件
    def fun1(self):  # 實例方法，以self作為第一個參數、只能通過實例調用、能夠訪問和修改實例屬性和類別屬性

        print('This is function1')

    def fun2(self, num1=0, num2=0):
        self.fun1()  # 在fun2()調用fun1()
        return num1 * 2 + num2

    @classmethod
    def class_method(cls):  # 類別方法，以cls作為第一個參數、通過類別和實例調用、只能訪問和修改類別屬性
        print('這是類別方法')

    @staticmethod
    def static_method():  # 靜態方法，沒有 self , cls 參數、通過類別和實例調用、不能訪問和修改實例和類別的屬性，通常值行醫些獨立於類別和實例的操作
        print('這是靜態方法')


class Person:
    # 在類別中使用函數(Method)
    def __init__(self, name, age):  # 稱為constuctor,建構方法。每次使用該類別(Class)建立物件時都會呼叫該函式
        self.name = name
        self.age = age

    def __str__(self):
        # return f"{self.name}({self.age})"
        return f"{self.name, self.age}"  # f-string 格式化方法,


class People:  # 公/私屬性 & 私有方法範例 (私有屬性 & 私有方法 都是在前面加兩個 _)
    # 類別中定義屬性(Property)
    height = 180  # Property
    weight = 69   # Property
    name = 'unknown'
    __name2 = 'unknown'

    def __init__(self, h, w, n1, n2):
        self.height = h
        self.weight = w
        self.name = str(n1)
        self.__name2 = str(n2)  # 設定私有屬性

    def __private(self):  # 私有方法
        print('這裡是私有方法', self.__name2)

    def BMI(self):
        bmi = self.weight / (self.height / 100) ** 2
        print('體重 :', self.weight, '身高 :', self.height, '=', bmi)
        # 傳入bmi參數，為何?  bmi不是類別屬性而是變數，沒辦法直接在函式中直接調用，只能透過傳遞參數的方式讓函式知道
        self.print(bmi)  # 這裡呼叫下面的函式 Print()

    def print(self, num):
        print(str(self.name) + "\nheight : " +
              str(self.height) + '\nweight:' + str(self.weight))
        print('His BMI is ' + str(num))
        self.__private()  # 公有方法調用私有方法

    @classmethod
    def show_class_properties(cls):
        print('類別屬性 - 體重 :', cls.weight, '身高 :', cls.height)

    @staticmethod
    def calculate_BMI(height, weight):
        bmi = weight / (height/100) ** 2
        return bmi


# 繼承範例
class Father(object):
    networth = 10 ** 6
    house = 10
    company = 2
    name = 'unknown'

    def __init__(self, m, h, c, n):
        self.money = m
        self.house = h
        self.company = c
        self.name = n

    def printNetWork(self):
        print('NetWork :', str(self.networth))

    def printHouse(self):
        print('House Number :', str(self.house))

    def printComany(self):
        print('Comany :', str(self.company))


class Mother:
    MomNetWorth = 10 ** 9
    MomHouse = 20
    MomCompant = 10
    MomName = 'Anna'

    def __init__(self, n):
        self.MomName = str(n)

    def printNetWorth_From_Mom(self):
        print('Mom Net Worth', self.MomNetWorth)

    def printHouse_From_Mom(self):
        print('Mom House Numbwe:', self.MomHouse)

    def printComany_From_Mom(self):
        print('Mom Compant Number', self.MomCompant)


class Child(Father, Mother):  # 原本是放Object 現在改為要繼承的Class (可多重繼承)
    def __init__(self, name):
        print('Child: ', str(name))

    def func(self):
        super(Child, self).printComany_From_Mom  # 母
        super(Child, self).printComany  # 父


# --------------------------FirstClass-------------------------
# hi = FirstClass('jack')  # 建立一個名為 hi 的類別 , 自訂初始化的值
# hi.fun1()
# print(hi.fun2(1, 2))  # 傳入1,2參數進去 fun2 ， 不傳參數會默認 num1 = 0 , num2 = 0
# # print(hi.fun2(1,2)) == print(hi.fun2(num1 = 1, num2 = 2))
# FirstClass.class_method()
# FirstClass.static_method()

# --------------------------People-------------------------
# bill = People()
bill = People(170, 72, 'Jack', n2=None)
bill.BMI()
# bill.__private()  # 無法直接調用私有方法、私有屬性，會出現 AttributeError 的錯誤訊息，僅能透過Class中自行調用。 (其實可以調用但不推薦)

bmi_value = People.calculate_BMI(170, 72)
print('靜態方法 BMI', bmi_value)

# --------------------------Person-------------------------
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)
# p2 = Person('Emma', 27)
# print(p2.age, ',', p2.name)
# a = 'world'
# b = 'oxxo'
# c = f'hello {a:-<10s}, I am {b:>10s}'
# d = f'hello {a:-^10s}, I am {b:->10s}'
# print(c)
# print(d)

# --------------------------繼承、多重繼承-------------------------
bill = Child('bill')  # 建立實例類別 (子物件)
bill.func()
bill.printComany()
bill.printComany_From_Mom()
# bill.printNetWork()  # 子物件的身價可以拿父物件來使用
# bill.printHouse()  # 子物件的房子可以拿父物件來使用
