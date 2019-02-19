import random

def RNG():
   r = random.randint(1,100)    
   #print 'r=' , r
   return r    
    

def main():
  while True:

    rawinput = raw_input('a/p/g/r: ').lower()

    if rawinput == 'quit':
      return
    elif rawinput[0:1] == 'r':
      r = RNG()
      print r
      print ''
    elif rawinput[0:1] == 'g':
      
    elif rawinput[0:1] == 'a':


    elif rawinput[0:1] == 'p':
      nums = rawinput.split(' ')
      bet = float(nums[1])
      pot = float(nums[2])
      pot_odds = float(bet / (bet + bet + pot))
      print 'PotOdds:', str(format(pot_odds*100, '.0f')) + '%'
      print ''

    else:
      print 'Oops, not a recognized option.'

main()