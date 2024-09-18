def template_func_1(func):
    def wrapper():
        print("Begin")
        func()
        print('End')
    return wrapper

def template_func_2(func):
    def wrapper():
        print("Begin_2")
        func()
        print('End_2')
    return wrapper

# TODO: if use argument func1 and func2
@template_func_1
@template_func_2 
def greeting():
    print('Hello')

greeting()
# func1 -> func2 -> 'hello'
# Begin
# Begin_2
# Hello
# End_2
# End