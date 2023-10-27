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
  






























