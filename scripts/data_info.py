import pandas as pd
import numpy as np


class dataframeInfo:
    ###############################################################################
    # data information extractor
    ################################################################################

    def __init__(self, df: pd.DataFrame):
        """
            Returns a dataframe Info Object with the passed DataFrame Data
            Parameters
        """
        self.df = df
    def find_matrix_correlation(self):
        '''
            Returns the correlation matrix of the passed Dataframe
        '''
        return self.df.corr()
    def find_memory_usage(self):
        '''
            Returns the memory usage of the passed DAtaframe
        '''
        print(f"Current DataFrame Memory Usage of columns is :")
        return self.df.memory_usage()

    def find_total_memory_usage(self):
        '''
            Returns the total memory usage of the passed Dataframe
        '''
        value = self.df.memory_usage(deep=True).sum()
        print(f"Current DataFrame Memory Usage:\n{value}")
        return value
    def find_aggregate(self, stat_list: list):
        '''
            Returns the aggregate of the passed Dataframe
        '''
        try:
            return self.df.agg(stat_list)
        except:
            print("Failed to get aggregates")