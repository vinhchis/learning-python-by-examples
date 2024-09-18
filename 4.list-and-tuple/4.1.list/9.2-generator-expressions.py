# Cú pháp cơ bản
gen_exp = (expression for item in iterable)

# Ví dụ 1: Generator expression để tạo bình phương các số
squares_gen = (x**2 for x in range(10))
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Ví dụ 2: Generator expression với điều kiện
even_squares_gen = (x**2 for x in range(10) if x % 2 == 0)
print(list(even_squares_gen))  # [0, 4, 16, 36, 64]

# Ví dụ 3: So sánh với list comprehension
list_comp = [x**2 for x in range(1000000)]  # Tạo và lưu trữ tất cả giá trị ngay lập tức
gen_exp = (x**2 for x in range(1000000))    # Chỉ tạo generator object, không tính toán ngay

print(type(list_comp))  # <class 'list'>
print(type(gen_exp))    # <class 'generator'>

# Ví dụ 4: Sử dụng generator expression trong hàm
sum_of_squares = sum(x**2 for x in range(10))
print(sum_of_squares)  # 285

# Ví dụ 5: Generator expression với nhiều vòng lặp
flat_gen = (item for sublist in [[1, 2], [3, 4], [5, 6]] for item in sublist)
print(list(flat_gen))  # [1, 2, 3, 4, 5, 6]

# Ví dụ 6: Sử dụng generator expression để xử lý file lớn
with open('large_file.txt', 'r') as file:
    line_count = sum(1 for line in file)
print(f"Số dòng trong file: {line_count}")