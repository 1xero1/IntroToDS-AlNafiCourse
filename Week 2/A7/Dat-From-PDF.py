
from tabula import read_pdf 
import pandas as pd
        
# Read table from pdf file 
df = read_pdf("p.pdf",pages="1-200") #address of pdf file 

Contcatdf = pd.concat(df)
Contcatdf.reset_index(drop=True, inplace=True)

GetDFF=df[0]

gfg_csv_data = df.to_csv('GfG.csv', index = False) 

xx=

for x in range(len(df)):
    GetDF=df[x]
    