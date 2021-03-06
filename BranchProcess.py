from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

SHILL_TIMES = 10
ROYALTY_FEE = 10
FIRST_SELL_PRICE = 100
LOSS_RATIO = 0.9
mu = SHILL_TIMES*0.3
GENERATION = 10

numbers = []
profits = []
total_profit = 0
numbers.append(1)
profits.append(0)
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

for i in range(0, GENERATION): 
        numbers.append(1)



fig, ax = plt.subplots(1, 1)
x = np.arange(poisson.ppf(0.01, mu),
              poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
rv = poisson(mu)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()