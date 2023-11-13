def print_table(obj_list, fields):
    for name in fields:
        print("%10s" % (name), end='')
    print()
    print(('-'*10 + ' ')*len(fields))
    for obj in obj_list:
        for name in fields:
            print("%10s" % (getattr(obj, name)), end='')
        print()