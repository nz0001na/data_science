# SQL Practice from Coursera: [[The Structured Query Language (SQL)]](https://www.coursera.org/learn/the-structured-query-language-sql?specialization=databases-for-data-scientists)

based on Northwinds database

# Practice some SELECT queries
* List all the products in the Northwinds database showing productid, productname, quantity per unit, unitprice, and unitsinstock.

            select productid, productname, quantityperunit, unitprice, unitsinstock
            from products;
  
* For all employees at Northwinds, list the first name and last name concatenated together with a blank space in-between, and the YEAR when they were hired.
   
            select concat(firstname,' ', lastname), hiredate, date_part('year', hiredate)
            from employees;

* For all products in the Northwinds database, list the productname, unitprice, unitsinstock,  and the total value of the inventory of that product as “Total Value”.  (HINT:  total value = unitsinstock * unitprice.)
   
            select productname, unitprice, unitsinstock, 
                        (unitprice * unitsinstock) AS "Total Value" 
            from products;

* For all employees at Northwinds, list the first name and last name concatenated together with a blank space in-between with a column header “Name”, and the name of the month (spelled out) for each employee’s birthday.  

		select concat(firstname,' ', lastname) as "Name", birthdate, to_char(birthdate, 'month')
		from employees;


# Practice some SELECT queries using the WHERE clause

* List the customerid, companyname, and country for all customers NOT in the U.S.A.

		select customerid, companyname, country
		from customers
		where Country <> 'USA';


* For all products in the Northwinds database, list the productname, unitprice, unitsinstock,  and the total value of the inventory of that product as “Total Value” for all products with a Total Value greater than $1000.  (HINT:  total value = unitsinstock * unitprice)

		select productname, unitprice, unitsinstock, 
			(unitprice * unitsinstock) AS "Total Value" 
		from products
		where (unitprice * unitsinstock) > 1000;
  
* List the productid, productname, and quantityperunit for all products that come in bottles.   

		select productid, productname, quantityperunit 
		from products
		where quantityperunit like '%bottles%';

* List the productid, productname, and unitprice for all products whose categoryid is an ODD number.   (HINT:  categoryid is a one digit integer less than 9 …) 

		select productid, productname, unitprice 
		from products
		where categoryid in (1, 3, 5, 7);

* List the orderid,  customerid, and shippeddate for orders that shipped to Canada  in December 1996 through the end of January 1997.

		select orderid, customerid, shippeddate
		from orders
		where shipcountry = 'Canada' and
		      shippeddate between '1996-12-01' and '1997-01-31';


# Practice some SELECT queries using DATE functions

* List the employeeid, firstname + lastname concatenated as ‘employee’, and the age of the employee  when they were hired.

		SELECT EmployeeID, Firstname || ' ' || Lastname as "employee",
			cast (age(HireDate, BirthDate) as text) AS HIRE_AGE 
		FROM employees;

  		SELECT EmployeeID, concat(Firstname, ' ', Lastname) as "employee",
		 	age(HireDate, BirthDate)::text AS "HIRE_AGE" 
		FROM employees;

* Run a query to calculate your age as of today.  

		SELECT cast (age(now(),'2010-09-08')as text);

		SELECT age(current_date, to_date('20100908', 'YYYYMMDD'))::text as "My Age";
  
* List the employeeid, firstname + lastname concatenated as ‘employee’, and hire date for all employees hired in 1993
		
		SELECT EmployeeID, Firstname || ' ' || Lastname as "employee", hiredate 
		FROM employees 
		WHERE Date_part('year', hiredate) = 1993; 

# Practice some SELECT queries using GROUP functions and GROUP BY

* List the total (unitprice * quantity) as “Total Value” by orderid for the top 5 orders.  (That is, the five orders with the highest Total Value.)  

		SELECT OrderID,  SUM(UnitPrice * Quantity) AS "Total Value"  
		FROM orderdetails 
		GROUP BY OrderID 
		ORDER BY 2 DESC LIMIT 5; 

* How many products does Northwinds have in inventory?
  
		SELECT count(productid)  
		FROM products 
		Where unitsinstock > 0; 


* How many products are out of stock? 

		SELECT count(productid)  
		FROM products 
		Where unitsinstock = 0; 

