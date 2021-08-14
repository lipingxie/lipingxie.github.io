import pandas as pd
from collections import defaultdict


dtypes = {
    "lga_name19": "category"
}

df = pd.read_csv(
    "confirmed_cases_14082021.csv",
    dtype=dtypes,
    usecols=list(dtypes) + ["notification_date"],
    parse_dates=["notification_date"]
)

nd = df.groupby("notification_date").size()
df1 = nd.reset_index()
df1.columns =['notification_date', 'TY']
df1["SType"]="All"

lga_list = df['lga_name19'].unique()

for lga in lga_list:
    df2 = df[df['lga_name19'] == lga]
    df2 = df2.groupby("notification_date").size()
    df2 = df2.reset_index()
    df2.columns =['notification_date', 'TY']
    df2["SType"]=lga
    df1 = df1.append(df2)

df1.to_csv('confirmed_cases_14082021_result.csv', index=True, encoding='utf-8')

