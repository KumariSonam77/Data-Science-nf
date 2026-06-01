#1. Create four Pandas DataFrames:df1,df2,df3,df4 and merge all the df and display the final result.

import pandas as pd

df1 = pd.DataFrame({
    "empId": [1, 2, 3, 4, 5],
    "name": ["Sonam", "Rupam", "Pallavi", "Aman", "Nilam"]
})
df2 = pd.DataFrame({
    "empId": [1, 2, 3, 4, 5],
    "salary": [30000, 35000, 40000, 45000, 50000]
})
df3 = pd.DataFrame({
    "empId": [1, 2, 3, 4, 5],
    "city": ["Delhi", "Mumbai", "Pune", "Chennai", "Kolkata"]
})
df4 = pd.DataFrame({
    "empId": [1, 2, 3, 4, 5],
    "contactNo": [9876534552, 7876543211, 3876543212, 1176543213, 8888543214]
})
result = pd.merge(df1, df2, on="empId")
result = pd.merge(result, df3, on="empId")
result = pd.merge(result, df4, on="empId")
print(result)