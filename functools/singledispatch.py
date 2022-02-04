from functools import singledispatch


# def append_one(obj):
#     if type(obj) == list:
#         return obj + [1]
#     elif type(obj) == set:
#         return obj.union({1})
#     elif type(obj) == str:
#         return obj + str(1)
#     else:
#         print("Unsupported type")
#         return obj


@singledispatch
def append_one(obj):
    pass


@append_one.register(list)
def _(obj):
    return obj + [1]


@append_one.register(set)
def _(obj):
    return obj.union({1})


@append_one.register(str)
def _(obj):
    return obj + str(1)


print(append_one([1, 2, 3]))
