import pandas as pd

df = pd.read_csv("./ny.csv")

locationsWithZip = df[['City', 'Property ID', 'ZIP Code', 'Site Sq Ft']]

df['ZIP Code Primary'] = map(lambda row: row.split("-")[0], sitesWithZip['ZIP Code'])

sitesWithZip = df[['City', 'Property ID', 'ZIP Code', 'Site Sq Ft', 'ZIP Code Primary']]

zips = pd.read_csv("./zipcode.csv", dtype={ 'zip': 'S10'})
