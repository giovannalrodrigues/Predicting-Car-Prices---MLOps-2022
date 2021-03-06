"""
Atividade - MLOPS
"""
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
import pandas as pd
import numpy as np

pd.options.display.max_columns = 99
cols = ['symboling',
        'normalized-losses',
        'make', 'fuel-type',
        'aspiration',
        'num-of-doors',
        'body-style',
        'drive-wheels',
        'engine-location',
        'wheel-base', 'length',
        'width', 'height',
        'curb-weight',
        'engine-type',
        'num-of-cylinders',
        'engine-size', 'fuel-system',
        'bore',
        'stroke',
        'compression-rate',
        'horsepower',
        'peak-rpm',
        'city-mpg',
        'highway-mpg',
        'price']
cars = pd.read_csv('imports-85.data', names=cols)
cars.head()

continuous_values_cols = ['normalized-losses',
                          'wheel-base',
                          'length',
                          'width',
                          'height',
                          'curb-weight',
                          'engine-size',
                          'bore',
                          'stroke',
                          'compression-rate',
                          'horsepower',
                          'peak-rpm',
                          'city-mpg',
                          'highway-mpg',
                          'price']
numeric_cars = cars[continuous_values_cols]
numeric_cars.head(5)
numeric_cars = numeric_cars.replace('?', np.nan)
numeric_cars.head(5)
numeric_cars = numeric_cars.astype('float')
numeric_cars.isnull().sum()
numeric_cars = numeric_cars.dropna(subset=['price'])
numeric_cars.isnull().sum()
numeric_cars = numeric_cars.fillna(numeric_cars.mean())
numeric_cars.isnull().sum()
price_col = numeric_cars['price']
numeric_cars = (numeric_cars - numeric_cars.min()) / \
    (numeric_cars.max() - numeric_cars.min())
numeric_cars['price'] = price_col
def knn_train_test(train_col, target_col, df):
    knn = KNeighborsRegressor()
    np.random.seed(1)
    shuffled_index = np.random.permutation(df.index)
    rand_df = df.reindex(shuffled_index)
    last_train_row = int(len(rand_df) / 2)
    train_df = rand_df.iloc[0:last_train_row]
    test_df = rand_df.iloc[last_train_row:]
    knn.fit(train_df[[train_col]], train_df[target_col])
    predicted_labels = knn.predict(test_df[[train_col]])
    mse = mean_squared_error(test_df[target_col], predicted_labels)
    rmse = np.sqrt(mse)
    return rmse
rmse_results = {}
train_cols = numeric_cars.columns.drop('price')
for col in train_cols:
    rmse_val = knn_train_test(col, 'price', numeric_cars)
    rmse_results[col] = rmse_val
rmse_results_series = pd.Series(rmse_results)
rmse_results_series.sort_values()
def knn_train_test(train_col, target_col, df):
    np.random.seed(1)
    shuffled_index = np.random.permutation(df.index)
    rand_df = df.reindex(shuffled_index)
    last_train_row = int(len(rand_df) / 2)
    train_df = rand_df.iloc[0:last_train_row]
    test_df = rand_df.iloc[last_train_row:]
    k_values = [1, 3, 5, 7, 9]
    k_rmses = {}
    for k in k_values:
        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(train_df[[train_col]], train_df[target_col])
        predicted_labels = knn.predict(test_df[[train_col]])
        mse = mean_squared_error(test_df[target_col], predicted_labels)
        rmse = np.sqrt(mse)
        k_rmses[k] = rmse
    return k_rmses
k_rmse_results = {}
train_cols = numeric_cars.columns.drop('price')
for col in train_cols:
    rmse_val = knn_train_test(col, 'price', numeric_cars)
    k_rmse_results[col] = rmse_val
k_rmse_results
for k, v in k_rmse_results.items():
    x = list(v.keys())
    y = list(v.values())
    plt.plot(x, y)
    plt.xlabel('k value')
    plt.ylabel('RMSE')
feature_avg_rmse = {}
for k, v in k_rmse_results.items():
    avg_rmse = np.mean(list(v.values()))
    feature_avg_rmse[k] = avg_rmse
series_avg_rmse = pd.Series(feature_avg_rmse)
sorted_series_avg_rmse = series_avg_rmse.sort_values()
print(sorted_series_avg_rmse)
sorted_features = sorted_series_avg_rmse.index
def knn_train_test(train_cols, target_col, df):
    np.random.seed(1)
    shuffled_index = np.random.permutation(df.index)
    rand_df = df.reindex(shuffled_index)
    last_train_row = int(len(rand_df) / 2)
    train_df = rand_df.iloc[0:last_train_row]
    test_df = rand_df.iloc[last_train_row:]
    k_values = [5]
    k_rmses = {}
    for k in k_values:
        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(train_df[train_cols], train_df[target_col])
        predicted_labels = knn.predict(test_df[train_cols])
        mse = mean_squared_error(test_df[target_col], predicted_labels)
        rmse = np.sqrt(mse)
        k_rmses[k] = rmse
    return k_rmses
k_rmse_results = {}
for nr_best_feats in range(2, 7):
    k_rmse_results['{} best features'.format(nr_best_feats)] = knn_train_test(
        sorted_features[:nr_best_feats],
        'price',
        numeric_cars
    )
k_rmse_results
def knn_train_test(train_cols, target_col, df):
    np.random.seed(1)
    shuffled_index = np.random.permutation(df.index)
    rand_df = df.reindex(shuffled_index)
    last_train_row = int(len(rand_df) / 2)
    train_df = rand_df.iloc[0:last_train_row]
    test_df = rand_df.iloc[last_train_row:]
    k_values = [i for i in range(1, 25)]
    k_rmses = {}
    for k in k_values:
        knn = KNeighborsRegressor(n_neighbors=k)
        knn.fit(train_df[train_cols], train_df[target_col])

        predicted_labels = knn.predict(test_df[train_cols])

        mse = mean_squared_error(test_df[target_col], predicted_labels)
        rmse = np.sqrt(mse)

        k_rmses[k] = rmse
    return k_rmses
k_rmse_results = {}
for nr_best_feats in range(2, 6):
    k_rmse_results['{} best features'.format(nr_best_feats)] = knn_train_test(
        sorted_features[:nr_best_feats],
        'price',
        numeric_cars
    )
k_rmse_results
for k, v in k_rmse_results.items():
    x = list(v.keys())
    y = list(v.values())
    plt.plot(x, y, label="{}".format(k))
plt.xlabel('k value')
plt.ylabel('RMSE')
plt.legend()
