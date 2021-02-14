import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create data
d = pd.read_csv("Destinations.csv")
year = d['no_all_Inc_hotels']
sea_levels = d['feedback_score']
plt.scatter(year, sea_levels, edgecolors='r')
plt.xlabel('no_all_inc_hotels')
plt.ylabel(' feedback_score')
plt.title('Correlation between Number of all inc hotels and feedback score')
plt.show()

