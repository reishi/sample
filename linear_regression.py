import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = 5.0 * np.random.randn(x.size) + x
plt.scatter(x, y)

clf = LinearRegression()
clf.fit([[xv] for xv in x], y)
Y = [clf.intercept_ + clf.coef_ * xv for xv in x]
plt.plot(x, Y, 'r')

plt.show()
