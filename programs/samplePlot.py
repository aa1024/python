import numpy as np
from scipy import cluster
from matplotlib import pyplot

np.random.seed(123)
tests = np.reshape( np.random.uniform(0,100,60), (30,2) )

print(tests)


#plot variance for each value for 'k' between 1,10
initial = [cluster.vq.kmeans(tests,i) for i in range(1,10)]
pyplot.plot([var for (cent,var) in initial])
pyplot.show()
