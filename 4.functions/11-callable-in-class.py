class Adder:
    def __init__(self, value):
        self.value = value
    
    # callable -> cho phép object gọi như 1 hàm
    def __call__(self, x):
        return self.value + x
    
a = Adder(2)
b = a(10)

print("A: " , a.value, "\nb:", b)