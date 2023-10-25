# SQL Practice from Coursera: [[The Structured Query Language (SQL)]](https://www.coursera.org/learn/the-structured-query-language-sql?specialization=databases-for-data-scientists)


# Practice some SELECT queries: based on Northwinds database
1. List all the products in the Northwinds database showing productid, productname, quantity per unit, unitprice, and unitsinstock.

            select productid, productname, quantityperunit, unitprice, unitsinstock
            from products;
  
2. For all employees at Northwinds, list the first name and last name concatenated together with a blank space in-between, and the YEAR when they were hired.
   
            select concat(firstname,' ', lastname), hiredate, date_part('year', hiredate)
            from employees;

4. For all products in the Northwinds database, list the productname, unitprice, unitsinstock,  and the total value of the inventory of that product as “Total Value”.  (HINT:  total value = unitsinstock * unitprice.)
   
            select productname, unitprice, unitsinstock, 
                        (unitprice * unitsinstock) AS "Total Value" 
            from products;

6. For all employees at Northwinds, list the first name and last name concatenated together with a blank space in-between with a column header “Name”, and the name of the month (spelled out) for each employee’s birthday.  

