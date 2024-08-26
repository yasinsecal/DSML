
import pandas as pd

def df_null_summary(df: pd.DataFrame) -> pd.DataFrame: 
    info = pd.DataFrame(df.dtypes).T.rename(index = {0:'Column Type'})
    info = info.append(pd.DataFrame(df.isnull().sum()).T.rename(index = {0:'null values (nb)'}))
    info = info.append(pd.DataFrame(df.isnull().sum()/df.shape[0]*100).T.rename(index = {0:'null values{%}'}))
    return info


def df_add_features(df:pd.DataFrame) -> pd.DataFrame:

    """
    Creates time series features from datetime index.
    """

    df = df.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['hour'] = df['date'].dt.hour
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.weekofyear

    return df
