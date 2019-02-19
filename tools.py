import random

def RNG():
   r = random.randint(1,100)    
   r = float(r / 100)
   #print 'r=' , r
   return r    
    

def main():
  while True:

    rawinput = raw_input('Select function: ').lower()

    if rawinput == 'quit':
      return
    elif rawinput == 'r':
      print RNG()
    elif rawinput == 'g':
      print 'run the geo function here'
    elif rawinput == 'a':
      print 'run the alpha function here'
    elif rawinput == 'p':
      print 'run the pot odds function here'
    else:
      print 'Oops, not a recognized option.'

main()