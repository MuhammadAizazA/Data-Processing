import numpy as np
# Create a NumPy array
data = np.array([["Name", "Age", "Country"],
                 ["John Doe", 30, "United States"],
                 ["Jane Doe", 28, "Canada"]])
# Save the array to a CSV file
np.savetxt("data/output.csv", data, delimiter=",", fmt="%s")

with open("data/output.csv", "a") as csv_file:
    # Create a NumPy array with the new data
    new_data = np.array([["Joe Smith", 35, "United Kingdom"],
                         ["Mary Smith", 32, "France"]])
    # Append the data to the file
    np.savetxt(csv_file, new_data, delimiter=",", fmt="%s")