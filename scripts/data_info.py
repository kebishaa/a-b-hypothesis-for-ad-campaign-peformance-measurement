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
