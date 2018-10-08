# unpacking function arguments

# * tells Python to accept an unlimited amount of unnamed arguments and pass them into the function as a tuple
def unlimited_arguments_tuple(*args):
    print(args)
    for argument in args:
        print(argument)

unlimited_arguments_tuple(*[1,2,3,4])


# ** tells Python to accept and unlimited amount of named arguments and pass them into the function as a dictionary
def unlimited_arguments_dictionary(**keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)

unlimited_arguments_dictionary(name='Harry Potter', age=29)
