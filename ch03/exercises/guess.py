import random

correct = random.randint(1, 10)

for i in range(3):
  question = int(input("What is your guess? "))
  if correct==question:
    print("Correct")
    break
  elif correct>question:
    print("Too Low")
  elif correct<question:
    print("Too High")









  
  

