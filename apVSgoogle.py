import scipy
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
#from sklearn.cluster import DBSCAN
from scipy.cluster import vq
import matplotlib.pyplot as plt
import json
import avoPriceRegionsToStates
import plotly.express as px


def plotAvgs():
    avgPricedf = pd.read_csv("./finalProj/avoPricesAvg.csv")
    fig = px.bar(avgPricedf, x='region', y='Total Volume')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    fig.update_layout(title_text='Avocado Purchases by State')
    fig.show()

    fig = px.bar(avgPricedf, x='region', y='AveragePrice')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    fig.update_layout(title_text='Average Avocado Price by State')
    fig.show()


def plotStatesAvo():
    googdf = pd.read_csv("./finalProj/trends_avocado.csv")
    googdf.fillna(0, inplace=True)
    googdf["state"] = np.frompyfunc(lambda x:x[3:],1,1)(googdf["state"])
    googdf["total"] = googdf.sum(axis=1)
    fig = px.bar(googdf,x = 'state', y='total')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    fig.update_layout(title_text='Searches "avocado" by State')
    fig.show()

def plotStatesToast():
    toastdf = pd.read_csv("./finalProj/trends_avocado_toast.csv")
    toastdf.fillna(0, inplace=True)
    toastdf["state"] = np.frompyfunc(lambda x:x[3:],1,1)(toastdf["state"])
    toastdf["total"] = toastdf.sum(axis=1)
    fig = px.bar(toastdf,x = 'state', y='total')
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    fig.update_layout(title_text='Searches "avocado toast" by State')
    fig.show()

def kmeans(df,apRegions):
    ap_centroids, ap_clusters = vq.kmeans2(df, k=10, minit='points')
    apClusters = {}
    for i in range(ap_clusters.size):
        key = str(ap_clusters[i])
        if key in apClusters:
            apClusters[key].append(apRegions[i])
        else:
            apClusters[key] = [apRegions[i]]
    return apClusters

def main():
    plotAvgs()
    plotStatesAvo()
    plotStatesToast()

    apdf = pd.read_csv("./finalProj/avoPricesNumerical.csv")
    apdf = apdf[apdf.region != 'TotalUS']
    apRegions = apdf["region"]
    print(pd.unique(apRegions))
    for i in range(apRegions.size):
        apRegions[i] = avoPriceRegionsToStates.REGION_TO_STATES[apRegions[i]]
    apdf.drop("region", axis=1, inplace = True)

    googdf = pd.read_csv("./finalProj/trends_avocado.csv",index_col = 'state')
    googdf.fillna(0, inplace=True)
    googdf = googdf.astype(np.float)
    googRegions = np.frompyfunc(lambda x:x[3:],1,1)(list(googdf.index))

    toastdf = pd.read_csv("./finalProj/trends_avocado_toast.csv",index_col = 'state')
    toastdf.fillna(0, inplace=True)
    toastdf = toastdf.astype(np.float)
    toastRegions = np.frompyfunc(lambda x:x[3:],1,1)(list(toastdf.index))

#hclustering
   # fig = ff.create_dendrogram(apdf,labels=apRegions.values)
   # fig.update_layout(width=2500, height=800)
   # fig.show()

    fig = ff.create_dendrogram(googdf,labels=list(googdf.index))
    fig.update_layout(width=800, height=500)
    fig.show()

    fig = ff.create_dendrogram(toastdf,labels=list(toastdf.index))
    fig.update_layout(width=800, height=500)
    fig.show()
   #numRegions = pd.unique(regions).size

#db scan
    #db = DBSCAN(eps=0.3, min_samples=numRegions/apdf.shape[0]).fit(newdf)
    #dbPlot(db, newdf)

#kmeans
    apClusters = kmeans(apdf, apRegions)
    googClusters = kmeans(googdf, googRegions)
    toastClusters = kmeans(toastdf, toastRegions)

    print("Avocado Prices", end="")
    for key in apClusters:
        print(f"\nCluster {key}:")
        temp = apClusters[key]
        uniqueStates, countStates = np.unique(temp, return_counts=True)
        count_sort_ind = np.argsort(-countStates)
        uniques = uniqueStates[count_sort_ind]
        print(uniques)

    print("\nGoogle Searches")
    for key in googClusters:
        print(f"\nCluster {key}:")
        print(googClusters[key])

    print("\nToast Searches")
    for key in toastClusters:
        print(f"\nCluster {key}:")
        print(toastClusters[key])

if __name__ == "__main__":
    main()
