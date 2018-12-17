# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:01:51 2017

@author: Parker
"""
from __future__ import division
from itertools import permutations
from collections import OrderedDict
#import numpy as np
import random
from os import listdir
import pandas as pd
#import time


# def get_filenames(path, suffix=".csv"):
#     filenames = listdir(path)
#     return [filename for filename in filenames if filename.endswith(suffix)]

def get_dataframes():
    
    #creates a dictionary that holds a dataframe of each csv
    filenames = ['BTN_Raise.csv', 'CO_Raise.csv', 'HJ_Raise.csv', 'SB_Raise.csv', 'SB_Limp.csv']
    
    df_dict = {}
    
    for file in filenames:
        df = pd.read_csv(file)
        keep_col = ['Combo', 'Weight']
        df = df[keep_col]
        df_dict[file] = df
    
    return df_dict

def match_dataframes(handlist, df_dict):
    #checks the hand list against each dataframe in the dictionary. returns a dictionary of action to take (via csv name) + percentage
    match_dict = {}
    
    for key in df_dict:
        df = df_dict[key]
        for hand in handlist:
            match_df = df[df['Combo'] == hand]
            #match_df = match_df.reset_index(drop=True)
            if not match_df.empty:
                #print key, type(key)        
                #print "{0:.0f}%".format(match_df.iloc[0,1]*100)#.to_string#(index=False, header=False)
                key = key.replace('100bb_',"").replace('.csv',"")
                match_dict[key] = match_df.iloc[0,1] # "{0:.0f}%".format(match_df.iloc[0,1]*100)
                break
            else:
                next
                 
    return match_dict        

def RNG():
   r = random.randint(1, 100)    
   r = float(r / 100)
  #  print 'r=' , r
   return r    


def HJ(handlist, df_dict):
    matches = match_dataframes(handlist, df_dict)
    HJ_Raise = round(matches.get('HJ_Raise', 0), 3)
    r = RNG()
    if r < HJ_Raise:
      print 'Open ', HJ_Raise, " Otherwise: Fold"
    else:
      print 'Fold', " Otherwise: Open", HJ_Raise

def CO(handlist, df_dict):
    matches = match_dataframes(handlist, df_dict)
    CO_Raise = round(matches.get('BTN_Raise', 0), 3)
    r = RNG()
    if r < CO_Raise:
      print 'Open ', CO_Raise, " Otherwise: Fold"
    else:
      print 'Fold', " Otherwise: Open", CO_Raise

def BTN(handlist, df_dict):
    matches = match_dataframes(handlist, df_dict)
    BTN_Raise = round(matches.get('BTN_Raise', 0), 3)
    r = RNG()
    if r < BTN_Raise:
      print 'Open ', BTN_Raise, " Otherwise: Fold"
    else:
      print 'Fold', " Otherwise: Open", BTN_Raise

def SB(handlist, df_dict):
    matches = match_dataframes(handlist, df_dict)
    SB_Raise = round(matches.get('SB_Raise', 0), 3)
    r = RNG()
    if r < SB_Raise:
      print 'Open ', SB_Raise, " Otherwise: Fold"
    else:
      print 'Fold', " Otherwise: Open", SB_Raise

def BB(handlist, df_dict):
    matches = match_dataframes(handlist, df_dict)
    BB_Raise = round(matches.get('BB_Raise', 0), 3)
    r = RNG()
    if r < BB_Raise:
      print 'Open ', BB_Raise, " Otherwise: Fold"
    else:
      print 'Fold', " Otherwise: Open", BB_Raise

positions_dispatcher = {
  'HJ': HJ,
  'CO': CO,
  'BTN': BTN,
  'SB': SB,
  'BB': BB
}

def convertinput(userinput):
    finalhand = "not recognized" 
    
    if (len(userinput) > 8 or len(userinput) < 4):
        finalhand = "not recognized" 
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
        finalhand = "%sd%ss%sh%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
    elif (len(userinput) == 5 or len(userinput) == 6):
    #for 5 or 6 character entries only
        if input0 == input1:  #check if first two characters are a pair and do the suiting this way
            if input4 == "s":
                finalhand = "%sc%sh%sh%sd" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == "d":
                finalhand = "%sh%ss%sh%ss" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == "r":
                finalhand = "%sd%ss%sh%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == "t":
                finalhand = "%sc%sd%sd%sd" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == "m":
                finalhand = "%sd%sh%sh%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
            elif input4 == "l":
                finalhand = "%ss%sc%sh%sh" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
        else: #else if the first two aren't a pair, then do the suiting as below
                if input4 == "s":
                    finalhand = "%sh%sh%sd%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == "d":
                    finalhand = "%sh%sh%ss%ss" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == "t":
                    finalhand = "%sd%sd%sd%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == "q":
                    finalhand = "%sh%sh%sh%sh" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == "r":
                    finalhand = "%sd%ss%sh%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == "m":
                    finalhand = "%sd%sh%sh%sc" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                elif input4 == "l":
                    finalhand = "%ss%sc%sh%sh" % (input0.upper(), input1.upper(), input2.upper(), input3.upper())
                else:
                    finalhand = "not recognized"
    #if its an 8 character input don't modify it other than the capitalization
    elif len(userinput) == 8:
            finalhand = "%s%s%s%s%s%s%s%s" % (input0.upper(), input1.lower(), input2.upper(), input3.lower(), input4.upper(), input5.lower(), input6.upper(), input7.lower())
    else:
            finalhand = "not recognized"

    return finalhand


def my_permutations2(myp):
    
    Card1 = myp[0:2]
    Card2 = myp[2:4]
    Card3 = myp[4:6]
    Card4 = myp[6:8]
    cardlist = (Card1, Card2, Card3, Card4)
    clength = len(cardlist)
    handlist = []
    
    handlist = [''.join(i) for i in permutations(cardlist, clength)]
    
    return handlist

def main():
    df_dict = get_dataframes()   
    print "blade runner p: gl"
    print "blade runner p: hf"
    print ""
    while True:
       rawinput = raw_input("Input PLO Hand: ").lower()
       if rawinput == "quit":
          print "blade runner p: gg"
          print "blade runner p: m8"
          return 

       posinput = raw_input("Position: ").upper()
       if posinput == "QUIT": return

       while posinput not in ['HJ', 'CO', 'BTN', 'SB', 'BB']:
          print 'Invalid Position'
          posinput = raw_input("Position: ").upper()
          if posinput == "QUIT": return

       else:
            convertedinput = convertinput(rawinput) #take raw input and convert it to a searchable plo hand
            
            if convertedinput == 'not recognized': #error catch
                print ""
                print "Oops, try again"
            else:
                handlist = my_permutations2(convertedinput)

                match_dict = match_dataframes(handlist,df_dict)
                print ""
                print "--------",convertedinput[0:2]+","+convertedinput[2:4]+","+convertedinput[4:6]+","+convertedinput[6:], "from", posinput, "--------" 
                print ""
                positions_dispatcher[posinput](handlist, df_dict)
                print ""

main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        