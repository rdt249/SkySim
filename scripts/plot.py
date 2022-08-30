# Stephen Lawrence 2022

import sys, os
import pandas as pd
pd.options.plotting.backend = "plotly"

CELL_NAME = '' # global variable to store name of cell

def plot(cell_name,test_name):
    file_name = 'output/' + cell_name + '/' + test_name + '/psf/sim.tran.tran'
    with open(file_name) as f: skips = f.read().split('\n').index('VALUE') # find where data starts
    df = pd.read_table(file_name,skiprows=skips)[:-1] # import as dataframe
    df = df['VALUE'].str.split(expand=True) # separate columns
    df[1] = df[1].astype(float) # convert values to float
    df[2] = (df.index / len(df[0].unique())).astype(int) # create new index
    df = df.pivot(columns=0,values=1,index=2).set_index('time') # reshape data
    df.columns.name = None # fix column name (causes plotly error)
    wave_path = 'output/' + cell_name + '/' + test_name + '/waveform'
    os.makedirs(wave_path,exist_ok=True) # create folder for waveform
    df.to_csv(wave_path + '/waveform.csv') # create csv
    fig = df.plot(title=file_name) # draw a figure for the data
    fig.write_html(wave_path + '/waveform.html') # create HTML
    fig.write_image(wave_path + '/waveform.png') # create PNG
    return fig

if __name__ == '__main__':
    if len(sys.argv) > 1: CELL_NAME = sys.argv[1] # get command-line argument
    else: CELL_NAME = str(input('CELL_NAME: ')) # alternate: get user input
    CELL_NAME = sys.argv[1] if len(sys.argv) > 1 else str(input('CELL_NAME: '))
    TEST_NAME = sys.argv[2] if len(sys.argv) > 2 else str(input('TEST_NAME: '))
    plot(CELL_NAME,TEST_NAME).show() # plot simulation data