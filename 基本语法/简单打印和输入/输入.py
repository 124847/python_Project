class person:
    k = '小明'
    def __init__(self,name,work):
        self.name = name
        self.work = work
    def show(self):
        print(self.name, end = '%s'%self.k)
if __name__ == '__main__':
    x = person('小红','哈哈')
    delattr(person,'show')
    x.show()
