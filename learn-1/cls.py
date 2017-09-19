class Char:
    """
    26个英文字母，可以作用与for in 可以使用切片 和 索引
    """
    def __init__(self):
        self.value = list(map(chr,range(97,123)))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next = self.value[self.index]
            self.index = self.index + 1
            return next
        except :
            raise StopIteration()
    def __getitem__(self, item):
        if isinstance(item,int):
            return self.value[item]
        if isinstance(item,slice):
            return self.value[item]
        raise TypeError("%s is must a int or slice" % item)


    def __len__(self):
        return len(self.value)

    def __str__(self):
        return "<[a-z]{0.__class__}>".format(self)

    def __getattr__(self, item):
        """
        动态属性
        :param item:
        :return:
        """
        if item == "upper":
            return list(map(chr,range(65,91)))

c = Char()

print(c)
for x in c:
    print(x)

print(len(c))
print(c[2])
print(c[2::2])
print(c.upper)