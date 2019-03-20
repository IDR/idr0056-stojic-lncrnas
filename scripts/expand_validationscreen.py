import pandas as pd

'''
The original annotations for the validation screen
contain several wells and two plates per row.
This script simply splits these rows into one plate 
/ one well per row, as expected as input for the 
metadata plugin.
'''

in_file = "../screen3/idr0056_screen3-library.txt"
out_file = "../screen3/idr0056_screen3-annotation.csv"

df = pd.read_csv(in_file)
header = df.columns.values.tolist()

out = pd.DataFrame(columns = header)

for index, row in df.iterrows():
  for well in row['Well'].split("-"):
    if well:
      newrow1 = row.copy()
      newrow2 = row.copy()
      newrow1['Plate'] = 'plate1'
      newrow2['Plate'] = 'plate2'
      newrow1['Well'] = well
      newrow2['Well'] = well
      out = out.append(newrow1, ignore_index=True)
      out = out.append(newrow2, ignore_index=True)

out.to_csv(out_file, index=False)
