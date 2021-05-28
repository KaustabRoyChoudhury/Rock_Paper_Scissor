import random
gamelist=["Rock","Paper","Scissor"]
n=int(input("Enter the no of games you want to play \n"))
yourscore=0
csscore=0
for i in range(1,n+1):
  choose=int(input("Enter your choice: 1: Rock 2: Paper 3: Scissor"))
  rand=random.choice(gamelist)
  if(choose == 1 and rand == "Rock"):
    print("Oh..! That's a tie.")
    print("Your score =", yourscore)
    print("Computer's score =", csscore)
  elif(choose == 1 and rand == "Paper"):
    print("Computer Scored a point")
    print("Your score =", yourscore)
    csscore += 1
    print("Computer's score =", csscore)
  elif(choose == 1 and rand == "Scissor"):
    print("You scored a point")
    yourscore += 1
    print("Your score =", yourscore)
    print("Computer's score =", csscore)
  elif(choose == 2 and rand == "Rock"):
    print(" You scored a point")
    yourscore += 1
    print("Your score =", yourscore)
    print("Computer's score =", csscore)
  elif(choose == 2 and rand =="Paper"):
    print("Oh..! That's a tie.")
    print("Your score =", yourscore) 
    print("Computer's score =", csscore)
  elif(choose == 2 and rand == "Scissor"):
    print("Computer Scored a point")
    print("Your score =", yourscore) 
    csscore += 1
    print("Computer's score =", csscore)
  elif(choose == 3 and rand == "Rock" ):
    print("Computer Scored a point")
    print("Your score =", yourscore) 
    csscore += 1
    print("Computer's score =", csscore)
  elif(choose == 3 and rand == "Paper"):
    print("You scored a point")
    yourscore += 1
    print("Your score =", yourscore)
    print("Computer's score =", csscore)
  elif(choose == 3 and rand == "Scissor"):
    print("Oh..! That's a tie.")
    print("Your score =", yourscore) 
    print("Computer's score =", csscore)
if(yourscore > csscore):
  print("Congratulations..! You won the Game..")
elif(yourscore == csscore):
    print("Oh..! That's a tie.")
else:
  print("Better luck next time")