db_order = ["CustomerName", "ContactName", "Address", "City", "PostalCode", "Country"]

customer_contact = 'Giovanni Rovelli'
customer_address = 'Via Ludovico il Moro 22'

company = 'Hungry Owl All-Night Grocers'
supplier = 'Leka Trading'
product = 'Chang'

made_changes = 'You have made changes to the database. Rows affected: 1'

select_all_request = 'SELECT * FROM Customers'


def select_by_city(city):
    return f"SELECT * FROM Customers WHERE City={city}"


insert_request = "INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)" \
                 " VALUES ('Die Hard', 'John McClane', '2121 Avenue of the Stars', 'Los Angeles', '90067', 'USA');"
insert_string = 'Die Hard John McClane 2121 Avenue of the Stars Los Angeles 90067 USA'

update_request = "UPDATE Customers SET CustomerName='Stark Inc.', ContactName='Pepper Pots', Address='Unknown'," \
                 " City='New-York', PostalCode='00000', Country='USA' WHERE CustomerID=1"
update_string = 'Stark Inc. Pepper Pots Unknown New-York 00000 USA'


def join_request(company_name, supplier_name):
    return f"SELECT * FROM Customers " \
           f"JOIN Orders ON Customers.CustomerId == Orders.CustomerID " \
           f"JOIN OrderDetails ON Orders.OrderID == OrderDetails.OrderID " \
           f"JOIN Products ON OrderDetails.ProductID == Products.ProductID " \
           f"JOIN Suppliers ON Products.SupplierID == Suppliers.SupplierID " \
           f"WHERE CustomerName=\'{company_name}\' AND SupplierName=\'{supplier_name}\'"
