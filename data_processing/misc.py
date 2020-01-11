import sql

some_table = sql.Table('some_table')
select = some_table.select()

x = tuple(select)

print(type(x))
