# Load the Dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read the csv file containing order details
Order_Details = pd.read_csv("iPhone-Sales-Analysis/Order_details-masked.csv")
print(Order_Details)


# Create a 'Time' Column in DateTime Format

# Convert the 'Transaction Date' column to DateTime format
Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'])

# Extract the hour from the 'Time' column and create a new 'Hour' column
Order_Details['Hour'] = (Order_Details['Time']).dt.hour
print(Order_Details)


# Identify the Busiest Hours

# Specify the number of top busiest hours to analyze (n = 24 in this case)
timemost1 = Order_Details['Hour'].value_counts().index.tolist()[:24]
timemost2 = Order_Details['Hour'].value_counts().values.tolist()[:24]


# Combine Hours and Frequencies

tmost = np.column_stack((timemost1,timemost2))

# Display the results in a tabular format
print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost))


# Generate Data for Visualization

timemost = Order_Details['Hour'].value_counts()
timemost1 = []

# Create a list of all 24 hours (0–23)
for i in range(0,23):
	timemost1.append(i)

# Sort frequencies by hour
timemost2 = timemost.sort_index()
timemost2.tolist()

# Convert frequencies to a DataFrame
timemost2 = pd.DataFrame(timemost2)


# Visualize Hourly Sales Trends

# number of purchases made per hour
plt.figure(figsize=(20, 10))

# Add a title to the plot
plt.title('Sales Happening Per Hour (Spread Throughout The Week)',
		fontdict={'fontname': 'monospace', 'fontsize': 30}, y=1.05)

#  Label the axes
plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(timemost1, timemost2, color='m')
plt.grid()
plt.show()

