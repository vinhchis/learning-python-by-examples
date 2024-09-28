def template_func(func):
    def wrapper():
        print("Begin")
        func()
        print('End')
    return wrapper

@template_func # use @ notation for a decorator
def greeting():
    print('Hello')

greeting()
# Begin
# Hello
# End  