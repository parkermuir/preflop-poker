def main():
  while True:
    rawinput = raw_input('Input PLO Hand: ').lower()

    if rawinput == 'quit':
      print 'blade runner p: gg'
      print 'blade runner p: m8'
      return
    elif rawinput[0:4] == 'info':
      infoRequest = True
      convertedinput = convertinput(rawinput[5:10])
    else:
      convertedinput = convertinput(rawinput) #take raw input and convert it to a searchable plo hand

    if convertedinput == 'not recognized': #error catch
      print ''
      print 'Oops, try again'
      continue

    
main()