# unpacking function arguments
def unlimited_arguments_tuple(*args):
    print(args)
    for argument in args:
        print(argument)

unlimited_arguments_tuple(*[1,2,3,4])


def unlimited_arguments_dictionary(**keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)

unlimited_arguments_dictionary(name='Harry Potter', age=29)
