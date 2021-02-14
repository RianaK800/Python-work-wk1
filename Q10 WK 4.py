import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('Destinations.csv')
dest_data = df["Destinations"]
feedback_data = df["feedback_score"]

colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#8c664b", "#8c764b", "#8c864b", "#8c964b", "#9c514b", "#2c524b", "#3c534b", "#4c544b", "#8c554b", "#1c564b"]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  

plt.pie(feedback_data, labels=dest_data, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Destinations and highest scores")
plt.show()
