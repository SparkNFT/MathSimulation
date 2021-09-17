from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
SHILL_TIMES = 10
ROYALTY_FEE = 0.1
SUB_ROYALTY_FEE = 1- ROYALTY_FEE
FIRST_SELL_PRICE = 100
LOSS_RATIO = 0.9
PROBABILITY = 0.3
mu = PROBABILITY*SHILL_TIMES
GENERATION = 10

numbers = []
profits = []
total_profit = 0
pre_total = 0
total = 0
numbers.append(1)
profits.append(0)
rv = poisson.rvs(mu= mu , size = 500)
print(rv)
class edition:
    def __init__(self, father_id,  shill_price):
        self.father_id = father_id
        self.remain_shilltimes = SHILL_TIMES
        self.shill_price = shill_price
        self.profit = 0

editions = []

def acceptShill(fatherId):
    if (editions[fatherId].remain_shilltimes == 0):
        return
    global total
    new_edition = edition(fatherId, editions[fatherId].shill_price*LOSS_RATIO)
    editions[fatherId].remain_shilltimes -= 1
    editions[fatherId].profit += editions[fatherId].shill_price
    editions.append(new_edition)
    total += 1


def main():
    global total
    global pre_total
    root_edition = edition(0, FIRST_SELL_PRICE)
    editions.append(root_edition)
    total += 1
    for i in range(0, GENERATION):
        rv = poisson.rvs(mu = mu, size = pre_total)
        for j in range(0, pre_total):
            random_variabal = rv[j]
            for k in range(0, random_variabal):
                acceptShill(j)
                # print("haha")
        pre_total = total



if __name__ == "__main__":
    main()