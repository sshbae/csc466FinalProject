from scipy.cluster import vq
import pandas as pd
import numpy as np


def clean_na(df: pd.DataFrame):
    df.fillna(0, inplace=True)
    df = df.astype(np.float)
    df = df.groupby(pd.PeriodIndex(df.columns, freq='Q'), axis=1).mean()
    return df


if __name__ == '__main__':
    avo_trends = pd.read_csv('./finalProj/trends_avocado.csv', index_col='state')
    avo_trends = clean_na(avo_trends)
    avo_toast_trends = pd.read_csv('./finalProj/trends_avocado_toast.csv', index_col='state')
    avo_toast_trends = clean_na(avo_toast_trends)
    h_owner_rate = pd.read_csv('./finalProj/homeownership_rates_by_state.csv', header=[0, 1], index_col=0).astype(np.float)
    h_vacancy_rate = pd.read_csv('./finalProj/homeowner_vacancy_rates.csv', header=[0, 1], index_col=0).astype(np.float)

    avo_centroids, avo_clusters = vq.kmeans2(avo_trends, k=4)
    toast_centroids, toast_clusters = vq.kmeans2(avo_toast_trends, k=4)
    h_owner_centroids, h_owner_clusters = vq.kmeans2(h_owner_rate, k=4)
    h_vacancy_centroids, h_vacancy_clusters = vq.kmeans2(h_vacancy_rate, k=4)

    print()