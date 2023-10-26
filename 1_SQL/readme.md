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


