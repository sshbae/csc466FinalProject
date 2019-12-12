import scipy
import pandas as pd
import numpy as np
#from sklearn import tree

def main():
    apdf = pd.read_csv("./finalProj/avoPrices.csv")
    apdf["Date"] = np.frompyfunc(lambda x:x[5:7],1,1)(apdf["Date"])
    
    apdf = apdf.rename(columns={"Date": "Month"})
    apdf = pd.get_dummies(apdf, columns = ["type"])
    outfile = open("./finalProj/avoPricesMonths.csv", "w+")
    apdf.to_csv(outfile)

if __name__ == '__main__':
    main()
