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
