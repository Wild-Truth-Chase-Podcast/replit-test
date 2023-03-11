from owid import catalog
import matplotlib.pyplot as plt

# look for Covid-19 data, return a data frame of matches
catalog.find('covid')

# load Covid-19 data from the Our World In Data namespace as a data frame
df = catalog.find('covid', namespace='owid').load()

# load data from other than the default `garden` channel
lung_cancer_tables = catalog.find('lung_cancer_deaths_per_100000_men', channels=['open_numbers'])
df = lung_cancer_tables.iloc[0].load()

#looking at the data, the time and values columns look flipped?
plt.plot(df.loc["alb"].values, df.loc["alb"].index)
plt.show()