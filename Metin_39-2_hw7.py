import sqlite3


def create_database(db_name):
    connect = None
    try:
        connect = sqlite3.connect(db_name)
    except sqlite3.Error as err:
        print(err)
    return connect


def create_table(connect, create_table_sql):
    try:
        cursor = connect.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as err:
        print(err)


def insert_prod(connect, product):  # sen de baglanti connect tu product ta sql_products_base bu listede
    sql = ''' INSERT INTO products (product_title, price, quantity) VALUES(?,?,?)'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as err:
        print(err)


def update_quant(connect, product):
    sql = ''' UPDATE products SET quantity = ? WHERE id=? '''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as err:
        print(err)


def update_price(connect, product):
    sql = ''' UPDATE products SET price = ? WHERE id=? '''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, product)
        connect.commit()
    except sqlite3.Error as err:
        print(err)


def del_prod(connect, id):
    sql = ''' DELETE FROM products WHERE id=? '''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, (id,))
        connect.commit()
    except sqlite3.Error as err:
        print(err)


def select_all_prod(connect):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
        l_product = cursor.fetchall()
        for product in l_product:
            print(product)
    except sqlite3.Error as err:
        print(err)


def select_prod_low(connect, low):
    sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ? '''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, low)
        l_product = cursor.fetchall()
        for product in l_product:
            print(product)
    except sqlite3.Error as err:
        print(err)


def search(connect, name):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%'||?||'%'  '''
    try:
        cursor = connect.cursor()
        cursor.execute(sql, (name,))
        l_product = cursor.fetchall()
        for product in l_product:
            print(product)
    except sqlite3.Error as err:
        print(err)


sql_products_base = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

connect_base = create_database('HW.db')
if connect_base:
    print('Succes')
    # create_table(connect_base, sql_products_base)
    # insert_prod(connect_base, ("Liquid soap with vanilla scent", 50.0, 10))
    # insert_prod(connect_base, ("Children's soap", 30.5, 20))
    # insert_prod(connect_base, ("Shampoo for hair", 80.75, 15))
    # insert_prod(connect_base, ("Toothpaste", 40.25, 25))
    # insert_prod(connect_base, ("Liquid hand soap", 55.0, 12))
    # insert_prod(connect_base, ("Hand cream", 70.0, 18))
    # insert_prod(connect_base, ("Shower gel", 65.25, 22))
    # insert_prod(connect_base, ("Hair conditioner", 90.0, 10))
    # insert_prod(connect_base, ("Lipstick", 120.0, 8))
    # insert_prod(connect_base, ("Toilet water", 150.5, 5))
    # insert_prod(connect_base, ("Face wash", 45.75, 30))
    # insert_prod(connect_base, ("Body lotion", 60.0, 20))
    # insert_prod(connect_base, ("Deodorant", 55.25, 15))
    # insert_prod(connect_base, ("After shave cream", 75.0, 10))
    # insert_prod(connect_base, ("Body oil", 85.5, 12))
    # update_price(connect_base,(115,15))
    # select_all_prod(connect_base)
    # select_prod_low(connect_base, (100, 5))
    search(connect_base, 'soap')
    connect_base.close()
