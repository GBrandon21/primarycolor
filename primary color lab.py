
red = 'red'
blue = 'blue'
yellow = 'yellow'

print ('Enter Two Primary Colors Below to Determine Secondary Color')

a1 = (input('Enter a Primary Color: '))
a2 = (input('Enter a Primary Color: '))

while True:
  if a1 == red and a2 == blue:
    print('You Mixed: Purple')
    break
         
  elif a1 == red and a2 == yellow:
    print ('You Mixed Orange')
    break
    
  elif a1 == blue and a2 == yellow:
    print ('You Mixed: Green')
    break

  elif a1 == blue and a2 ==red:
    print (' You Mixed Purple')
    break
     	
  elif a1 == yellow and a2 == red:
    print ('You Mixed Orange')
    break
          	
  elif a1 == yellow and a2 == blue:
    print ('You Mixed: Green')
    break

  else:  
    print('Please Only Input Primary Colors')
    a3 = (input('Try Again: Y or N: '))
   
    if a3== "N":
      break
    else:
      a1 = (input('Enter a Primary Color: '))
      a2 = (input('Enter a Primary Color: '))   	
