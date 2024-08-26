
import pandas as pd

def df_null_summary(df: pd.DataFrame) -> pd.DataFrame: 
    info = pd.DataFrame(df.dtypes).T.rename(index = {0:'Column Type'})
    info = info.append(pd.DataFrame(df.isnull().sum()).T.rename(index = {0:'null values (nb)'}))
    info = info.append(pd.DataFrame(df.isnull().sum()/df.shape[0]*100).T.rename(index = {0:'null values{%}'}))
    return info

