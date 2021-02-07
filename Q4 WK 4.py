import pandas as pd

data = pd.read_csv("Destinations.csv")

print(data["feedback_score"].min())


