from __future__ import division
from itertools import permutations
from collections import OrderedDict
#import numpy as np
import random
from os import listdir
import pandas as pd
#import time

def get_filenames(path, suffix='.csv'):
    filenames = listdir(path)
    return [filename for filename in filenames if filename.endswith(suffix)]

def get_dataframes(filenames, path):
    print 'loading files from ' + path
    #creates a dictionary that holds a dataframe of each csv
    actions_dict = {}
    
    for filename in filenames:
        file_df = pd.read_csv(path + filename)
        keep_col = ['Combo', 'Weight']
        file_df = file_df[keep_col]

        action_name = filename.replace('50bb_','').replace('.csv','')
        actions_dict[action_name] = file_df
    
    return actions_dict

def match_dataframes(handlist, df_dict):
    #checks the hand list against each dataframe in the dictionary. returns a dictionary of action to take (via csv name) + percentage
    match_dict = {}
    
    for key in df_dict:
        df = df_dict[key]
        for h in handlist:
            match_df = df[df['Combo'] == h]

            if not match_df.empty:
                match_dict[key] = round(match_df.iloc[0,1], 3)
                break
            else:
                next
                 
    return match_dict  

def RNG():
   r = random.randint(1,100)    
   r = float(r / 100)
   #print 'r=' , r
   return r    
    
def convertinput(userinput):
    finalhand = 'not recognized' 
    
    if (len(userinput) > 8 or len(userinput) < 4):
        finalhand = 'not recognized' 
        pass
    else:
        input0 = userinput[0:1]
        input1 = userinput[1:2]
        input2 = userinput[2:3]
        input3 = userinput[3:4]
        input4 = userinput[4:5]
        input5 = userinput[5:6] #but gives error when I just do 5 and the input is shorter than 6 characters
        input6 = userinput[6:7]
        input7 = userinput[7:8]

    if len(userinput) == 4:
        finalhand = '%sd%ss%sh%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
    elif (len(userinput) == 5 or len(userinput) == 6):
    #for 5 or 6 character entries only
        if input0 == input1:  #check if first two characters are a pair and do the suiting this way
            if input4 == 's':
                finalhand = '%sc%sh%sh%sd' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == 'd':
                finalhand = '%sh%ss%sh%ss' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == 'r':
                finalhand = '%sd%ss%sh%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == 't':
                finalhand = '%sc%sd%sd%sd' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == 'm':
                finalhand = '%sd%sh%sh%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == 'l':
                finalhand = '%ss%sc%sh%sh' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
        else: #else if the first two aren't a pair, then do the suiting as below
                if input4 == 's':
                    finalhand = '%sh%sh%sd%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == 'd':
                    finalhand = '%sh%sh%ss%ss' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == 't':
                    finalhand = '%sd%sd%sd%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == 'q':
                    finalhand = '%sh%sh%sh%sh' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == 'r':
                    finalhand = '%sd%ss%sh%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == 'm':
                    finalhand = '%sd%sh%sh%sc' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == 'l':
                    finalhand = '%ss%sc%sh%sh' % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                else:
                    finalhand = 'not recognized'
    #if its an 8 character input don't modify it other than the capitalization
    elif len(userinput) == 8:
            finalhand = '%s%s%s%s%s%s%s%s' % (input0.upper(), input1.lower(), input2.upper(), input3.lower(), input4.upper(), input5.lower(), input6.upper(), input7.lower())
    else:
            finalhand = 'not recognized'

    return finalhand


def get_permutations(myp):
    
    Card1 = myp[0:2]
    Card2 = myp[2:4]
    Card3 = myp[4:6]
    Card4 = myp[6:8]
    cardlist = (Card1, Card2, Card3, Card4)
    clength = len(cardlist)
    handlist = []
    
    handlist = [''.join(i) for i in permutations(cardlist, clength)]
    
    return handlist

def small_blind_tree(frequencies):
  print frequencies
  sb_action_1 = OrderedDict([
    ('2x', frequencies['SB_2x']),
    ('3x', frequencies['SB_3x']),
    ('Limp', frequencies['SB_Limp']),
    ('Fold', frequencies['SB_FoldBTN'])
  ])

  print sb_action_1

  for key in sb_action_1:
    if sb_action_1[key] > .99:
      action = key
      break
    else:
      action = 'Mix'
  
  if action == 'Mix':
    for key in sb_action_1:
      if sb_action_1[key] < .01:
       del sb_action_1[key]
      else:
        pass



  else:
    pass


def main():
  sb_files = ['50bb_SB_2x.csv', '50bb_SB_2x_4bet.csv', '50bb_SB_2x_Call3bet.csv', '50bb_SB_2x_Fold3bet.csv','50bb_SB_3x.csv', '50bb_SB_3x_4bet.csv', '50bb_SB_3x_Fold3bet.csv', '50bb_SB_3x_Call3bet.csv', '50bb_SB_FoldBTN.csv', '50bb_SB_Limp.csv', '50bb_SB_LimpCall.csv', '50bb_SB_LimpFold.csv']
  bb_files = ['50bb_BB_3Bet_2x.csv', '50bb_BB_3Bet_2x_5bet.csv', '50bb_BB_3Bet_2x_Call4bet.csv', '50bb_BB_3Bet_2x_Fold4bet.csv', '50bb_BB_3Bet_3x.csv', '50bb_BB_3bet_3x_5bet.csv', '50bb_BB_3bet_3x_Call4bet.csv', '50bb_BB_3bet_3x_Fold4bet.csv', '50bb_BB_4bet_LRR.csv', '50bb_BB_Call_2x.csv', '50bb_BB_Call_3x.csv', '50bb_BB_Call_LRR.csv', '50bb_BB_CheckLimp.csv', '50bb_BB_Fold_2x.csv', '50bb_BB_Fold_3x.csv', '50bb_BB_Fold_LRR.csv', '50bb_BB_RaiseLimp.csv']
  
  sb_dict = get_dataframes(sb_files, 'SB/')   
  bb_dict = get_dataframes(bb_files, 'BB/')

  handlist = get_permutations(convertinput('AK74d'))

  sb_matches = match_dataframes(handlist, sb_dict)
  small_blind_tree(sb_matches)

  # sb_actions_list = []
  # for key in sb_dict:
  #   print key

  # print bb_actions_list
 

  

    # while True:
    #    rawinput = raw_input('Input PLO Hand: ').lower()
    #    if rawinput == 'quit':
    #         print 'blade runner p: gg'
    #         print 'blade runner p: m8'
    #         return
    #    else:
    #         convertedinput = convertinput(rawinput) #take raw input and convert it to a searchable plo hand
            
    #         if convertedinput == 'not recognized': #error catch
    #             print ''
    #             print 'Oops, try again'
    #         else:
    #             handlist = get_permutations(convertedinput)
    #             match_dict = match_dataframes(handlist,df_dict)
    #             print ''
    #             print '--------',convertedinput[0:2]+','+convertedinput[2:4]+','+convertedinput[4:6]+','+convertedinput[6:],'--------' 
    #             print ''
    #             print'SB:'
    #             small_blind_new(match_dict)
    #             print ''
    #             print 'BB:'
    #             big_blind_new(match_dict)
    #             print ''

main() 