

df.isnan().any()


for  i in df.columns:
    is_na=df[i].isnan().sum()
    if is_na:
        if df[i].dtype=='object':
            df[i]=df[i].fillna().mode()
        elif df[i].dtype=='int':
            df[i]=df[i].fillna().median()
                
