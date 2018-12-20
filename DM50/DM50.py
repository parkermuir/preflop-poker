from collections import OrderedDict
#import numpy as np
import random
from os import listdir
import pandas as pd
#import time



def get_filenames(path, suffix=".csv"):
    filenames = listdir(path)
    return [filename for filename in filenames if filename.endswith(suffix)]

['50bb_SB_2x.csv', '50bb_SB_2x_4bet.csv', '50bb_SB_2x_Call3bet.csv', '50bb_SB_2x_Fold3bet.csv',
'50bb_SB_3x.csv', '50bb_SB_3x_4bet.csv', '50bb_SB_3x_Fold3bet.csv', '50bb_SB_Call3bet.csv', '50bb_SB_FoldBTN.csv', '50bb_SB_Limp.csv', '50bb_SB_LimpCall.csv', '50bb_SB_LimpFold.csv']

['50bb_BB_3Bet_2x.csv', '50bb_BB_3Bet_2x_5bet.csv', '50bb_BB_3Bet_2x_Call4bet.csv', '50bb_BB_3Bet_2x_Fold4bet.csv', '50bb_BB_3Bet_3x.csv', '50bb_BB_3bet_3x_5bet.csv', '50bb_BB_3bet_3x_Call4bet.csv', '50bb_BB_3bet_3x_Fold4bet.csv', '50bb_BB_4bet_LRR.csv', '50bb_BB_Call_2x.csv', '50bb_BB_Call_3x.csv', '50bb_BB_Call_LRR.csv', '50bb_BB_CheckLimp.csv', '50bb_BB_Fold_2x.csv', '50bb_BB_Fold_3x.csv', '50bb_BB_Fold_LRR.csv', '50bb_BB_RaiseLimp.csv']

def get_dataframes():
    #creates a dictionary that holds a dataframe of each csv
    filenames = ['50bb_BB_3Bet_2x.csv', '50bb_BB_3Bet_2x_5bet.csv', '50bb_BB_3Bet_2x_Call4bet.csv', '50bb_BB_3Bet_2x_Fold4bet.csv', '50bb_BB_3Bet_3x.csv', '50bb_BB_3bet_3x_5bet.csv', '50bb_BB_3bet_3x_Call4bet.csv', '50bb_BB_3bet_3x_Fold4bet.csv', '50bb_BB_4bet_LRR.csv', '50bb_BB_Call_2x.csv', '50bb_BB_Call_3x.csv', '50bb_BB_Call_LRR.csv', '50bb_BB_CheckLimp.csv', '50bb_BB_Fold_2x.csv', '50bb_BB_Fold_3x.csv', '50bb_BB_Fold_LRR.csv', '50bb_BB_RaiseLimp.csv']

    
    actions_dict = {}
    
    for file in filenames:
        file_df = pd.read_csv("BB" + "/" + file)
        keep_col = ['Combo', 'Weight']
        file_df = file_df[keep_col]

        actions_dict[file] = file_df
    
    return actions_dict


