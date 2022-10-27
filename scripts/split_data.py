import pandas as pd
import os
import preprocess

def split(df, column):
    split_dict = {}
    for i in list(df[column].value_counts().index):
        split_dict[i] = df[df[column] == i]
    
    """Only keep piece of data with more than 30 rows."""
    split_dict = split_dict
    todel = []
    for i in split_dict.keys():
        if len(split_dict[i]) <= 30:
            todel.append(i)
    for i in todel:
        del split_dict[i]

    return split_dict 


if __name__ == "__main__":

    df = pd.read_csv("./dSmartABdata.csv")

    df = preprocess.nonResponse(df)

    dict_browsers = split(df, 'browser')
    dict_platforms = split(df, 'platform_os')

    for col in dict_platforms.keys():
        dict_platforms[col].to_csv(os.path.join("./data/",'data_'+str(col)+".csv"), index=False)
    
    for col in dict_browsers.keys():
        dict_browsers[col].to_csv(os.path.join("./data/","data_"+col.replace('/', '' )+".csv"), index=False)