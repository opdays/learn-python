############################################元类使用
class ListMetaClass(type):
    """
    定义元类
    """
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)

        attrs["add"] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
##################################################

class Mylist(list, metaclass=ListMetaClass):
    pass


class List(Mylist):
    def __init__(self):
        super(List, self).__init__()


l = List()

l.add(1)
l.add(2)
print(l)


######################################## 用type 创建类

def __init__(self, name):
    self.name = name
    print(self.name)


Class = type("class", (object,), {
    "__init__": __init__,
    "say_hello":lambda self:print("hello",self.name)
})

c = Class("yangyang")
print(c)
print(c.name)
c.say_hello()
##########################################
#
#__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值
#__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法
#__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数
#
class Animals:
    def __new__(cls, *args, **kwargs):
        print("go to __new__")
        print(*args)
        print(kwargs)
        print(cls)
        return object.__new__(cls)
        #return cls

    def __init__(self,name,age,):
        print("go to __init__")

a=Animals("aaa",age=12)
print(a)
##########################################################
#列表生成式 和 列表生成器
l = [ x for x in "abcd"]
print(l)
g = ( x for x in "abcd")
print(g)
print(next(g))

#可以直接用for遍历的对象叫    "可迭代对象"
from collections import Iterable,Iterator
print(isinstance([],Iterable))
print(isinstance(range(10),Iterable))
#

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
print(isinstance([],Iterator))
print(isinstance(range(10),Iterator))
print(isinstance(g,Iterator))

#字典生成式
d = { x:x for x in "abcd"}
d2 = dict(zip(list("abcd"),list("abcd")))
print(d)
print(d2)
print(d == d2)

#函数也是变量 可以作为字典的key 和value
def ni():
    print("asd")

aa={
    ni:ni
}
aa[ni]()

#匿名函数立即执行
(lambda :print("111111111111"))()