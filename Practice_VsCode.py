import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

print(pd.Series([1,2,3]).array)
s = pd.Series([1,2,3,4])
print(s)

x = [24,25,26]
y = [23,24,25]

plt.plot(x,y)
plt.show()