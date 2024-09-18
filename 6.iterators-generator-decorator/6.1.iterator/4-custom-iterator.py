class MyIterable:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

my_iterable = MyIterable([10, 20, 30])
for value in my_iterable:
    print(value, end=', ')
# 10, 20, 30, 

print(my_iterable.data)