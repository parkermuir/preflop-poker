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



def get_filenames(path, suffix=".csv"):
    filenames = listdir(path)
    return [filename for filename in filenames if filename.endswith(suffix)]

def get_dataframes():
    
    #creates a dictionary that holds a dataframe of each csv
    filenames = ['100bb_BBCheckvsLimp.csv', '100bb_BB_3bvs3x.csv', '100bb_BB_5bet.csv', '100bb_BB_Callv3x.csv', '100bb_BB_Callvs4bet.csv', '100bb_BB_Foldv3x.csv', '100bb_BB_Foldvs4bet.csv', '100bb_BB_RaiseLimp.csv', '100bb_BTN_4bet.csv', '100bb_BTN_Allin.csv', '100bb_BTN_Callvs3b.csv', '100bb_BTN_Fold.csv', '100bb_BTN_Foldvs3b.csv', '100bb_BTN_Foldvs5bet.csv', '100bb_BTN_Limp.csv', '100bb_BTN_Pot.csv']
    
    df_dict = {}
    
    for file in filenames:
        df = pd.read_csv(file)
        keep_col = ['Combo', 'Weight']
        df = df[keep_col]
        df_dict[file] = df
    
    return df_dict

def match_dataframes(handlist,df_dict):
    #checks the hand list against each dataframe in the dictionary. returns a dictionary of action to take (via csv name) + percentage
    match_dict = {}
    
    for key in df_dict:
        df = df_dict[key]
        for h in handlist:
            match_df = df[df['Combo']== h]
            #match_df = match_df.reset_index(drop=True)
            if not match_df.empty:
                #print key, type(key)        
                #print "{0:.0f}%".format(match_df.iloc[0,1]*100)#.to_string#(index=False, header=False)
                key = key.replace('100bb_',"").replace('.csv',"")
                match_dict[key] =match_df.iloc[0,1] # "{0:.0f}%".format(match_df.iloc[0,1]*100)
                break
            else:
                next
                 
    return match_dict        

def small_blind_new(match_dict):
    
    BTN_Allin = round(match_dict.get('BTN_Allin',0),3)
    BTN_Pot = round(match_dict.get('BTN_Pot',0),3)
    BTN_Fold = round(match_dict.get('BTN_Fold',0),3)
    BTN_Limp = round(match_dict.get('BTN_Limp',0),3)
    BTN_4bet = round(match_dict.get('BTN_4bet',0),3)
    BTN_Foldvs3b = round(match_dict.get('BTN_Foldvs3b',0),3)
    BTN_Callvs3b = round(match_dict.get('BTN_Callvs3b',0),3)
    
    
    #create dictionary of possible action 1s and get an r
    SB_action1 = OrderedDict([("Open",BTN_Pot), ("Limp", BTN_Limp),("Fold",BTN_Fold)]) 
    r = RNG()
    
    for key in SB_action1:
        #check each action1 to see if its 100, if so, print it
        if SB_action1[key] > .99:
            action = key
            print action
            break
        else:
            #if none are 100, we have a mix strategy and proceed with that
            action = 'Mix'
     
    if action == 'Mix':
        #for a mixed strategy, check if any of the actions are 0 and remove them from the dictionary. at least one should be zero
        for key in SB_action1:
            if SB_action1[key] < .01:
                #print 'debug', SB_action1[key]
                del SB_action1[key]
            else:
                pass
        #print SB_action1
        
        if SB_action1.values()[0] >= r:
           print SB_action1.keys()[0],SB_action1.values()[0], " Otherwise:",  SB_action1.keys()[1]
           action = SB_action1.keys()[0]
        elif SB_action1.values()[0] < r:
           print SB_action1.keys()[1],SB_action1.values()[1], " Otherwise:",  SB_action1.keys()[0]
           action = SB_action1.keys()[1]
        else:
           print 'Fin - this is prob a crack in SB action #1'
    else:
        pass

    #print 'Debug: Action 1:', action
    
    
    
    #Action 2 section
    if action == 'Open':   
        #Action2 only happens if action1 was an Open, if so make our dictionary of possible second actions and get a new r
        SB_action2 = OrderedDict([('Call 3bet',BTN_Callvs3b),('Fold to 3bet',BTN_Foldvs3b), ('4bet',BTN_4bet)])
        r=RNG()
        
        for key in SB_action2:
            #check each action1 to see if any are 100, if so, print it and move on
            if SB_action2[key] > .99:
                action2 = key
                print action2
                break
            else:
                action2 = 'Mix'

        #print 'Debug - Action =', action2
        
        if action2 == 'Mix':
            #remove actions with that happen 0
            for key in SB_action2:
                if SB_action2[key] < .01:
                    del SB_action2[key]
                else:
                    pass
                
            #print 'Debug - Action2:', action2, 'Dict action2:', SB_action2,'Len:', len(SB_action2)
                
            if len(SB_action2) == 1:
                #if there is only one action in the mix strat, show it, because we always do that at this point int he tree
                print SB_action2.keys()[0]
            elif SB_action2.values()[0] >= r:
                #may need to add multiplication here so that these represent the right thing in mixed strategies
               print SB_action2.keys()[0],SB_action2.values()[0], " Otherwise:",  SB_action2.keys()[1]
            elif SB_action2.values()[0] < r:
               print SB_action2.keys()[1],SB_action2.values()[1], " Otherwise:",  SB_action2.keys()[0]
            else:
               print 'Fin - this is prob a crack in SB action #2'
        else:
            pass
    else:
        pass         
    
