import pandas as pd

#create simple data frame
data = {'Name': ['Alice','Bob','Charles'], 'Age': [25, 30, 35]}
df=pd.DataFrame(data)

#print a 'Hello World" Message with the Dataframe
print("Hello World from pandas!")
print(df)