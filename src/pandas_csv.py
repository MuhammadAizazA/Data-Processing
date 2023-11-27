import pandas as pd

data = pd.DataFrame([["John Doe", 30, "United States"],
                     ["Jane Doe", 28, "Canada"]])

data.to_csv("data/output_pandas.csv", index=False, header=False)