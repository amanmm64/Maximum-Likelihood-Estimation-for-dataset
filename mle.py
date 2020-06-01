import pandas as pd
import numpy as np
from scipy.stats import norm
import math 
import array
import matplotlib.pyplot as plt
# Here X is the dataset.
mean=X.mean()
std=X.std()
normal=norm.cdf(X,loc=mean,scale=std)
df=pd.DataFrame(normal)
lh=np.product(df)
llh=np.log(lh)
median=llh.median()
llh=abs(llh)
median=abs(median)
c=llh.count()
n=int(c)
a=[]
b=[]
k=1
for i in range(1, n+1):
	a.append(i)
if c>10:
   ax=5
else:
   ax=1     
'''plt.plot(a,lh,marker='o')
plt.xticks(np.arange(0,c+ax,ax))
plt.show()'''
plt.plot(a,llh, marker='o')
plt.xticks(np.arange(0, c+ax,ax))
plt.show()
for j in range(1, n):
    if llh[j]>median:
        m=a[j]
        b.insert(k,m)
        k=k+1
print(k-1, " features/attributes selected")
print(b, "indices are selected")
X=dataset.iloc[:,b]
