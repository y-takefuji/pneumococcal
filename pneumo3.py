import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('data.csv')

# Filter the data for the years 1998 to 2021
df = df[df['Year'].between(1998, 2021)]

# Define the line styles
line_styles = ['-', '--', '-.', ':']

# Define the line widths
line_widths = [1, 3]  # Normal and bold

# Get the unique age groups
age_groups = df['Age Group (years)'].unique()

# Create a new figure with expanded horizontal size
plt.figure(figsize=(12, 6))

# For each age group
for i, age_group in enumerate(age_groups):
    # Filter the data for the current age group
    df_age_group = df[df['Age Group (years)'] == age_group]
    
    # Group by year and sum the frequency counts
    df_grouped = df_age_group.groupby('Year')['Frequency Count'].sum()
    
    # Plot the data with the corresponding line style and width
    df_grouped.plot(linestyle=line_styles[i % len(line_styles)], color='black', linewidth=line_widths[i // len(line_styles)])

# Rotate the x-axis labels
plt.xticks(rotation=90)

# Set x-ticks to have more labels
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MaxNLocator(10))

# Show the legend
plt.legend(age_groups)
plt.xlabel('Year')
plt.ylabel('Invasive Pneumococcal Disease Cases')
plt.title('Invasive Pneumococcal Disease Cases over the years')

# Show the plot
plt.savefig('age.png',dpi=300)
plt.show()

df = pd.read_csv('data.csv')
df = df[(df['Year'] >= 1998) & (df['Year'] <= 2021) & (df['Age Group (years)'] == '<2')]

for year in range(1998, 2022):
    yearly_data = df[df['Year'] == year]
    top_3_serotypes = yearly_data.groupby('IPD Serotype')['Frequency Count'].sum().nlargest(3)
    print(f"{year}: ", end='')
    for serotype, count in top_3_serotypes.items():
        print(f"Serotype {serotype} ({count} cases); ", end='')
    print()
print()

df = pd.read_csv('data.csv')
df = df[(df['Year'] >= 1998) & (df['Year'] <= 2021) & (df['Age Group (years)'] == '50-64')]

for year in range(1998, 2022):
    yearly_data = df[df['Year'] == year]
    top_3_serotypes = yearly_data.groupby('IPD Serotype')['Frequency Count'].sum().nlargest(3)
    print(f"{year}: ", end='')
    for serotype, count in top_3_serotypes.items():
        print(f"Serotype {serotype} ({count} cases); ", end='')
    print()
print()
df = pd.read_csv('data.csv')
df = df[(df['Year'] >= 1998) & (df['Year'] <= 2021) & (df['Age Group (years)'] == '65+')]

for year in range(1998, 2022):
    yearly_data = df[df['Year'] == year]
    top_3_serotypes = yearly_data.groupby('IPD Serotype')['Frequency Count'].sum().nlargest(3)
    print(f"{year}: ", end='')
    for serotype, count in top_3_serotypes.items():
        print(f"Serotype {serotype} ({count} cases); ", end='')
    print()
