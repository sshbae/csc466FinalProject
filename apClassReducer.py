import scipy
import pandas as pd
import numpy as np
#from sklearn import tree

def main():
    apdf = pd.read_csv("./finalProj/avoPrices.csv")
    prices = pd.unique(apdf["AveragePrice"])
    prices = np.sort(prices)
    divisions = int(prices.size/5)
    v_cheap = prices[:divisions]
    cheap = prices[divisions:2*divisions]
    moderate = prices[2*divisions:3*divisions]
    expensive = prices[3*divisions:4*divisions]
    v_expensive = prices[4*divisions:]
    
    apdf["PriceRange"] = ""
    for index,rows in apdf.iterrows():
        price = rows["AveragePrice"]
        if np.isin(price,v_cheap):
            apdf.loc[index,"PriceRange"] = "v_cheap"
        elif np.isin(price, cheap):
            apdf.loc[index, "PriceRange"] = "cheap"
        elif np.isin(price, moderate):
            apdf.loc[index,"PriceRange"] = "moderate"
        elif np.isin(price, expensive):
            apdf.loc[index,"PriceRange"] = "expensive"
        elif np.isin(price, v_expensive):
            apdf.loc[index,"PriceRange"] = "v_expensive"

    outfile = open("./finalProj/avoPricesCategor.csv", "w+")
    apdf.to_csv(outfile)

if __name__ == '__main__':
    main()
