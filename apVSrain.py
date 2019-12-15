#apVSrain.py >> finalProj/apvrainfall/conf_matrix_*.csv, stats_*.csv

import scipy
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
from sklearn.model_selection import train_test_split, \
    RandomizedSearchCV  # Split the data into training and testing sets

def clean_datasets():
    rfdf = pd.read_csv("./finalProj/avo_rainfall.csv", index_col=[0, 1])
    apdf = pd.read_csv("./finalProj/avoPricesCategor.csv")
    apdf.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1'], inplace=True)
    apdf = apdf[['Month', 'AveragePrice', 'year', 'region',
                 'type_organic', 'type_conventional', 'PriceRange']]
    apdf.rename(columns={'region': 'Region', 'year': 'Year',
                         'type_organic': 'TypeOrganic', 'type_conventional': 'TypeConventional'},
                inplace=True)
    rfdf.rename(columns={'Avg': 'AvgRainfall'}, inplace=True)
    rfdf.to_csv("./finalProj/apvrainfall/avo_rainfall_apvrain.csv", index=['Month', 'Year'])
    apdf.to_csv("./finalProj/apvrainfall/avoPricesCategor_apvrain.csv")
    return rfdf, apdf

def merge_dfs():
    rfdf = pd.read_csv("./finalProj/apvrainfall/avo_rainfall_apvrain.csv", index_col=[0, 1])
    apdf = pd.read_csv("./finalProj/apvrainfall/avoPricesCategor_apvrain.csv")
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
              'NOV', 'DEC']
    for month_id in range(len(months)):
        for year in apdf['Year'].unique():
            if year == 2018 and months[month_id] in ['OCT', 'NOV', 'DEC']:
                continue

            apdf.loc[(apdf['Month'] == month_id+1) & (apdf['Year'] == year), 'AvgRainfall(Current)'] = \
                rfdf.loc[(year, months[month_id]), 'AvgRainfall']
            # print(apdf)
            if month_id >= 6:
                month_offset = month_id - 6
                year_offset = year
            else:
                month_offset = 11-(6-month_id)
                year_offset = year-1
            # month_offset = month_id - 6 if month_id>=6 else 11-(6-month_id)
            # year_offset = year if month_id >=6 else year - 1
            # print('6 mo ', month_offset, year_offset, rfdf.loc[(year_offset, months[month_offset]), 'AvgRainfall'])
            apdf.loc[(apdf['Month'] == month_id+1) & (apdf['Year'] == year), 'AvgRainfall(-6mo)'] = \
                rfdf.loc[(year_offset, months[month_offset]), 'AvgRainfall']
            # print(apdf)
            if month_id >= 3:
                month_offset = month_id - 3
                year_offset = year
            else:
                month_offset = 11-(3-month_id)
                year_offset = year-1
            # month_offset = month_id - 3 if month_id>=3 else 11-(3-month_id)
            # year_offset = year if month_id >=3 else year - 1
            # print('3 mo ', month_offset, year_offset, rfdf.loc[(year_offset, months[month_offset]), 'AvgRainfall'])
            apdf.loc[(apdf['Month'] == month_id+1) & (apdf['Year'] == year), 'AvgRainfall(-3mo)'] = \
                rfdf.loc[(year_offset, months[month_offset]), 'AvgRainfall']
            # print(apdf)
            if month_id >= 1:
                month_offset = month_id - 1
                year_offset = year
            else:
                month_offset = 11-(1-month_id)
                year_offset = year-1
            # month_offset = month_id - 1 if month_id>=1 else 11-(1-month_id)
            # year_offset = year if month_id >=1 else year - 1
            # print('1 mo ', month_offset, year_offset, rfdf.loc[(year_offset, months[month_offset]), 'AvgRainfall'])
            apdf.loc[(apdf['Month'] == month_id+1) & (apdf['Year'] == year), 'AvgRainfall(-1mo)'] = \
                rfdf.loc[(year_offset, months[month_offset]), 'AvgRainfall']
            # print(apdf)
    apdf.drop(columns=['Unnamed: 0', 'AveragePrice'],  inplace=True)
    apdf.to_csv('./finalProj/apvrainfall/avo_rainfall_v_price.csv', index=False)
    return apdf.drop(columns=['Region'])

