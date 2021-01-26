import pandas as pd

df = pd.read_csv('mypath.csv')
df.columns = [c.lower() for c in df.columns]