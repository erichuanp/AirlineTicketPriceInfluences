import pandas as pd
file_path = 'DirtyDatasets/dataset3.csv'
data = pd.read_csv(file_path)

data['Month'] = data['Date'].apply(lambda x: str(x)[-2:])
data['Year'] = data['Date'].apply(lambda x: str(x)[:4])

data.drop('Date', axis=1, inplace=True)

data = data[['Year', 'Month', 'Value', 'Anomaly']]


new_file_path = 'CleanDatasets/dataset3.csv'
data.to_csv(new_file_path, index=False)