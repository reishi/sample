import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 2.0, 100)
y_true = np.sin(x) + 0.3 * np.random.randn(x.size)
plt.scatter(x, y_true)

clf = svm.SVR()
clf.fit([[xv] for xv in x], y_true)
y_pred = clf.predict([[xv] for xv in x])

plt.plot(x, y_pred)
plt.show()
