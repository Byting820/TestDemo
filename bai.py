import argparse
from itertools import count
import numpy as np
from torchvision.transforms.transforms import RandomAdjustSharpness
data = np.load("/vol1/cuipeng_group/baiyuting/tumor/gcn_clustering-master/features_data/512.fea.npy")
data.shape    #(18171, 512)

#%%
class Cat:
    def __init__(self,new_name):
        print("这是一个初始化方法")
        #self.属性名=属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)

#使用类名（）创建对象的时候，会自动调用初始化方法，而不用Cat.__init__进行调用
tom = Cat("Tom")
print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()

class cat:
    def __init__(self,new_name):
        self.name = new_name
        print("%s 来了"% self.name)

    def __del__(self):
        print("%s 我去了"% self.name)

    def __str__(self):
        #必须返回一个字符串
        return "我是小猫[%s]" % self.name


tom = cat("Tom")
print(tom)
#del 关键字可以删除一个对象
del tom
print("*" * 50)

class person():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫 %s 体重是 %.2f 公斤" % (self.name,self.weight)

    def run(self):
        self.weight -= 0.5
    
    def eat(self):
        self.weight += 1


xiaoming = person("小明",75.0)

xiaoming.run()
xiaoming.eat()
print(xiaoming)



class women:

    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        #在对象的方法内部，是可以对象的私有属性的
        print("%s 的年龄是 %d" % (self.name,self.__age))

xiaofang = women("小芳")
#私有属性，在外界不能被直接访问
#print(xiaofang.__age)
#私有方法，同样不允许在外界直接访问
xiaofang.__secret()

class A:
     
     def test(self):
        print("test方法")

class B:

    def demo(self):
        print("demo方法")

class C(A,B):
    """多继承可以让子类对象同时拥有多个父类的属性和方法"""
    pass   #保证语法完整性


#创建子类对象
c = C()
c.test()
c.demo()


def test(name,age):
    print("今天天气不错")
    print(name)
    print(age)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='测试接受参数')
    parser.add_argument('-n',help = '姓名输入.')
    parser.add_argument('-a', help='年龄输入.')
    args = parser.parse_args()
    print(type(args),args)
    name = args.n
    print(type(name))
    age = args.a
    print(type(age),age)
    test(name,age)



class tool(object):

    #使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self,name):
        self.name = name

        #让类属性的值+1

#创建工具对象
tool1 = tool("斧头")
tool2 = tool("榔头")
tool3 = tool("水桶")

#输出工具对象的数量
print(tool.count)


#石头剪刀布案例
import random

#从控制台输入要输入的拳——石头（1）/剪刀（2）/布（3）：
player = int(input("请输入您要出的拳：石头（1）/剪刀（2）/布（3）"))

#电脑随机出拳
computer = random.randint(1,3)
print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player,computer))

#比较胜负
#1玩家胜
if ((player == 1 and computer == 3)
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
    print("欧耶，电脑弱爆了！")
#2平局
elif player == computer:
    print("真是心有灵犀啊，再来一盘！")
#3电脑胜
else:
    print("不服气，决战到天亮！")


i = 0
while i < 10:
    
    #continue某一条件满足时，不执行后续重复的代码
    if i == 3:
        #注意：在循环中如果使用continue这个关键字，
        #在使用关键字之前，需要确认循环的计数是否修改，否则可能导致死循环
        i += 1
        continue
    
    print(i)
    i += 1      #!!!重要！！一定要给计数器+1，要不然就陷入死循环！
print("over")

#打印小星星
row = 1
while row <= 3:
    # 每一行要打印的小星星就是和当前的行数是一致的
    # 增加一个小循环，专门负责当前行中，每一‘列’的星星显示
    # 定义一个列计数器变量
    col = 1
    #2开始循环
    while col <= row:
        print("*", end = "")
        col += 1

    #print("第 %d 行"% row)
    #!重要！这行代码的目的就是在一行小星星输出完成之后，添加换行！
    print("")
    row += 1


# %%
def say_hello():
    print("你好你好，我是say hello")

#如果直接执行模块，得到的永远只是__main__
if __name__ == "__main__":
    print(__name__)

    #文件导入时，能够执行的代码不需要被执行
    print("小明开发的代码")
    say_hello()


#%%
def demo1():
    num = 10
    print("demo1的内部变量是 %d"% num)

#在函数内部定义的变量，不能在其他位置使用
#print(" %d"% num)
demo1()