* From which supplier(s) does Northwinds carry the fewest products? 

		SELECT supplierid, count(productid)  
		FROM products 
		GROUP BY supplierid 
		ORDER BY 2 limit 1;  

* Which Northwinds employees (just show their employeeid) had over 100 orders ? 

		SELECT employeeid, count(orderid) AS "Orders"  
		FROM orders 
		GROUP BY employeeid 
		HAVING count(orderid) > 100 
		ORDER BY 2 desc;  

# Practice some SELECT queries using subqueries

* List the productid, productname, unitprice of the lowest priced product Northwinds sells. 

		select productID, productname, unitprice 
		from products 
		where UnitPrice = ( 
			select MIN(UnitPrice)  
			from products ); 

		select productID, productname, unitprice 
		from products 
		order by unitprice limit 1;

* How many orders in the orders table have a bad customerID (either missing or not on file in the customers table.) 

		SELECT count(orderid) 
		FROM orders 
		WHERE customerid is NULL or
                      customerid NOT IN ( 
				SELECT customerID
	  			FROM customers); 

* Use a subquery in a SELECT to list productname and its totoal values.  

		SELECT productname, ( SELECT SUM(unitprice*quantity)
					from orderdetails O
					where O.productid = P.productid) as Total
		FROM products P; 

* Use a subquery in a FROM to list orderid that have less than 100 quantity. 

		SELECT orderid
		FROM (  SELECT orderid, SUM(quantity)
			FROM orderdetals
			GROUP BY orderid
			HAVING SUM(quantity) < 100
			) as DetailCount;


# Practice some SELECT queries using inner joins

* List each order and its Total Value (unitprice * quantity) for all orders shipping into France in descending Total Value order.  

		SELECT O.orderID, sum(unitprice * quantity) as "Total Value"  
		FROM orders O  
		  JOIN orderdetails D  
		       ON O.orderid = D.orderid 
		    WHERE shipcountry = 'France' 
		GROUP BY O.orderid     
		ORDER BY 2 DESC; 

		SELECT O.orderID, sum(unitprice * quantity) as "Total Value"  
		FROM orders O,  orderdetails D
		WHERE O.orderid = D.orderid and shipcountry = 'France'          
		GROUP BY O.orderid     
		ORDER BY 2 DESC; 

     
* Create a Suppliers List showing Supplier CompanyName, and names of all the products sold by each supplier located in Japan.   
		
		SELECT companyname, productname 
		FROM suppliers S  
			JOIN products P 
			ON S.supplierID = P.supplierID 
		WHERE S.country = 'Japan'; 

		SELECT companyname, productname 
		FROM suppliers S,  products P  
		WHERE S.supplierID = P.supplierID and S.country = 'Japan'; 
  
* Create a “Low Performers” list showing the employees who have less than $100,000 in total sales.  List the employee’s LastName, FirstName followed by their total sales volume (the total dollar value of their orders.)    

		SELECT LastName, Firstname, sum(unitprice * quantity) as "Total Sales"
		FROM employees E 
			JOIN 
			orders O 
			ON E.employeeid  =  O.employeeid
			      JOIN 
			      orderdetails D 
			      ON O.orderid  =  D.orderid
		GROUP BY LastName, FirstName
		HAVING  sum(unitprice * quantity) < 100000;


		SELECT LastName, Firstname, sum(unitprice * quantity) as "Total Sales"
		FROM employees E, orders O, orderdetails D
		WHERE E.employeeid  =  O.employeeid AND O.orderid  =  D.orderid
		GROUP BY LastName, FirstName
		HAVING  sum(unitprice * quantity) < 100000;
  
# Practice some SELECT queries using outer joins

* Are there any Northwinds employees that have no orders?  

		SELECT E.employeeid, lastname, firstname, count(orderid)
		FROM employees E  LEFT OUTER JOIN
		    	orders O  ON E.employeeid = O.employeeid 
		GROUP BY E.employeeid, lastname, firstname
		Having count(orderid) = 0
		ORDER BY E.employeeid;

* Are there any Northwinds customers that have no orders?  

		SELECT C.customerid, companyname, count(orderid)
		FROM customers C  LEFT OUTER JOIN
			orders O  ON C.customerid = O.customerid 
		GROUP BY C.customerid, companyname
		HAVING count(orderid) = 0;

