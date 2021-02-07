import pandas as pd

data = pd.read_csv("Destinations.csv")

print(data["no_all_Inc_hotels"].mean())
