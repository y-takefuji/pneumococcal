import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('data.csv')

# Filter the data for the years 1998 to 2021
df = df[df['Year'].between(1998, 2021)]

# Get the unique age groups
age_groups = df['Age Group (years)'].unique()

# Print the unique age groups and let the user select one
print("Select an age group by number:")
for i, age_group in enumerate(age_groups):
    print(f"{i+1}. {age_group}")
selected_index = int(input("Enter your selection: ")) - 1
selected_age_group = age_groups[selected_index]

# Filter the data for the selected age group
df = df[df['Age Group (years)'] == selected_age_group]

for year in range(1998, 2022):
    yearly_data = df[df['Year'] == year]
    top_3_serotypes = yearly_data.groupby('IPD Serotype')['Frequency Count'].sum().nlargest(3)
    print(f"{year}: ", end='')
    for serotype, count in top_3_serotypes.items():
        print(f"Serotype {serotype} ({count} cases); ", end='')
    print()

