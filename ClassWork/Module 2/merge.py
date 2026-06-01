#merge
import pandas as pd
Df1 = pd.DataFrame({"A":[1,2,3,4],"B":["A","B","C","D"]})
Df2 = pd.DataFrame({"A":[1,2,3,4],"D":["a","b","c","d"]})
result = pd.merge(Df1, Df2, on="A")
print(result)

#merge follow on value
Df1 = pd.DataFrame({"A":[1,2,3,4],"B":["A","B","C","D"]})
Df2 = pd.DataFrame({"A":[1,2,3,4],"B":["a","b","c","d"]})
result = pd.merge(Df1, Df2, on="B")
print(result)

#inner merge
Df1 = pd.DataFrame({"A":[1,2,3,4],"B":["A","B","C","D"]})
Df2 = pd.DataFrame({"A":[1,2,3,4],"C":["a","b","c","d"]})
result = pd.merge(Df1, Df2, on="A", how='inner', indicator=True)
print(result)

#outer merge(union)
Df1 = pd.DataFrame({"A":[1,2,3,4],"B":["A","B","C","D"]})
Df2 = pd.DataFrame({"A":[1,2,3,4],"C":["a","b","c","d"]})
result = pd.merge(Df1, Df2, on="A", how='outer', indicator=True)
print(result)

#left merge ()
Df1 = pd.DataFrame({"A":[1,2,3,4],"B":["A","B","C","D"]})
Df2 = pd.DataFrame({"A":[1,5,7,4],"C":["a","b","c","d"]})
result = pd.merge(Df1, Df2, on="A", how='left', indicator=True)
print(result)

#right merge
Df1 = pd.DataFrame({"A":[1,2,3,4],"B":["A","B","C","D"]})
Df2 = pd.DataFrame({"A":[1,5,7,4],"C":["a","b","c","d"]})
result = pd.merge(Df1, Df2, on="A", how='right', indicator=True)
print(result)

#merge on index
Df1 = pd.DataFrame({"A":[1,2,3,4,5],"B":["A","B","C","D","E"]})
Df2 = pd.DataFrame({"A":[1,5,7,4,5],"B":["a","b","c","d","e"]})
result = pd.merge(Df1,Df2,left_index=True,right_index=True)
print(result)

##remove x,y add name use suffixes
Df1 = pd.DataFrame({"A":[1,2,3,4,5],"B":["A","B","C","D","E"]})
Df2 = pd.DataFrame({"A":[1,5,7,4,5],"B":["a","b","c","d","e"]})
result = pd.merge(Df1,Df2,left_index=True,right_index=True,suffixes=('Id','name'))
print(result)