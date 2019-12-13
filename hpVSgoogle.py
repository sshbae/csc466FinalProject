from scipy.cluster import vq
import pandas as pd
import numpy as np

K = 4


def clean_na(df: pd.DataFrame):
    df.fillna(0, inplace=True)
    df = df.astype(np.float)
    df = df.groupby(pd.PeriodIndex(df.columns, freq='Q'), axis=1).mean()
    df = df.drop(df.columns.values[:4], axis=1)
    df = df.drop(df.columns.values[-1], axis=1)
    return df


def get_clusters(avo_toast_trends, avo_trends, ownership_rate, vacancy_rate):
    clusters = {}
    for col in avo_trends:
        avo_centroids, avo_clusts = vq.kmeans2(avo_trends[col], k=K)
        avo_clusters = []
        for clust_no in range(K):
            avo_clusters.append(avo_trends[avo_clusts == clust_no].index.values)

        toast_centroids, toast_clusts = vq.kmeans2(avo_toast_trends[col], k=K)
        toast_clusters = []
        for clust_no in range(K):
            toast_clusters.append(avo_toast_trends[toast_clusts == clust_no].index.values)

        h_owner_centroids, oship_clusts = vq.kmeans2(ownership_rate[col.strftime('%FQ%q')], k=K)
        oship_clusters = []
        for clust_no in range(K):
            oship_clusters.append(ownership_rate[oship_clusts == clust_no].index.values)

        h_vacancy_centroids, vacancy_clusts = vq.kmeans2(vacancy_rate[col.strftime('%FQ%q')], k=K)
        vacancy_clusters = []
        for clust_no in range(K):
            vacancy_clusters.append(vacancy_rate[vacancy_clusts == clust_no].index.values)

        clusters.update({col: {'avo': (avo_centroids, avo_clusters), 'toast': (toast_centroids, toast_clusters),
                               'ownership': (h_owner_centroids, oship_clusters), 'vacancy': (h_vacancy_centroids,
                                                                                             vacancy_clusters)}})
    return clusters


def get_matches(clusters):
    m = pd.DataFrame(index=['avo_own', 'avo_vac', 'tst_own', 'tst_vac'], columns=[list(clusters.keys()) + ['totals',
                                                                                  'averages']])
    m[:] = 0
    matches = {}
    matches['totals'] = {'avo_own': 0, 'avo_vac': 0, 'tst_own': 0, 'tst_vac': 0}
    for quarter in clusters:
        matches[quarter] = {'avo_own': 0, 'avo_vac': 0, 'tst_own': 0, 'tst_vac': 0}

        cluster_nos = list(range(K))
        for clust in clusters[quarter]['avo'][1]:
            best_match = (None, 0)
            for clust_no in cluster_nos:
                clust2 = clusters[quarter]['ownership'][1][clust_no]
                num_matched = len(set(clust).intersection(clust2))
                if num_matched > best_match[1]:
                    best_match = (clust_no, num_matched)
            matches[quarter]['avo_own'] += best_match[1]
            m.loc['avo_own', quarter] += best_match[1]
            matches['totals']['avo_own'] += best_match[1]
            if best_match[0] is not None:
                cluster_nos.remove(best_match[0])

        cluster_nos = list(range(K))
        for clust in clusters[quarter]['toast'][1]:
            best_match = (None, 0)
            for clust_no in cluster_nos:
                clust2 = clusters[quarter]['ownership'][1][clust_no]
                num_matched = len(set(clust).intersection(clust2))
                if num_matched > best_match[1]:
                    best_match = (clust_no, num_matched)
            matches[quarter]['tst_own'] += best_match[1]
            matches['totals']['tst_own'] += best_match[1]
            if best_match[0] is not None:
                cluster_nos.remove(best_match[0])

        cluster_nos = list(range(K))
        for clust in clusters[quarter]['avo'][1]:
            best_match = (None, 0)
            for clust_no in cluster_nos:
                clust2 = clusters[quarter]['vacancy'][1][clust_no]
                num_matched = len(set(clust).intersection(clust2))
                if num_matched > best_match[1]:
                    best_match = (clust_no, num_matched)
            matches[quarter]['avo_vac'] += best_match[1]
            matches['totals']['avo_vac'] += best_match[1]
            if best_match[0] is not None:
                cluster_nos.remove(best_match[0])

        cluster_nos = list(range(K))
        for clust in clusters[quarter]['toast'][1]:
            best_match = (None, 0)
            for clust_no in cluster_nos:
                clust2 = clusters[quarter]['vacancy'][1][clust_no]
                num_matched = len(set(clust).intersection(clust2))
                if num_matched > best_match[1]:
                    best_match = (clust_no, num_matched)
            matches[quarter]['tst_vac'] += best_match[1]
            matches['totals']['tst_vac'] += best_match[1]
            if best_match[0] is not None:
                cluster_nos.remove(best_match[0])
    num_quarters = len(matches) - 1
    matches['averages'] = {'avo_own': 0, 'avo_vac': 0, 'tst_own': 0, 'tst_vac': 0}
    matches['averages']['avo_own'] = matches['totals']['avo_own'] / num_quarters / 51
    matches['averages']['avo_vac'] = matches['totals']['avo_vac'] / num_quarters / 51
    matches['averages']['tst_own'] = matches['totals']['tst_own'] / num_quarters / 51
    matches['averages']['tst_vac'] = matches['totals']['tst_vac'] / num_quarters / 51
    return pd.DataFrame(matches)

def main():
    avo_trends = pd.read_csv('./finalProj/trends_avocado.csv', index_col='state')
    avo_trends = clean_na(avo_trends)
    avo_toast_trends = pd.read_csv('./finalProj/trends_avocado_toast.csv', index_col='state')
    avo_toast_trends = clean_na(avo_toast_trends)
    ownership_rate = pd.read_csv('finalProj/homeownership_rates_by_state.csv', header=0, index_col=0).astype(
        np.float)
    vacancy_rate = pd.read_csv('finalProj/homeowner_vacancy_rates.csv', header=0, index_col=0).astype(np.float)

    clusters = get_clusters(avo_toast_trends, avo_trends, ownership_rate, vacancy_rate)
    matches = get_matches(clusters)
    print(matches['averages'])
    matches.to_csv('./out/hpVSgoogle.csv')

if __name__ == '__main__':
    main()
