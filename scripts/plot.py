# Stephen Lawrence 2022

import sys, os
import pandas as pd
pd.options.plotting.backend = "plotly"

TEST_PATH = 'MAINLIB_TESTING/SL_inv_1x/test0'

def plot(test_path): # plot spectre transient simulation results
    df = pd.read_csv(test_path + '/transient.csv',index_col='time') # get transient CSV file
    fig = df.plot(title=test_path + '/transient.csv') # draw a figure for the data
    # fig.write_html(wave_path + '/transient.html') # create HTML (really big file!)
    # fig.write_image(test_path + '/transient.png',scale=3) # create PNG
    return fig

if __name__ == '__main__':
    if len(sys.argv) > 1: TEST_PATH = sys.argv[1]
    plot(TEST_PATH).show()