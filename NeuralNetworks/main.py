import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)
print(x)
x = np.median(speed)
print(x)
x = stats.mode(speed)
print(x)
x = np.std(speed)
print(x)
x = np.var(speed)
print(x)