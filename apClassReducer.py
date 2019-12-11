import scipy
import pandas as pd
import numpy as np
#from sklearn import tree

def main():
    apdf = pd.read_csv("./finalProj/avoPrices.csv")
    prices = pd.unique(apdf["AveragePrice"])
    prices = np.sort(prices)
    divisions = int(prices.size/5)
    print(f"max is {prices.max()}")
    print(f"min is {prices.min()}")
    vCheap = prices[:divisions]
    cheap = prices[divisions:2*divisions]
    moderate = prices[2*divisions:3*divisions]
    expensive = prices[3*divisions:4*divisions]
    vExpensive = prices[4*divisions:]
    print(f"vcheap: {vCheap}\ncheap: {cheap}\nmod: {moderate}\nexpensive: {expensive}\nvExpensive: {vExpensive}")


if __name__ == '__main__':
    main()
