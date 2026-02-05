import random

rand_num = random.randint(1,100)

while True:
   try:
       num = int(input("guess a random number btw 1-100:"))
       if num < rand_num :
         print("too low")
       elif num > rand_num:
          print("too high")
       elif num==rand_num:
          print("perfect! you got it")
          break
   except ValueError:
      print("invalid input, please enter a number")

      
    