import pandas as pd
import os
def split(df, column):
    split_dict = {}
    for i in list(df[column].value_counts().index):
        split_dict[i] = df[df[column] == i]
    
    """Only keep piece of data with more than 10 rows."""
    split_dict = split_dict
    todel = []
    for i in split_dict.keys():
        if len(split_dict[i]) <= 10:
            todel.append(i)
    for i in todel:
        del split_dict[i]

    return split_dict 


if __name__ == "__main__":
    df = pd.read_csv("/home/jds98/10 Academy/Week 2/a-b-hypothesis-for-ad-campaign-peformance-measurement/data/AdSmartABdata.csv")

    dict_browsers = split(df, 'browser')
    dict_platforms = split(df, 'platform_os')

    for col in dict_platforms.keys():
        dict_platforms[col].to_csv(f"/home/jds98/10 Academy/Week 2/a-b-hypothesis-for-ad-campaign-peformance-measurement/data/data_{col}.csv", index=False)
    
    for col in dict_browsers.keys():
        dict_browsers[col].to_csv(f"/home/jds98/10 Academy/Week 2/a-b-hypothesis-for-ad-campaign-peformance-measurement/data/data_{col.replace('/', '' )}.csv", index=False)