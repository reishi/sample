import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import math

population = np.random.randn(5000)
plt.plot([0, population.size], [population.mean(), population.mean()], color='r')

x = []
y = []
yerr = []

for i in range(10, 3500, 100):
    sample = np.random.choice(population, size=i)
    sem = sample.std() / math.sqrt(i)
    x.append(i)
    y.append(sample.mean())
    yerr.append(2 * sem)

plt.errorbar(x, y, yerr=yerr)
plt.show()
