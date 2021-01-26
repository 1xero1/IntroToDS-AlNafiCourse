#Import libraries
from tabula import read_pdf 
import pandas as pd
        
# Read table from pdf file 
df = read_pdf("p.pdf",pages="1-200")

#Skip the first dataframe (on index 0 )
df1=df[1:196]

#concatenate all the dataframes
Contcatdf = pd.concat(df1)

#reset the index
Contcatdf.reset_index(drop=True, inplace=True)

#save the dataframes to csv file
SaveToCsvFile = Contcatdf.to_csv('FBR-2018-200Pages.csv', index = False)  
