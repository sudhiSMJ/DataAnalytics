import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data1=stats.norm(scale=1,loc=0).rvs(1000)
ax=sns.displot(data1,bins=50,kde=True,color='red')
ax.set(xlabel="Norm Dist",ylabel="Freq")
plt.show()

n,p=10,0.3
data=np.random.binomial(n,p,100)
ax=sns.displot(data,bins=20,kde=True,color='blue')
ax.set(xlabel="Binom Dist",ylabel="Freq")
plt.show()

poi_data=np.random.poisson(lam=5,size=1000)
ax=sns.displot(poi_data,kde=False,color='Green')
ax.set(xlabel="Poisson Dist",ylabel="Freq")
plt.show()
