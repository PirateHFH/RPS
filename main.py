import random 
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os


# tkinter setup
root = Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(background="#bca0dc")
root.minsize(600, 500)  # width, height
root.geometry("300x300+50+50")  # width x height + x + y

#Computer Choice
choice = ["Rock", "Paper", "Scissors"]
choiceType = random.choice(choice)

#Variables
global greetSprite
global gameStart
gameStart = False
restart = False


# sprites
rockImage = tk.PhotoImage(file="rock.png")
paperImage = tk.PhotoImage(file="paper.png")
scissorsImage = tk.PhotoImage(file="scissors.png")
winImage = tk.PhotoImage(file="win.png")
loseImage = tk.PhotoImage(file="lose.png")
tieImage = tk.PhotoImage(file="tie.png")
mainImage = tk.PhotoImage(file="main.png")
  
#Win Image 
def Win():
  label = ttk.Label(image=winImage)
  label.pack()
  label.place(x=100, y=85)

#Lose Image
def Lose():
  label = ttk.Label(image=loseImage)
  label.pack()
  label.place(x=100, y=85)

#Tie Image
def Tie():
  label = ttk.Label(image=tieImage)
  label.pack()
  label.place(x=100, y=85)

# Choice defs
def PaperChoice():
    label = ttk.Label(image=paperImage)
    label.pack()
    label.place(x=200, y=200)
  
def RockChoice():
    label = ttk.Label(image=rockImage)
    label.pack()
    label.place(x=200, y=200)
  
def ScissorsChoice():
    label = ttk.Label(image=scissorsImage)
    label.pack()
    label.place(x=200, y=200)

#Enter Game / player choice
def Rock():
  global gameActive
  print("game active")
  gameActive = True
  global playerChoice
  playerChoice = "rock"
  check_game_state() 
def Paper():
  global gameActive
  print("game active")
  gameActive = True
  global playerChoice
  playerChoice = "paper"
  check_game_state() 
def Scissors():
  global gameActive
  print("game active")
  gameActive = True
  global playerChoice
  playerChoice = "scissors"
  check_game_state() 
def destroyButtons(): 
  A.after(0, A.destroy)
  B.after(0, B.destroy)
  C.after(0, C.destroy)
  D.after(0, D.destroy)

#Restart Button
def Restart(): 
  os.system('python main.py')

#Game Verdicts
def paperVerdict():
  if playerChoice == "paper": 
    print("Tie")
    Tie()
  elif playerChoice == "scissors":
    print("You Win")
    Win()
  elif playerChoice == "rock":
    print("You Lose")
    Lose()
    
def rockVerdict():
  if playerChoice == "rock": 
    print("Tie")
    Tie()
  elif playerChoice == "paper":
    print("You Win")
    Win()
  elif playerChoice == "scissors":
    print("You Lose")
    Lose()
    
def scissorsVerdict():
  if playerChoice == "scissors": 
    print("Tie")
    Tie()
  elif playerChoice == "rock":
    print("You Win")
    Win()
  elif playerChoice == "paper":
    print("You Lose")
    Lose()

  
# Check game state periodically
def check_game_state():
    if gameActive and choiceType == "Paper":
      PaperChoice()
      destroyButtons()
      paperVerdict()
      print(playerChoice)
    if gameActive and choiceType == "Rock":
      RockChoice()
      destroyButtons()
      rockVerdict()
      print(playerChoice)
    if gameActive and choiceType == "Scissors":
      ScissorsChoice()
      destroyButtons()
      scissorsVerdict()
      print(playerChoice)

    else:
        root.after(100, check_game_state)  # Check again after 100 ms


# Initial button to enter the game
A = Button(root, text="Rock", command=Rock)
A.place(x=100, y=400)
B = Button(root, text="Paper", command=Paper)
B.place(x=200, y=400)
C = Button(root, text="Scissors", command=Scissors)
C.place(x=300, y=400)
D = ttk.Label(image=mainImage)
D.pack()
D.place(x=100, y=85)
E =  Button(root, text="Restart", command=Restart)
E.place(x=0, y=85)


root.mainloop()