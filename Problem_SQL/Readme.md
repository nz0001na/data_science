SQL Questions


# Problem 1

[Question Link](https://stackoverflow.com/questions/64608365/write-query-to-display-look-like-in-image)

 The table provided shows all new users signing up on a specific date in the format YYYY-MM-DD. Your query should output the change from one month to the next. Because the first month has no preceding month, your output should skip that row. Your output should look like the following table.

My table data: userlog
        
        ID    joindate
        
        1     2017-01-06
        
        2     2017-01-12
        
        3     2017-01-16
        
        4     2017-01-25
        
        5     2017-02-05
        
        6     2017-02-07
        
        7     2017-02-21
        
        8     2017-03-05
        
        9     2017-03-07
        
        10    2017-03-14
        
        11    2017-03-16
        
        12    2017-03-25
        
        13    2017-03-25
        
        14    2017-03-25
        
        15    2017-03-25
        
        16    2017-03-26
        
        17    2017-04-05
        
        18    2017-04-14
        
        19    2017-04-21
        
        20    2017-05-07
        
        23    2017-05-14
        
        24    2017-05-16
        
        25    2017-05-25
        
        26    2017-05-25
        
        27    2017-05-25
        
        28    2017-05-25


I want this output: count all records from every month and subtract it from the next month record. 
As shown in the following picture:
![arch](CuOVa.png)


Solution: 

Use lag(), available in MySQL 8.0:

        select date_format(joindate, '%Y-%m-01') as Month,
            count(*) - lag(count(*), 1, 0) over(order by date_format(joindate, '%Y-%m-01')) MonthToMonthChange
        from userlog
        group by Month
        
Note that I changed the logic to truncate dates to the first of month to use date_format().

In earlier versions, you can use a correlated subquery:

      select date_format(joindate, '%Y-%m-01') Month,
          count(*) - (
              select count(*)
              from userlog l1
              where l1.joindate >= date_format(l.joindate, '%Y-%m-01') - interval 1 month
                and l1.joindate <  date_format(l.joindate, '%Y-%m-01')
          ) MonthToMonthChange
      from userlog l
      group by Month
      LIMIT 12 OFFSET 1







