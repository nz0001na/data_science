'''
Question [Medium]:
    Python Missing Data Project

    You are provided with a dataset that contains missing values across different columns.
    Your task is to implement a median imputation method to replace these missing values.
    After the imputation, you should return the resulting data as a list of lists.

    Example input:
    ID,Name,Age,Height,Weight,Eye_Color
    1,Kate,20,5.6,55,5,Blue
    2,Monica,98,,58.6,Brown
    ......

    Example output:
    [[1,'Kate',20, 5.6, 55.5, 'Blue'],
    [2, 'Monica', 98, 5.8, 58.6, 'Brown'],
    ......
    ]


'''



import pandas as pd
import numpy as np

csv_file = 'data_missing_values.csv'
df = pd.read_csv(csv_file)

df.head()

Height_median = df['Height'].median()
df['Height'].fillna(value=Height_median, inplace=True)

Age_median = df['Age'].median()
df['Age'].fillna(value=Age_median, inplace=True)

Weight_median = df['Weight'].median()
df['Weight'].fillna(value=Weight_median, inplace=True)

result = df.values.tolist()

print(result)

















