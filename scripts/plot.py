# Stephen Lawrence 2022

import sys, os
import pandas as pd
import plotly.express as px

CELL_PATH = 'MAINLIB_TESTING/SL_inv_1x'

def get_facet(file,tag):
    df = pd.read_csv(file,index_col=0)
    df = df.stack().reset_index().set_index(df.index.name).rename(columns={'level_1':'node',0:'value'})
    df['test'] = tag
    return df

def plot(cell_path): # plot spectre transient simulation results
    meta = pd.read_csv(cell_path + '/meta.csv',index_col=0)
    df = pd.DataFrame()
    for test in meta['folder']:
        df = pd.concat([df,get_facet(test + '/transient.csv',test.split('/')[-1])])
    fig = px.line(df,color='node',animation_frame='test',title=cell_path)
    # fig.write_html(wave_path + '/transient.html') # create HTML (really big file!)
    # fig.write_image(test_path + '/transient.png',scale=3) # create PNG
    return fig

if __name__ == '__main__':
    if len(sys.argv) > 1: CELL_PATH = sys.argv[1]
    plot(CELL_PATH).show()