* Are there any Northwinds orders that have bad (not on file) customer numbers?
  
		SELECT DISTINCT O.customerid, count(orderid)
		FROM orders O LEFT OUTER JOIN
			customers C on C.customerid = O.customerid 
		WHERE C.customerid is NULL
		GROUP BY O.customerid;

		SELECT DISTINCT C.customerid, count(orderid)
		FROM customers C RIGHT OUTER JOIN
		 	orders O on C.customerid = O.customerid 
		WHERE C.customerid is NULL
		GROUP BY c.customerid;

* Are there any Shippers that have shipped no Northwinds orders? 

		SELECT S.shipperid, companyname, count(orderid)
		FROM shippers S LEFT OUTER JOIN orders O  
			ON S.shipperid = O.shipvia 
		GROUP BY S.shipperid, companyname
		HAVING count(orderid) = 0;

# Create an Tables/Views
* create an “items” table with the following schema:
  
		itemID integer primary key, 
		itemcode varchar(5) null,
		itemname varchar(40) not null default “ “,
		quantity integer not null default 0,
		price decimal (9,2) not null default 0

Solution: 

		CREATE TABLE items  
		(  
		    itemID     INT           primary key, 
		    itemcode   VARCHAR(5)    NULL, 
		    itemname   VARCHAR(40)   NOT NULL DEFAULT ' ', 
		    quantity   INT           NOT NULL DEFAULT 0, 
		    price      DECIMAL(9,2)  NOT NULL DEFAULT 0 
		  ); 



* Populate your new table with data from the Products table: 
	Consisting of productid, 
	concat(supplierid, categoryid,discontinued),
	productname, unitsinstock, unitprice

Solution: 

		INSERT INTO items 
			(SELECT productid,  
			concat(supplierid, categoryid,discontinued),  
				productname, unitsinstock, unitprice  
			from products); 

* Verify that your table was created and populated successfully

		Select * from items



#  Alter operations

* Change the name of the ‘items’ table to ‘demo’  

		ALTER TABLE items
			RENAME TO "demo";

* Change the name of the ‘itemcode’ column to ‘itemclass’  

		ALTER TABLE demo
			RENAME COLUMN "itemcode" TO "itemclass";

* Add a new column ‘iteminfo’ to your ‘demo’ table  

		ALTER TABLE demo
			ADD COLUMN "iteminfo" VARCHAR(5) NULL;

* Add some data to your new column, copying the values from the itemclass column

		UPDATE demo
			SET "iteminfo" = "itemclass";	

* Take another look at your ALTERed table 

		Select * from demo


# Add/Update/Drop/Truncate Operations

* Insert a new row of data into your "demo" table using format # 1 of the INSERT.  Include these values:
		VALUES
		    (101,'1234','Spicy Grillmate', 12, 1.99, '1234');

Solution:

		INSERT INTO demo
		    		(itemid, itemclass, itemname, quantity, price, iteminfo)
		 	VALUES 
		  		(101,'1234','Spicy Grillmate', 12, 1.99, '1234');

* Insert a new row of data into your "demo" table using format # 2 of the INSERT.  Include these values:

		VALUES
		    (102,'6789','GlobalWarmer', 24, 42.99, '6789');

Solution:
		
		INSERT INTO demo
		    	  VALUES 
		  		(102,'6789','GlobalWarmer', 24, 42.99, '6789');
    
* Update the iteminfo column to ‘0000’ for rows where the itemid is greater than 100

		UPDATE demo
			SET "iteminfo" = '0000'
			WHERE itemid > 100;	

* Delete the rows you just added  to the “demo” table

		DELETE FROM demo
				WHERE itemid > 100;

* Drop the “demo” table  

		DROP TABLE demo

# Use a View
* Create a "TopCustomers" view  using the following SELECT statement to populate the view.

  		SELECT companyname, sum(unitprice * quantity) as "Total Sales"
		from customers C JOIN
		    orders O ON C.customerid  =  O.customerid JOIN
		          orderdetails D ON O.orderid  =  D.orderid
		GROUP BY companyname 
		Order By 2 desc LIMIT 5;

