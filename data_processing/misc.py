import sql

some_table = sql.Table('some_table')
select = some_table.select()

x = tuple(select)

print(type(x))


def func1():
    print('func1')
    return


def func2():
    print('func2')
    return


def func3():
    print('func3')
    return


def func4():
    print('func4')
    return



def func_caller():
    funcs = [func1(), func2(), func3(), func4()]