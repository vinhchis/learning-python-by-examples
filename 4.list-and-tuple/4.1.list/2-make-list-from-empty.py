def main():
    # Using square brackets
    list1 = [1, 2, 3, 4, 5]
    # Using the list() constructor
    list2 = list([6, 7, 8, 9, 10])
    # List comprehension
    list3 = [x * 2 for x in range(5)]
    # Creating an empty list
    empty_list = []
    # Using the append() method
    append_list = []
    append_list.append(1)
    append_list.append(2)
    append_list.append(3)
    # Using the extend() method
    extend_list = [1, 2, 3]
    extend_list.extend([4, 5, 6])
    # Using repetition operator
    repeated_list = [0] * 5
    # Using list slicing
    original_list = [1, 2, 3, 4, 5]
    sliced_list = original_list[1:4]
    # Using the list() function with other iterables
    string = "hello"
    char_list = list(string)
    # Print the created lists
    print("list1:", list1)
    print("list2:", list2,'with length is', len(list2))
    print("list3:", list3)
    print("empty_list:", empty_list)
    print("append_list:", append_list)
    print("extend_list:", extend_list)
    print("repeated_list:", repeated_list)
    print("sliced_list:", sliced_list)
    print("char_list:", char_list)

if __name__ == "__main__":
    main()