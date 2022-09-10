import sys
from pandas import read_table

LIB_NAME = 'MAINLIB_TESTING'
CELL_NAME = 'SL_inv_1x'
TEST_NAME = 'test0'

def analyze(lib_name,cell_name,test_name):
    file_name = f'data/{lib_name}/{cell_name}/{test_name}/sim.tran.tran'
    with open(file_name) as f: skips = f.read().split('\n').index('VALUE') # find where data starts
    df = read_table(file_name,skiprows=skips)[:-1] # import as dataframe
    df = df['VALUE'].str.split(expand=True) # separate columns
    df[1] = df[1].astype(float) # convert values to float
    df[2] = (df.index / len(df[0].unique())).astype(int) # create new index
    df = df.pivot(columns=0,values=1,index=2).set_index('time') # reshape data
    df.columns.name = None # fix column name (causes plotly error)
    file_name = f'data/{lib_name}/{cell_name}/{test_name}/transient.csv'
    df.to_csv(file_name) # create csv

if __name__ == '__main__':
    if len(sys.argv) > 1: LIB_NAME = sys.argv[1]
    if len(sys.argv) > 2: CELL_NAME = sys.argv[2]
    if len(sys.argv) > 3: TEST_NAME = sys.argv[3]
    analyze(LIB_NAME,CELL_NAME,TEST_NAME)