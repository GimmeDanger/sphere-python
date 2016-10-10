# coding=utf-8
import pandas as pd
import numpy as np

'''
1) разделить набор данных на кваритили по цене продажи;
2) узнать средний YearBuilt в квартиле, средний Kitchen.
3) перегруппировать по Functional и узнать среднюю цену в классе продаж.
'''

house_prices = pd.read_csv('house_prices.csv')

# Part 1
house_prices_dict = {}
percentiles = np.percentile(house_prices.SalePrice, [0, 25, 50, 75, 100])
for i in range(len(percentiles) - 1):
    house_prices_dict[i] = house_prices[house_prices["SalePrice"] >= percentiles[i]]
    house_prices_dict[i] = house_prices_dict[i][house_prices_dict[i]["SalePrice"] < percentiles[i + 1]]

house_prices_dict[len(percentiles) - 2] = pd.concat([house_prices_dict[len(percentiles) - 2],
                                                     house_prices[house_prices["SalePrice"] == percentiles[
                                                         len(percentiles) - 1]]])
# Part 2
mean_yearbuilt = {}
for key, value in house_prices_dict.iteritems():
    mean_yearbuilt[key] = value["YearBuilt"].mean()

mean_kitchen = {}
for key, value in house_prices_dict.iteritems():
    mean_kitchen[key] = value["KitchenAbvGr"].mean()

# Part 3
mean_functional = {}
functional_grouped = house_prices.groupby("Functional")
for name, group in functional_grouped:
    mean_functional[name] = group["SalePrice"].mean()