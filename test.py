# Creating the histogram without specifying color options
from matplotlib import pyplot as plt

# Data points that fit the bin counts: [1,2): 1, [2,3): 4, [3,4): 3
data = [1.5] + [2.5] * 4 + [3.5] * 3

# Defining bin edges
bins = [1, 2, 3, 4]


plt.hist(data, bins=bins)

# Adjusting x-axis to match the bins
plt.xticks(bins)

# Adding titles and labels
plt.title("Example histogram")
plt.xlabel("t (in ms)")
plt.ylabel("Count")

# Display the plot
plt.show()