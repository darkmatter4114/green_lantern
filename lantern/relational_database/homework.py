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




def task_2_list_all_customers(cur) -> list:
    cur.execute("""SELECT * FROM Customers ;""")
    list = cur.fetchall()
    return list



def task_3_list_customers_in_germany(cur) -> list:
    cur.execute("""SELECT * FROM Customers WHERE Country='Germany'; """)
    list = cur.fetchall()
    return list




def task_4_update_customer(con):
    cur = con.cursor()
    cur.execute("""UPDATE Customers SET CustomerName='Johnny Depp'  WHERE CustomerID=1; """)




def task_5_delete_the_last_customer(con) -> None:
    cur = con.cursor()
    cur.execute("""DELETE FROM Customers WHERE CustomerID= (SELECT MAX(CustomerID) FROM Customers); """)




def task_6_list_all_supplier_countries(cur) -> list:
    cur.execute("""SELECT Country FROM Suppliers ; """)
    list = cur.fetchall()
    return list




def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    cur.execute("""SELECT Country FROM Suppliers ORDER BY Country DESC; """)
    list = cur.fetchall()
    return list




def task_8_count_customers_by_city(cur):
    cur.execute("""SELECT COUNT(City), City FROM Customers
        GROUP BY City
        ORDER BY COUNT(City) DESC; """)
    list = cur.fetchall()
    print(list)
    return list




def task_9_count_customers_by_country_with_than_10_customers(cur):
    cur.execute("""SELECT COUNT(Country), Country FROM Customers 
        GROUP BY Country 
        HAVING COUNT(Country) > 10; """)
    list = cur.fetchall()
    return list




def task_10_list_first_10_customers(cur):
    cur.execute("""SELECT * FROM Customers 
            LIMIT  10; """)
    list = cur.fetchall()
    return list




def task_11_list_customers_starting_from_11th(cur):
    cur.execute("""SELECT * FROM Customers 
                OFFSET 11; """)
    list = cur.fetchall()
    return list



def task_12_list_suppliers_from_specified_countries(cur):
    cur.execute("""SELECT supplierid,SupplierName,ContactName,City,Country FROM Suppliers WHERE Country='USA' 
    or Country='UK'
    or Country='Japan'; """)
    list = cur.fetchall()
    return list



def task_13_list_products_from_sweden_suppliers(cur):
    cur.execute("""SELECT ProductName FROM Products 
        left join Suppliers 
        on Products.SupplierID = Suppliers.SupplierID
        where Country = 'Sweden'; """)
    list = cur.fetchall()
    return list




def task_14_list_products_with_supplier_information(cur):
    cur.execute("""SELECT productid, ProductName,Unit,Price,Suppliers.Country,Suppliers.City,Suppliers.SupplierName 
    FROM Products 
    LEFT OUTER JOIN Suppliers ON Products.SupplierID= Suppliers. SupplierID; """)
    list = cur.fetchall()
    print(list)
    return list




def task_15_list_customers_with_any_order_or_not(cur):
    cur.execute("""SELECT CustomerName,ContactName,Country,Orders.OrderID
        FROM Customers 
        INNER JOIN Orders ON Orders.CustomerID= Customers.CustomerID; """)
    list = cur.fetchall()
    return list



def task_16_match_all_customers_and_suppliers_by_country(cur):
    cur.execute("""SELECT CustomerName,Customers.Address,Customers.Country AS CustomerCountry,Suppliers.Country AS 
    SupplierCountry,Suppliers.SupplierName from customers 
    full outer join Suppliers on 
    Customers.Country = Suppliers.Country order by CustomerCountry,SupplierCountry; """)
    list = cur.fetchall()
    return list
