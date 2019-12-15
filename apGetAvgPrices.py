import scipy
import pandas as pd
import numpy as np
#from sklearn import tree
import avoPriceRegionsToStates

def main():
    apdf = pd.read_csv("./finalProj/avoPrices.csv")
    apdf = apdf.drop(apdf.columns[0], axis = 1)
    apdf["Date"] = np.frompyfunc(lambda x:x[5:7],1,1)(apdf["Date"])
    
    apdf = apdf.rename(columns={"Date": "Month"})
    #apdf = apdf.groupby(["region", "type"],as_index=False).mean()
    apdf = apdf.drop(columns=['year', '4046','4225','4770','Total Bags','Small Bags','Large Bags','XLarge Bags','type'])
    apdf = apdf.groupby(["region"],as_index=False).agg({'Total Volume':'sum','AveragePrice':'mean'})
    #apdf = pd.get_dummies(apdf, columns = ["type"])
    apdf = apdf.groupby(["region"], as_index=False).agg({'Total Volume':'sum','AveragePrice':'mean'})
    apdf = apdf[apdf.region != 'TotalUS']

    for index,row in apdf.iterrows():
        apdf.loc[index,"region"] = avoPriceRegionsToStates.REGION_TO_STATES[row["region"]]
    #apdf.drop("region", axis=1, inplace = True)
    apdf = apdf.groupby(["region"], as_index=False).mean()

    outfile = open("./finalProj/avoPricesAvg.csv", "w+")
    apdf.to_csv(outfile, index=False)

if __name__ == '__main__':
    main()
