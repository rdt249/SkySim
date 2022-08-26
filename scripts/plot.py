import sys
import pandas as pd
pd.options.plotting.backend = "plotly"

CELL_NAME = ''

def plot(cell_name):
    file_name = cell_name + '/psf/test1.tran.tran'
    df = pd.read_table(file_name,skiprows=167)[:-1]
    df = df['VALUE'].str.split(expand=True)
    df[1] = df[1].astype(float)
    df[2] = (df.index / len(df[0].unique())).astype(int)
    df = df.pivot(columns=0,values=1,index=2).set_index('time')
    df.columns.name = None
    print(df)
    df.plot(title=file_name).show()

if __name__ == '__main__':
    if len(sys.argv) > 1: CELL_NAME = sys.argv[1]
    else: CELL_NAME = str(input('CELL_NAME: '))
    plot(CELL_NAME)
    