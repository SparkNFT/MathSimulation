from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
import pydot
import networkx as nx
SHILL_TIMES = 10
ROYALTY_FEE = 0.1
SUB_ROYALTY_FEE = 1- ROYALTY_FEE
FIRST_SELL_PRICE = 100
LOSS_RATIO = 0.9
PROBABILITY = 0.2
mu = PROBABILITY*SHILL_TIMES
GENERATION = 5
G = nx.DiGraph()
generation_increase = 0
numbers_generation = []
profits = []
profits_generation = []
total_profit = 0
pre_total = 0
total = 0
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
    global generation_increase
    new_edition = edition(fatherId, editions[fatherId].shill_price*LOSS_RATIO)
    G.add_node(total)
    # print("fatherID: ")
    # print(fatherId)
    # print("total: ")
    # print(total)
    G.add_edge(fatherId, total)
    editions[fatherId].remain_shilltimes -= 1
    editions[fatherId].profit += editions[fatherId].shill_price
    editions.append(new_edition)
    profits.append(0)
    total += 1
    generation_increase += editions[fatherId].shill_price

def claim(NFT_id):
    profits[NFT_id] += editions[NFT_id].profit*SUB_ROYALTY_FEE
    profits[editions[NFT_id].father_id] += editions[NFT_id].profit*ROYALTY_FEE
    editions[NFT_id].profit = 0

def main():
    global total
    global pre_total
    global generation_increase
    root_edition = edition(0, FIRST_SELL_PRICE)
    G.add_node(0)
    editions.append(root_edition)
    profits.append(0)
    total += 1
    for i in range(0, GENERATION):
        rv = poisson.rvs(mu = mu, size = pre_total)
        for j in range(0, pre_total):
            random_variabal = rv[j]
            for k in range(0, random_variabal):
                acceptShill(j)
                # print("haha")
        for x in range(pre_total-1, -1, -1):
            claim(x)
        numbers_generation.append(total - pre_total)
        profits_generation.append(generation_increase)
        pre_total = total
        generation_increase = 0
    print("total number increase: ")
    print(numbers_generation)
    print("profits of generation: ")
    print(profits_generation)
    # print(profits)
    pos = nx.nx_pydot.pydot_layout(G, prog = 'dot')
    nx.draw(G, pos)
    plt.show()



if __name__ == "__main__":
    main()