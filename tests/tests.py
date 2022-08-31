import unittest

import pandas as pd
import logging

import sys, os

sys.path.append(os.path.abspath(os.path.join("./scripts")))

import data_loader

logging.basicConfig(filename='./logfile.log', filemode='a',
                    encoding='utf-8', level=logging.DEBUG)

try:
    test_data = pd.read_csv('./data/AdSmartABdata.csv')
except BaseException:
    logging.warning('file not found or wrong file format')

class TestGetInformations(unittest.TestCase):
    # def setUp(self):
        
    def test_top_values(self):
        self.assertIsInstance(data_loader.top_values(
            test_data, 'yes',3),pd.DataFrame )
    
    def test_load_data(self):
       self.assertIsInstance(data_loader.load_data(
           './data/AdSmartABdata.csv'),pd.DataFrame)

        
if __name__ == "__main__":
    unittest.main()