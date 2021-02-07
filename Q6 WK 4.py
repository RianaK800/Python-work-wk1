import pandas as pd

data = pd.read_csv("Destinations.csv")

myfilter = data["no_all_Inc_hotels"]>9

print(myfilter)


