from typing import List

import psycopg2


def task_1_add_new_record_to_db(con) -> None:
    cur = con.cursor()
    data = ({'customer_name': 'Thomas'},
            {'contactname': 'David'},
            {'address': 'Some Address'},
            {'city': 'London'},
            {'postalcode': '774'},
            {'country': 'Singapore'},
            )
    cur.execute(
        """INSERT INTO Customers(CustomerName,ContactName,Address,City,PostalCode,Country) VALUES ('Thomas','David', 'Some Address','London','774','Singapore')""")

    # "INSERT INTO Customers(CustomerName,ContactName,Address,City,PostalCode,Country) VALUES \n"
    # "        (%(customer_name)s, %(contactname)s, %(address)s, %(city)s, %(postalcode)s, %(country)s)", data)
    # """
    # Add a record for a new customer from Singapore
    # {    s)s, % (city)    s)s, % (city)
    #     s, % (postalcode)
    #     s, % (country)
    #     s)", data)
    #     s, % (postalcode)
    #     s, % (country)
    #     s)", data)
    #     'customer_name': 'Thomas',
    #     'contactname': 'David',
    #     'address': 'Some Address',
    #     'city': 'London',
    #     'postalcode': '774',
    #     'country': 'Singapore',
    # }
    #
    # Args:
    #     con: psycopg connection
    #
    # Returns: 92 records
    #
    # """


def task_2_list_all_customers(cur) -> list:
    cur.execute("""SELECT * FROM Customers ;""")
    list = cur.fetchall()
    return list
    # """
    # Get all records from table Customers
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 91 records
    #
    # """


def task_3_list_customers_in_germany(cur) -> list:
    cur.execute("""SELECT * FROM Customers WHERE Country='Germany'; """)
    list = cur.fetchall()
    return list

    # # """
    # # List the customers in Germany
    # #
    # # Args:
    # #     cur: psycopg cursor
    # #
    # # Returns: 11 records
    # # """
    # pass


def task_4_update_customer(con):
    cur = con.cursor()
    cur.execute("""UPDATE Customers SET CustomerName='Johnny Depp'  WHERE CustomerID=1; """)

    # """
    # Update first customer's name (Set customername equal to  'Johnny Depp')
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 91 records with updated customer
    #
    # """
    # pass


def task_5_delete_the_last_customer(con) -> None:
    cur = con.cursor()
    # last = cur.execute("""SELECT CustomerID FROM 'Customers' ORDER BY id DESC LIMIT 1; """)
    cur.execute("""DELETE FROM Customers WHERE CustomerID= (SELECT MAX(CustomerID) FROM Customers); """)

    # """
    # Delete the last customer
    #
    # Args:
    #     con: psycopg connection
    # """
    # pass


def task_6_list_all_supplier_countries(cur) -> list:
    cur.execute("""SELECT Country FROM Suppliers ; """)
    list = cur.fetchall()
    return list

    # """
    # List all supplier countries
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 29 records
    #
    # """
    # pass


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    cur.execute("""SELECT Country FROM Suppliers ORDER BY Country DESC; """)
    list = cur.fetchall()
    return list

    # """
    # List all supplier countries in descending order
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 29 records in descending order
    #
    # """
    # pass


def task_8_count_customers_by_city(cur):
    # cur.execute("""SELECT COUNT City FROM Customers; """)
    #  cur.execute("""SELECT CustomerName, COUNT(*) AS CNT
    # FROM Customers
    # GROUP BY City
    # HAVING COUNT(*) > 1; """)
    cur.execute("""SELECT COUNT(City), City FROM Customers
        GROUP BY City
        ORDER BY COUNT(City) DESC; """)
    list = cur.fetchall()
    print(list)
    return list

    #"select city,count(city) from (select * from customers order by customername) as nested group by city order by count(*) desc,city asc"
    #SELECT city, count(city) from customers GROUP BY city ORDER BY COUNT(city) DESC
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 69 records in descending order
    #
    # """
    # pass


def task_9_count_customers_by_country_with_than_10_customers(cur):
    cur.execute("""SELECT COUNT(Country), Country FROM Customers 
        GROUP BY Country 
        HAVING COUNT(Country) > 10; """)
    list = cur.fetchall()
    return list

    # """ORDER BY COUNT(Country) DESC
    # List the number of customers in each country. Only include countries with more than 10 customers.
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 3 records
    # """
    # pass


def task_10_list_first_10_customers(cur):
    cur.execute("""SELECT * FROM Customers 
            LIMIT  10; """)
    list = cur.fetchall()
    return list

    # """
    # List first 10 customers from the table
    #
    # Results: 10 records
    # """
    # pass


def task_11_list_customers_starting_from_11th(cur):
    cur.execute("""SELECT * FROM Customers 
                OFFSET 11; """)
    list = cur.fetchall()
    return list
    # """
    # List all customers starting from 11th record
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 11 records
    # """
    # pass


def task_12_list_suppliers_from_specified_countries(cur):
    cur.execute("""SELECT supplierid,SupplierName,ContactName,City,Country FROM Suppliers WHERE Country='USA' 
    or Country='UK'
    or Country='Japan'; """)
    list = cur.fetchall()
    return list
    # """
    # List all suppliers from the USA, UK, OR Japan
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 8 records
    # """
    # pass


def task_13_list_products_from_sweden_suppliers(cur):
    cur.execute("""SELECT ProductName FROM Products 
        left join Suppliers 
        on Products.SupplierID = Suppliers.SupplierID
        where Country = 'Sweden'; """)
    list = cur.fetchall()
    return list

    # """
    # List products with suppliers from Sweden.
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 3 records
    # """
    # pass


def task_14_list_products_with_supplier_information(cur):
    cur.execute("""SELECT productid, ProductName,Unit,Price,Suppliers.Country,Suppliers.City,Suppliers.SupplierName 
    FROM Products 
    LEFT OUTER JOIN Suppliers ON Products.SupplierID= Suppliers. SupplierID; """)
    list = cur.fetchall()
    print(list)
    return list

    # """
    # List all products with supplier information
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 77 records
    # """
    # pass


def task_15_list_customers_with_any_order_or_not(cur):
    cur.execute("""SELECT CustomerName,ContactName,Country,Orders.OrderID
        FROM Customers 
        INNER JOIN Orders ON Orders.CustomerID= Customers.CustomerID; """)
    list = cur.fetchall()
    return list
    # """
    # List all customers, whether they placed any order or not.
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 213 records
    # """
    # pass


def task_16_match_all_customers_and_suppliers_by_country(cur):
    cur.execute("""SELECT CustomerName,Customers.Address,Customers.Country AS CustomerCountry,Suppliers.Country AS 
    SupplierCountry,Suppliers.SupplierName from customers 
    full outer join Suppliers on 
    Customers.Country = Suppliers.Country order by CustomerCountry,SupplierCountry; """)
    list = cur.fetchall()
    return list
    # """
    # Match all customers and suppliers by country
    #
    # Args:
    #     cur: psycopg cursor
    #
    # Returns: 194 records
    # """
    # pass

# if __name__ == '__main__':
#     con = psycopg2.connect(database='cursor_db', user='cursor', password='very_secret_password', host="localhost",
#                            port="5432")
#     cur = con.cursor()
#
#     task_8_count_customers_by_city(cur)

# ok, you can edit the postgres configuration file:
#
# sudo vim /etc/postgresql/9.6/main/pg_hba.conf
#
# and replace:
#
# local all all peer
#
# with
#
# local all all password
#
# and it should work as expected.
