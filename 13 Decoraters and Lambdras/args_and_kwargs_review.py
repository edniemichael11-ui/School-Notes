def my_args_example(*args):
    print(args)
    for arg in args:
        print(arg)

#*args mean we can pass a variable number of values to a function 

def my_kwargs_example(**kwargs):
    print(kwargs)
    for kwarg_key, kwarg_val in kwargs.items():
        print(f"{kwarg_key}: {kwarg_val}")

if __name__ == "__main__":
    my_args_example(1, 2, 3, 4)
    my_kwargs_example(name = "Klins", age = 100, exmployed = True)