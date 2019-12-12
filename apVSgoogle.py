import scipy
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

def main():
    apdf = pd.read_csv("./finalProj/avoPricesCategor.csv")
    googdf = pd.read_csv("./finalProj/trends_avocado.csv")
    fig = ff.create_dendrogram(apdf)
    fig.update_layout(width=800, height=500)
    fig.show()

if __name__ == "__main__":
    main()
