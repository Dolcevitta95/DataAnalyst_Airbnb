#drop duplicate rows from dataframe df


print("numero de registros duplicados: ", df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("numero de registros duplicados: ", df.duplicated().sum())


#count the number of duplicated rows in dataframe df

#how to describe object columns in a datagframe