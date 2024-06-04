import pandas as pd

file_path = 'DirtyDatasets/dataset1.csv'
data = pd.read_csv(file_path)

columns_to_convert = ['Consumption(million gallons)', 'Cost(million dollars)', 'Cost per Gallon (dollars)']

# Remove commas and percentages, then convert
for col in columns_to_convert:
    data[col] = data[col].str.replace(',', '')
    data[col] = data[col].str.replace('%', '')
    data[col] = data[col].astype(float)

new_file_path = 'CleanDatasets/dataset1.csv'
data.to_csv(new_file_path, index=False)