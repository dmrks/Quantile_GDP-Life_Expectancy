import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

#1
#print(data.head(5))

#2
life_expectancy= data["Life Expectancy"]

#3 Quartiles = [62.325     72.525     75.4421875]
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25,0.5,0.75])
print(life_expectancy_quartiles)

#3
#plt.hist(life_expectancy)
#plt.show()

#4 life expectancy of 70 years falls into Second Quartile

#6

gdp= data["GDP"]

#7 Median GDP = 2938.0781152500003
median_gdp = np.quantile(gdp,0.5)
#print(median_gdp)

#8

low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

#8 low_gdp_quartiles =  [56.3375  64.34375 71.7375 ]
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25,0.5,0.75])
print(low_gdp_quartiles)

#10 high_gdp_quartiles =  [72.965625 75.15625  80.521875]

high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25,0.5,0.75])
print(high_gdp_quartiles)

#11 Histogram

plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()

#12 In low-GDP Countries 70 years falls into third quartile, in high-GDP countries below first quartile
