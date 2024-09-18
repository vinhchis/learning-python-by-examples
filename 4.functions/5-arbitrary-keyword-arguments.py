def print_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print("Key:", key, "- Value:", str(value))


# dictionary

print_keyword_arguments(name='Chi',
                        age=26,
                        city="HCM")
