import pandas as pd
import numpy as np
import copy
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn import ensemble
from sklearn import tree
from sklearn import metrics

def main():
    df = pd.read_csv("./finalProj/avoWagesFixed.csv")
    df = df.sample(frac=1).reset_index(drop=True)
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop("Date", axis=1, inplace=True)
    df.drop("XLarge Bags", axis=1, inplace=True)

    train, test = train_test_split(df, test_size=0.2)

    train_labes = train["wage"]
    test_labels = test["wage"]

    lab_enc = preprocessing.LabelEncoder()
    train_labels = lab_enc.fit_transform(train_labes)
    print(train_labes)
    print(train_labels)
    test_labels = lab_enc.fit_transform(test_labels)

    train = train.drop("wage", axis=1)
    test = test.drop("wage", axis=1)

    train = pd.get_dummies(train, columns=["type", "region"])
    test = pd.get_dummies(test, columns=["type", "region"])

    parameters = {'max_depth':range(10,40),
    'max_features':range(2, 9), 'min_samples_split':(3, 50)}
    clf = GridSearchCV(tree.DecisionTreeClassifier(), parameters, n_jobs=6)
    clf.fit(train, train_labels)
    model = clf.best_estimator_

    predictions = clf.predict(test)
    accuracy = metrics.accuracy_score(test_labels, predictions)
    print(f"Accuracy: {accuracy}")
    print(f"Best Training Score: {clf.best_score_}")
    print(f"Best Parameters: {clf.best_params_}")
    print("Confusion Matrix: ")
    print(pd.crosstab(test_labels, predictions, rownames=['True'], colnames=['Predicted'], margins=True))

    parameters = {'max_depth':range(10,30), 'n_estimators':range(5,25)}
    clf = GridSearchCV(ensemble.RandomForestClassifier(), parameters, n_jobs=6)
    clf.fit(train, train_labels)
    model = clf.best_estimator_

    predictions = clf.predict(test)
    accuracy = metrics.accuracy_score(test_labels, predictions)
    print(f"Accuracy: {accuracy}")
    print(f"Best Training Score: {clf.best_score_}")
    print(f"Best Parameters: {clf.best_params_}")
    print(pd.crosstab(test_labels, predictions, rownames=['True'], colnames=['Predicted'], margins=True))



if __name__ == '__main__':
    main()