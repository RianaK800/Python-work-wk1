import pandas as pd

data = pd.read_csv("Destinations.csv")

condition = data["feedback_score"] <2

print(data[condition])
