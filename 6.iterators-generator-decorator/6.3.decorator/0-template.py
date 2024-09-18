def template_func(func):
    def wrapper():
        print("Begin")
        func()
        print('End')
    return wrapper

@template_func
def greeting():
    print('Hello')

greeting()