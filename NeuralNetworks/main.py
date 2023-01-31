import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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
x = np.percentile(speed, 75)
print(x)
x = np.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show