Solution:
		create view topcustomers as 
		SELECT companyname, sum(unitprice * quantity) as "Total Sales"
		  from customers C JOIN
		    orders O ON C.customerid  =  O.customerid JOIN 
		          orderdetails D ON O.orderid  =  D.orderid
		GROUP BY companyname 
		Order By 2 desc LIMIT 5;


* Run a Query Against Your View to ensure that it works

		Select * from topcustomers

# CASE statement

* Let’s drop and recreate your view topcustomers, adding a CASE expression.  Add a third column to your view called “Assessment”.

    Set the Assessment column equal to “Needs Focus” if the customer’s total sales is less than $60,000

    Set the Assessment column equal to “Average” if the customer’s total sales is greater than or equal to $60,000 but less than $115,000.

    Otherwise set the Assessment column equal to “Outstanding” if the customer’s total sales is greater than or equal to $115,000.


		DROP VIEW TopCustomers;
		
		create view TopCustomers as 
		SELECT companyname, sum(unitprice * quantity) as "Total Sales",
		  CASE  
		        WHEN sum(unitprice * quantity) < 60000 THEN 'NeedsFocus'
		        WHEN sum(unitprice * quantity) < 110000 THEN 'Average'
		        ELSE 'Outstanding'
		  END  Assessment
		FROM customers C JOIN
		    orders O ON C.customerid  =  O.customerid JOIN 
		          orderdetails D ON O.orderid  =  D.orderid
		GROUP BY companyname 
		Order By 2 desc LIMIT 5;

* Run a Query Against Your View to see the CASE results
  
		SELECT * FROM TopCustomers


# Projects

* Overview of the Classic Models database

Classic Models Company:  Classic Models is a retailer of diecast miniature collectible model cars, motorcycles, airplanes, trains and ships.  

Classic Models Database : The sample “Classic Models” database consists of the following eight tables: 

1. Customers: stores customer data.
   
2. Products: stores information about the scale models. 

3. ProductLines: stores a list of Classic Models’ various product lines. 

4. Orders: stores sales orders placed by customers. 

5. OrderDetails: stores sales order line items for each sales order. 

6. Payments: stores payments made by customers for purchases

7. Employees: stores all Classic Models employee information 

8. Offices: stores sales office data.


* Query SELECT Problems Using the Classic Models database

For this lab you must create and execute queries against the ClassicModels database to fulfill the requirements listed below.  As a HINT, the expected number of rows in the answer set is shown in parentheses. 

1. List  the names of the cities in alphabetical order where Classic Models has offices. (7)

		select city 
		from offices 
		order by city; 

2. List the EmployeeNumber, LastName, FirstName, Extension for all employees working out of the Paris office. (5)  

		select employeenumber, lastname, firstname, extension  
		from employees 
		where officecode in (
			select officecode
   			from offices
   			where city = 'Paris'
			);

3. List the ProductCode, ProductName, ProductVendor, QuantityInStock and ProductLine for all products with a QuantityInStock between 200 and 1200. (11) 

		select ProductCode, ProductName, ProductVendor, quantityinstock, productline 
		from products  
		where quantityinstock between 200 and 1200; 

4. (Use a SUBQUERY) List the ProductCode, ProductName, ProductVendor, BuyPrice and MSRP for the least expensive (lowest MSRP) product sold by ClassicModels.  (“MSRP” is the Manufacturer’s Suggested Retail Price.)  (1)    

		select Productcode, ProductName,  productvendor, buyprice, MSRP   
		from products  
		where MSRP = ( 
			select min(msrp) from products);

5. What is the ProductName and Profit of the product that has the highest profit (profit = MSRP minus BuyPrice). (1)   

		select ProductName, (MSRP – BuyPrice) as PROFIT   
		from products  
		order by profit desc limit 1;


 		select ProductName, (MSRP – BuyPrice) as PROFIT   
		from products  
		where (MSRP – BuyPrice) = ( 
			select max((MSRP – BuyPrice))
   			from products);
   
6. List the country and the number of customers from that country for all countries having just two  customers.  List the countries sorted in ascending alphabetical order. Title the column heading for the count of customers as “Customers”.(7)   

		Select distinct country, count(*) as customers
		from Customers
		group by country
		having count(*) = 2 
		order by 1 asc; 

