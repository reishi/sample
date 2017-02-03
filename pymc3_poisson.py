import numpy as np
import pandas as pd
import pymc3 as pm
import scipy.stats
import matplotlib.pyplot as plt

x = scipy.stats.uniform.rvs(3, 7, 20)
y = scipy.stats.poisson.rvs(np.exp(1.5 + 0.1 * x))

with pm.Model() as model:
    # Priors
    b0 = pm.Normal('b0', mu=0, sd=100**2)
    b1 = pm.Normal('b1', mu=0, sd=100**2)

    # Likelihood
    z = b0 + b1 * x
    likelihood = pm.Poisson('y', mu=np.exp(z), observed=y)

    # Inference
    step = pm.NUTS()
    trace = pm.sample(2000, step=step)

    # Posterior distributions
    pm.traceplot(trace)
    plt.show()