def big_blind_new(match_dict):
    BB_Callv3x = round(match_dict.get('BB_Callv3x',0),3)
    BB_Foldv3x = round(match_dict.get('BB_Foldv3x',0),3)
    BB_3bvs3x = round(match_dict.get('BB_3bvs3x',0),3)
    BBCheckvsLimp = round(match_dict.get('BBCheckvsLimp',0),3)
    BB_Callvs4bet= round(match_dict.get('BB_Callvs4bet',0),3)
    BB_RaiseLimp = round(match_dict.get('BB_RaiseLimp',0),3)
    BB_5bet = round(match_dict.get('BB_5bet',0),3)
    BB_Foldvs4bet = round(match_dict.get('BB_Foldvs4bet',0),3)

    #action0 logic - vs a Limp
    #create dictionary of possible action 0s facing a limp
    BB_action0 = OrderedDict([("Raise Limp", BB_RaiseLimp), ("Check", BBCheckvsLimp)]) 
    r = RNG()
    
    for key in BB_action0:
        #check each action0 to see if its 100, if so, print it
        if BB_action0[key] > .99:
            action0 = key
            print action0
            break
        else:
            #if none are 100, we have a mix strategy and proceed with that
            action0 = 'Mix'
            
    if action0 == 'Mix':
        #for a mixed strategy, check if any of the actions are 0 and remove them from the dictionary. at least one should be zero
        for key in BB_action0:
            if BB_action0[key] < .01:
                #print 'debug', BB_action0[key]
                del BB_action0[key]
            else:
                pass
            
        if BB_action0.values()[0] >= r:
           print BB_action0.keys()[0],BB_action0.values()[0], " Otherwise:",  BB_action0.keys()[1]
           action = BB_action0.keys()[0]
        elif BB_action0.values()[0] < r:
           print BB_action0.keys()[1],BB_action0.values()[1], " Otherwise:",  BB_action0.keys()[0]
           action = BB_action0.keys()[1]
        else:
           print 'Fin - this is prob a crack in BB action #1'          
            
  
    
    #action1 logic facing a 3x
    #create dictionary of possible action 1s facing a raise and get an r
    BB_action1 = OrderedDict([("Flat",BB_Callv3x), ("Fold", BB_Foldv3x),("3bet",BB_3bvs3x)]) 
    r = RNG()
    
    for key in BB_action1:
        #check each action1 to see if its 100, if so, print it
        if BB_action1[key] > .99:
            action = key
            print action
            break
        else:
            #if none are 100, we have a mix strategy and proceed with that
            action = 'Mix'
            
    if action == 'Mix':
        #for a mixed strategy, check if any of the next actions are 0 and remove them from the dictionary. at least one should be zero
        for key in BB_action1:
            if BB_action1[key] < .01:
                #print 'debug', BB_action1[key]
                del BB_action1[key]
            else:
                pass
        #print BB_action1
        
        if BB_action1.values()[0] >= r:
           print BB_action1.keys()[0],BB_action1.values()[0], " Otherwise:",  BB_action1.keys()[1]
           action = BB_action1.keys()[0]
        elif BB_action1.values()[0] < r:
           print BB_action1.keys()[1],BB_action1.values()[1], " Otherwise:",  BB_action1.keys()[0]
           action = BB_action1.keys()[1]
        else:
           print 'Fin - this is prob a crack in BB action #1'
    else:
        pass       
    
    #BB Action 2 section, once we have already 3bet
    if action == '3bet':   
        #Action2 only happens if action1 was an Open, if so make our dictionary of possible second actions and get a new r
        BB_action2 = OrderedDict([('Call 4bet',BB_Callvs4bet),('Fold to 4bet',BB_Foldvs4bet), ('5bet',BB_5bet)])
        r=RNG()
        
        for key in BB_action2:
            #check each action1 to see if any are 100, if so, print it and move on
            if BB_action2[key] > .99:
                action2 = key
                print action2
                break
            else:
                action2 = 'Mix'

        #print 'Debug - Action =', action2
        
        if action2 == 'Mix':
            #remove actions with that happen 0
            for key in BB_action2:
                if BB_action2[key] < .01:
                    del BB_action2[key]
                else:
                    pass
                
            #print 'Debug - Action2:', action2, 'Dict action2:', BB_action2,'Len:', len(BB_action2)
                
            if len(BB_action2) == 1:
                #if there is only one action in the mix strat, show it, because we always do that at this point int he tree
                print BB_action2.keys()[0]
            elif BB_action2.values()[0] >= r:
                #may need to add multiplication here so that these represent the right thing in mixed strategies
               print BB_action2.keys()[0],BB_action2.values()[0], " Otherwise:",  BB_action2.keys()[1]
            elif BB_action2.values()[0] < r:
               print BB_action2.keys()[1],BB_action2.values()[1], " Otherwise:",  BB_action2.keys()[0]
            else:
               print 'Fin - this is prob a crack in SB action #2'
        else:
            pass
    else:    
        pass

def RNG():
   r = random.randint(1,100)    
   r = float(r / 100)
   #print 'r=' , r
   return r    
    
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
       else:
            convertedinput = convertinput(rawinput) #take raw input and convert it to a searchable plo hand
            
            if convertedinput == 'not recognized': #error catch
                print ""
                print "Oops, try again"
            else:
                handlist = my_permutations2(convertedinput)
                match_dict = match_dataframes(handlist,df_dict)
                print ""
                print "--------", '[' + convertedinput[0:2] + ' ' + convertedinput[2:4] + ' ' + convertedinput[4:6] + ' ' + convertedinput[6:] + ']', "--------" 
                print ""
                print"SB:"
                small_blind_new(match_dict)
                print ""
                print "BB:"
                big_blind_new(match_dict)
                print ""


main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        