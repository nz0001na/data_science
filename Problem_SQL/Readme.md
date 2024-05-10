SQL Questions


# Problem 1

[Question Link](https://stackoverflow.com/questions/64608365/write-query-to-display-look-like-in-image)

 The table provided shows all new users signing up on a specific date in the format YYYY-MM-DD. Your query should output the change from one month to the next. Because the first month has no preceding month, your output should skip that row. Your output should look like the following table.

My table data:
        
        ID    DateJoined
        
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








