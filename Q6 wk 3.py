import numpy as np

a=np.arange (1,10).reshape (3,3)
b=np.arange (10,19).reshape (3,3)
c=np.dot(a,b)

print(c)

#vertically stacking
res = np.vstack((a,b))

print(res)

import numpy as np

a=np.arange (1,10).reshape (3,3)
b=np.arange (10,19).reshape (3,3)
c=np.dot(a,b)
sum=np.sum(c)

print(sum)
