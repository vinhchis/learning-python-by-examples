def combined_arguments(arg1, arg2, *args, kwarg1=None, **kwargs):
    print("Fixed arguments:", arg1, arg2)
    print("Additional positional arguments:", args)
    print("Keyword arguments:", kwargs)


combined_arguments("fixed1", "fixed2", "extra1", "extra2",
                   kwarg1="value1", kwarg2="value2")
