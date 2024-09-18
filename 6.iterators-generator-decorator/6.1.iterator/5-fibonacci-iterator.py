class Fibonacci:
    def __init__(self, limit):
        self.count = 0
        self.a , self.b = 0 , 1 # a,b = f(n), f(n+1)
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count > self.limit:
            raise StopIteration

        value = self.a # store a = f(n)
        # swap
        self.a ,self.b = self.b, self.a + self.b # a,b = f(n), f(n+1)
        return value
    
f = Fibonacci(10)

for i in range(10):
    print(i+1,':' , next(f))



# Nhận xét:
# 1 -> 0, => k chung quy luat -> 1 lần so sánh
# 2 -> 1  => k chung quy luat -> 1 lần so sánh
# 3 -> 0 + 1 = 1
# 4 -> 1 + 1 = 2


# NOTE: chuyển sang mô hình này
# f1 -> (f1, f2) = (0, 1) -> có sẵn
# f2 -> (f2, f3) = (1, 2)
# f3 -> (f3, f4) = (2, 3)