7. List the ProductCode, ProductName, and number of orders for the products with exactly 25 orders.  Title the column heading for the count of orders as “OrderCount”. (12)  

		Select p.productcode, productname, count(ordernumber) as OrderCount  	
		from products p join orderdetails o 
			on p.productcode = o.productcode     
		group by productcode, productname 
		having OrderCount = 25;

		Select p.productcode, productname, count(ordernumber) as OrderCount  	
		from products p, orderdetails o 
		where p.productcode = o.productcode     
		group by productcode, productname 
		having OrderCount = 25;

8. List the EmployeeNumber, Firstname + Lastname  (concatenated into one column in the answer set, separated by a blank and referred to as ‘name’) for all the employees reporting to Diane Murphy or Gerard Bondur. (8)  

		Select employeenumber, concat(firstname, ' ', lastname) as "name"
		from employees 
		where reportsto in (
			select employeenumber
			from employees
			where concat(firstname, ' ', lastname) in ('Diane Murphy', 'Gerard Bondur')
		); 


9. List the EmployeeNumber, LastName, FirstName of the president of the company (the one employee with no boss.)  (1)  

		Select employeenumber, lastname, firstname 
		from employees 
		where reportsto is null; 

10. List the ProductName for all products in the “Classic Cars” product line from the 1950’s.  (6)

		Select productname  
		from products 
		where productline = "Classic Cars"  
		 	and productname like "195%" 
		order by productname;

11. List the month name and the total number of orders for the month in 2004 in which ClassicModels customers placed the most orders. (1)  

		select count(ordernumber), monthname(orderdate) as ordermonth  
		from  orders  
		where extract(year from orderdate) = '2004' 
		group by ordermonth 
		order by 1 desc limit 1;

		select count(ordernumber), date_part('month', orderdate)::text as ordermonth  
		from  orders  
		where extract(year from orderdate) = '2004' 
		group by ordermonth 
		order by 1 desc limit 1;


12. List the firstname, lastname of employees who are Sales Reps who have no assigned customers.  (2) 

		select lastname, firstname 
		from employees e left outer join customers c on
			e.employeenumber = c.salesrepemployeenumber 
		where customername is null  
			and jobtitle = "Sales Rep";


13. List the customername of customers from Switzerland with no orders. (2)  

		select customername , country 
		from customers c left outer join orders o on
			c.customernumber = o.customernumber 
		where o.customernumber is null    
			and country = 'Switzerland';
   
14. List the customername and total quantity of products ordered for customers who have ordered more than 1650 products across all their orders.  (8) 

		select customername, sum(quantityordered) as totalq 
		from customers c  
			join orders o on c.customernumber = o.customernumber 
			join orderdetails d on o.ordernumber = d.ordernumber 
		group by customername  
		having totalq > 1650;

		select customername, sum(quantityordered) as totalq 
		from customers c, orders o, orderdetails d
		where c.customernumber = o.customernumber and o.ordernumber = d.ordernumber 
		group by customername  
		having totalq > 1650;


* Query DML/DDL Problems Using the Classic Models database

1.  Create a NEW table named “TopCustomers” with three columns: CustomerNumber (integer), ContactDate (DATE) and  OrderTotal (a real number.)  None of these columns can be NULL.  

		create table if not exists TopCustomers ( 
			Customernumber int not null,  
			ContactDate    DATE not null, 
			OrderTotal  decimal(9,2) not null default 0,
			constraint  PKTopCustomers primary key (CustomerNumber) 
		);

3.  Populate the new table “TopCustomers” with the CustomerNumber, today’s date, and the total value of all their orders (PriceEach * quantityOrdered) for those customers whose order total value is greater than $140,000. (should insert 10 rows )



4.  List the contents of the TopCustomers table in descending OrderTotal sequence. (10) 



5.  Add a new column to the TopCustomers table called OrderCount (integer).



6.  Update the Top Customers table, setting the OrderCount to a random number between 1 and 10.  Hint:  use (RANDOM() *10)



7.  List the contents of the TopCustomers table in descending OrderCount sequence. (10 rows)




8.  Drop the TopCustomers table. (no answer set)  








