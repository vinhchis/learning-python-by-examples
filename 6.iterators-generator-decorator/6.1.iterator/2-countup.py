class SimpleIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    def __next__(self):
        if self.current < self.max_value:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration
# Using the SimpleIterator
iterator = SimpleIterator(5)
try:
    while True:
        value = next(iterator)
        print(value)
except StopIteration:
    pass
#Output:
# 0
# 1
# 2
# 3
# 4