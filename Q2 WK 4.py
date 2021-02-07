##Import Pandas
import pandas as pd

##read the csv file using pd.read._csv
destinations = pd.read_csv("Destinations.csv")

##print out observations for index row 3-8
print(destinations.iloc[3:8])
