# -*- coding: utf-8 -*-
"""Copy of predicting_car_prices_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BkiDX7DBAxf7TB1oyRlC2Cy4y5iFsgX2
"""

import pandas as pd

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
cars = pd.DataFrame()

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
