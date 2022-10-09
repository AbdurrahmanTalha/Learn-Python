def full_name(f_name, l_name):
    name = f"{f_name} {l_name}"
    return name


def long_name(**kargs):
    print(kargs)


def name_mixed(first, last, **name_parts):
    print(first, last, name_parts)


def all_types(first, *args, **kargs):
    print(first)
    print(args)
    print(kargs)


# name = name_mixed(first="chowduhry", last="Choto", middle="abdf")
# long_name(first="Dr. ", last="Chowdhory", middle="Rahman")
# print(name)

all_types("abd", "ddd", "kjk", "lll", "pp", bob="eee")
