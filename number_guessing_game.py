import random
numbers=[]
for i in range(1,101):
 numbers.append(i)
logo='''
   \ |  |  |  \  |  _ )  __|  _ \     __|  |  | __|   __|   __| _ _|   \ |   __|     __|    \     \  |  __| 
  .  |  |  | |\/ |  _ \  _|     /    (_ |  |  | _|  \__ \ \__ \   |   .  |  (_ |    (_ |   _ \   |\/ |  _|  
 _|\_| \__/ _|  _| ___/ ___| _|_\   \___| \__/ ___| ____/ ____/ ___| _|\_| \___|   \___| _/  _\ _|  _| ___| 

'''

while 5<8:
 print(logo)
 random_num=random.choice(numbers)
 print("\nWelcome to the number guessing GAME !!")
 while 5<8:
  ask2=input("\nPlease choose the difficulty 'H' for HARD and 'E' for EASY :  ").lower()
  if ask2=="h":
   lives=5
   break
  elif ask2=="e":
   lives=10
   break
  else:  
   ask2  
 while 5<8:
  ask=int(input("\nGuess a number : "))
  if ask<101 and ask>0:
     if ask==random_num:
       print("\nYOU WON")
       break
     elif lives==1:
        print("\nGAME OVER")
        break
     elif ask<random_num:
         print("\nTOO LOW")
         lives-=1
         print(f"\nYOU STILL HAVE {lives} chance")
     elif ask>random_num:
         print("\nTOO HIGH")
         lives-=1
         print(f"\nYOU STILL HAVE {lives} chance")
     else:
         print("\nYOU WON")  
         break    
  else:
   ask  

