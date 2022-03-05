import pandas as pd

#cargar el csv como dataframe de pandas
dfcsv= pd.read_csv('/Users/julio.mendez/Downloads/de-learn01.csv')

valorTotaldeEdades=dfcsv['edad'].sum()
personMenor=dfcsv['edad'].min()
personMeyor=dfcsv['edad'].max()

resultado=dfcsv[dfcsv['edad'] == dfcsv['edad'].max()]

print(resultado['Nombres'])