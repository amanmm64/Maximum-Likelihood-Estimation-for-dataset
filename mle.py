import pandas as pd
import numpy as np
from scipy.stats import norm
import math 
import array
import matplotlib.pyplot as plt
def MLE(X):	
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
	for i in range(1, n+1):
		a.append(i)
	plt.plot(a,lh,marker='o')
	plt.xticks(np.arange(0,20,1))
	plt.show()
	plt.plot(a,llh, marker='o')
	plt.xticks(np.arange(0, 20, 1))
	plt.show() 
	print("Median =", median)
	return 
