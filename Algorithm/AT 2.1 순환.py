def recurse(count):
    if count == 0:
        print('.')
    else:
        print('*')
        recurse(count-1)


recurse(5)

