print("gittest01.py")

sum = lambda a,b: a*b
print(sum(3,5))
sum2 = lambda a,b: a/b
print(sum2(3,5))

import numpy as np
print(np.__version__)

ar4 = [1,2,3,4,5,6]
print(ar4)
ar4 = np.array([1,2,3,4,5,6])
print(ar4)
ar4 = np.array([1,2,3,4,5,6]).reshape((3,2))
print(ar4)
