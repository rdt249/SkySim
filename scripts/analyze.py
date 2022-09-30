# Stephen Lawrence 2022

import sys
from pandas import read_table

TEST_PATH = 'MAINLIB_TESTING/SL_inv_1x/test0' # dev use only -- replaced by command line argument

def analyze(test_path): # create CSV for spectre transient simulation
    file_name = f'{test_path}/sim.tran.tran' # get file name
    with open(file_name) as f: skips = f.read().split('\n').index('VALUE') # find where data starts
    df = read_table(file_name,skiprows=skips)[:-1] # import as dataframe
    df = df['VALUE'].str.split(expand=True) # separate columns
    df[1] = df[1].astype(float) # convert values to float
    df[2] = (df.index / len(df[0].unique())).astype(int) # create new index
    df = df.pivot(columns=0,values=1,index=2).set_index('time') # reshape data
    df.columns.name = None # fix column name (causes plotly error)
    file_name = f'{test_path}/transient.csv'
    df.to_csv(file_name) # create csv

if __name__ == '__main__':
    if len(sys.argv) > 1: TEST_PATH = sys.argv[1]
    analyze(TEST_PATH)