def get_stats(conf_matrix, name):
    res = pd.DataFrame(columns=['Precision', 'Recall', 'F-Measure'])
    for pricerange in conf_matrix:
        correct_pred = conf_matrix.loc[pricerange, pricerange]
        num_written = conf_matrix.loc[pricerange].sum()
        num_predicted = conf_matrix[pricerange].sum()
        # res.loc[pricerange, 'Hits'] = correct_pred
        # res.loc[pricerange, 'Strikes'] = num_written - correct_pred
        # res.loc[pricerange, 'Misses'] = num_predicted - correct_pred
        # precision - percent of retrieved documents that are relevant
        prec = correct_pred / num_predicted
        res.loc[pricerange, 'Precision'] = round(prec * 100, 2)
        # recall - percent of relevant documents that are retrieved
        recall = correct_pred / num_written
        res.loc[pricerange, 'Recall'] = round(recall* 100, 2)
        # f-measure - harmonic mean of prec and recall
        res.loc[pricerange, 'F-Measure'] = round(100*(2 * prec * recall) / (prec + recall), 3)
    # res.loc['avg', 'Hits'] = round(res['Hits'].mean(), 2)
    # res.loc['avg', 'Strikes'] = round(res['Strikes'].mean(), 2)
    # res.loc['avg', 'Misses'] = round(res['Misses'].mean(), 2)
    res.loc['avg', 'Precision'] = round(res['Precision'].mean(), 2)
    res.loc['avg', 'Recall'] = round(res['Recall'].mean(), 2)
    res.loc['avg', 'F-Measure'] = round(res['F-Measure'].mean(), 3)
    res.to_csv(f'./finalProj/apvrainfall/stats_{name}.csv')


def confusion_matrix(predicted, actual, name):
    conf_matrix = pd.DataFrame(index=np.unique(actual), columns=np.unique(actual))
    conf_matrix = conf_matrix.fillna(0)
    for i in range(len(predicted)):
        conf_matrix.loc[actual[i], predicted[i]] += 1
    # code repurposed from lab 5

    print(conf_matrix)

    conf_matrix.to_csv(f'./finalProj/apvrainfall/conf_matrix_{name}')

    get_stats(conf_matrix, name)

def predict(df: pd.DataFrame, name):
    labels = np.array(df['PriceRange'])
    features = df.drop('PriceRange', axis=1)
    feature_list = list(features.columns)
    features = np.array(features)
    # Using Skicit-learn to split data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.25, random_state=42)
    # Instantiate model with 1000 decision trees
    # https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74
    max_depth = [int(x) for x in np.linspace(10, 110, num=6)]
    max_depth.append(None)
    random_grid = {'n_estimators': [int(x) for x in np.linspace(start=200, stop=2000, num=10)],
                   'max_features': ['auto', 'sqrt'],
                   'max_depth': max_depth,
                   'min_samples_split': [2, 5],
                   'min_samples_leaf': [1, 2, 4],
                   'bootstrap': [True, False]}
    rf = RandomForestClassifier(n_estimators = 400, min_samples_split=2, random_state = 42, max_features='auto', max_depth=90,
                                min_samples_leaf=1, bootstrap=True) # Train the model on training data
    rf.fit(train_features, train_labels)
    print(pd.DataFrame(rf.feature_importances_, index=feature_list))
    predictions = rf.predict(test_features)
    confusion_matrix(predictions, test_labels, name+'_random_fit.csv')

def main():
    clean_datasets()
    df = merge_dfs()
    df3 = df.drop(columns=['AvgRainfall(Current)']).dropna()
    print(df3)
    print("\n\nall 3")
    predict(df3, 'all3')

if __name__ == '__main__':
    main()
