
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Sample age distribution data
age_groups = [
    '0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39',
    '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79',
    '80-84', '85+'
]
population = [
    1500000, 1400000, 1300000, 1200000, 1100000, 1000000, 950000, 900000,
    850000, 800000, 750000, 700000, 650000, 600000, 550000, 500000, 450000, 400000
]

# Create the bar chart
plt.figure(figsize=(14, 8))
plt.bar(age_groups, population, color='yellow', edgecolor='black')

# Adding titles and labels
plt.title('Population Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Population')

# Rotate x-axis 
plt.xticks(rotation=45)

# Show the plot
plt.show()
