import pandas as pd
import numpy as np
from pandas import Series
import random
c=np.zeros((2,3))
bios=pd.read_csv('bios.csv')
print(bios[['height_cm',"name","born_country"]])
print(bios["height_cm"].fillna(33))
print(bios.isna().sum())
print(bios[bios['height_cm']>200])
print(bios[bios["name"].str.contains('Keith')&bios['born_country']=='USA'])
d=['a','b','c','d','e','f']
e=random.choice(d)
print(e)
def g(x,y):
    return 5*x+y
f=np.fromfunction(g,(2,5))
print(f)