'''
    Question [Medium]:
    Python Imputing Data Project

    You are provided with a dataset containing personal attributes of individuals.
    Some columns, notably Eye Color and Height, have missing values.
    Your task is to implement mode imputation for the Eye Color column and KNN imputation
    for Height column.
    To ensure results consistency you can utilize KNNimputer from sklearn,impute with the
    following settings:
        - n_neighbors: 5
        - weights: 'uniform'
        - metric: 'nan_euclidean'

    When imputing height values please, round the values to one decimal place.
    After completing the imputation, return the processed data in the form of
    a list of lists, when each inner list represents an individual's data.

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
from sklearn.impute import KNNImputer

csv_file = 'data_missing_values.csv'
df = pd.read_csv(csv_file)

df.head()

eye_mode = df['Eye_Color'].mode()[0]
df['Eye_Color'].fillna(value=eye_mode, inplace=True)

target_data = df[['Height']]
Height_knn = KNNImputer(n_neighbors=5,
                        weights='uniform',
                        metric='nan_euclidean')

imputed_data = Height_knn.fit_transform(target_data)
df['Height'] = imputed_data
df['Height'] = df['Height'].round(1)

result = df.values.tolist()

print(result)






















