import scipy
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
#from sklearn.cluster import DBSCAN
from scipy.cluster import vq
import matplotlib.pyplot as plt
import json
import avoPriceRegionsToStates

def main():
    apdf = pd.read_csv("./finalProj/avoPricesNumerical.csv")
    apRegions = apdf["region"]
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
#    fig = ff.create_dendrogram(apdf,labels=apRegions.values)
 #   fig.update_layout(width=2500, height=800)
  #  fig.show()

   # fig = ff.create_dendrogram(googdf,labels=list(googdf.index))
   # fig.update_layout(width=800, height=500)
   # fig.show()

    fig = ff.create_dendrogram(toastdf,labels=list(toastdf.index))
    fig.update_layout(width=800, height=500)
    fig.show()
    #numRegions = pd.unique(regions).size

#db scan
    #db = DBSCAN(eps=0.3, min_samples=numRegions/apdf.shape[0]).fit(newdf)
    #dbPlot(db, newdf)

#kmeans
    ap_centroids, ap_clusters = vq.kmeans2(apdf, k=10, minit='points')
    goog_centroids, goog_clusters = vq.kmeans2(googdf, k=10, minit='points')
    toast_centroids, toast_clusters = vq.kmeans2(toastdf, k=10, minit='points')
    apClusters = {}
    googClusters = {}
    toastClusters = {}
    for i in range(ap_clusters.size):
        key = str(ap_clusters[i])
        if key in apClusters:
            apClusters[key].append(apRegions[i])
        else:
            apClusters[key] = [apRegions[i]]

    for i in range(goog_clusters.size):
        key = str(goog_clusters[i])
        if key in googClusters:
            googClusters[key].append(googRegions[i])
        else:
            googClusters[key] = [googRegions[i]]

    for i in range(toast_clusters.size):
        key = str(toast_clusters[i])
        if key in toastClusters:
            toastClusters[key].append(toastRegions[i])
        else:
            toastClusters[key] = [toastRegions[i]]

    print("Avocado Prices", end="")
    for key in apClusters:
        print(f"\nCluster {key}:")
        temp = apClusters[key]
        uniqueStates, countStates = np.unique(temp, return_counts=True)
        count_sort_ind = np.argsort(-countStates)
        uniques = uniqueStates[count_sort_ind]
        print(uniques)

    print("\nGoogle Searches")
    #print(json.dumps(googClusters, indent=2))
    for key in googClusters:
        print(f"\nCluster {key}:")
        print(googClusters[key])

    print("\nToast Searches")
    for key in toastClusters:
        print(f"\nCluster {key}:")
        print(toastClusters[key])

if __name__ == "__main__":
    main()
