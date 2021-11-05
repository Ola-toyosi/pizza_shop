import sqlite3

conn = sqlite3.connect('pizza.db')
cursor = conn.cursor()

# stmt = 'create table Toppings(name varchar(15) primary key)'
# cursor.execute(stmt)
# stmt = 'create table Prices(product varchar(30) primary key, prices int)'
# cursor.execute(stmt)




# stmt = "insert into Toppings(name) values('Sausage')"
# cursor.execute(stmt)

# stmt = "insert into Toppings(name) values(?)"
# values = [('Chicken',), ('Mushroom',), ('Black Olive',), ('Green Pepper',), ('Red Pepper',), ('Onion',)]
# cursor.executemany(stmt, values)

# stmt = "insert into Prices(product, prices) values(?, ?)"
# values = [('Medium', 2600), ('Large', 3500), ('xLarge', 5000), ('Sausage', 400), ('Pepperoni', 300), ('Chicken', 500),
#           ('Mushroom', 500), ('Black Olive', 100), ('Green Pepper', 200), ('Red Pepper', 150), ('Onion', 100)]
# cursor.executemany(stmt, values)


conn.commit()
conn.close()
