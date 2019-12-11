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
    
    apdf["PriceRange"] = ""
    for index,rows in apdf.iterrows():
        price = rows["AveragePrice"]
#how to get this to actually change the df?
        if np.isin(price,vCheap):
            apdf.loc[index,"PriceRange"] = "vCheap"
        elif np.isin(price, cheap):
            apdf.loc[index, "PriceRange"] = "cheap"
        elif np.isin(price, moderate):
            apdf.loc[index,"PriceRange"] = "moderate"
        elif np.isin(price, expensive):
            apdf.loc[index,"PriceRange"] = "expensive"
        elif np.isin(price, vExpensive):
            apdf.loc[index,"PriceRange"] = "expensive"
    print(apdf)

if __name__ == '__main__':
    main()
