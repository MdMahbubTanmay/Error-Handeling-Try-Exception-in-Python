a = "Hello"


try:
  print(a.index("x")) # as x not in the string so it will  through an error 
except:
  print("Cant do this") 


# If we want to print the roor I mean what the error is for debugging :
try:
  print(a.index("x")) # as x not in the string so it will  through an error 
except Exception as e:
  print(e) #substring not found





# Finally: It will run no matter error occurd or not
try:
  print(a.index("x")) # as x not in the string so it will  through an error 
except:
  print("Cant do this") 

finally:
  print("কখগঘঙ") 




  #Making My own error

  k = int(input("Enter Values less Than 5:"))

  if k>=5:
    raise ValueError("Hey! Do What I Asked for") #It will throw an Error.This is how we can make error by ourselves to stop program
