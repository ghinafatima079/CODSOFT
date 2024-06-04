# Rock-Paper-Scissors Game
""" User Input: Prompt the user to choose rock, paper, or scissors.
Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
Game Logic: Determine the winner based on the user's choice and the computer's choice. Rock beats scissors, scissors beat paper, and paper beats rock.
Display Result: Show the user's choice and the computer's choice. Display the result, whether the user wins, loses, or it's a tie.
Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
Play Again: Ask the user if they want to play another round.
User Interface: Design a user-friendly interface with clear instructions and feedback."""

import random
from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title('Rock-Paper-Scissors Game')

options=['Rock', 'Paper', 'Scissors']

instructions=Label(root,text='Rock beats scissors, scissors beat paper, and paper beats rock.\nYou can choose from the following options- \n 1.Rock \n 2.Paper \n 3.Scissors \n',font=('comic sas',16))
instructions.grid(pady=5,padx=5,row=0,column=0,columnspan=3)

player_label=Label(root, text='Player-',font=(12))
player_label.grid(pady=5,padx=5,row=2,column=0)

player_choice_label=Label(root,text="",font=(12))
player_choice_label.grid(pady=5,padx=5,row=2,column=1)

computer_label=Label(root, text='Computer-',font=(12))
computer_label.grid(pady=5,padx=5,row=3,column=0)

computer_choice_label=Label(root,text="",font=(12))
computer_choice_label.grid(pady=5,padx=5,row=3,column=1)


result_label=Label(root,text="Result",font=(12))
result_label.grid(pady=5,padx=5,row=4,column=0)

result=Label(root,text="",font=(12))
result.grid(pady=5,padx=5,row=4,column=1)

score_label=Label(root,text="Score",font=(12))
score_label.grid(pady=5,padx=5,row=5,column=0)

player_score_label=Label(root,text="Player",font=(12))
player_score_label.grid(pady=5,padx=5,row=5,column=1)

player_score_display=Label(root,text="",font=(12))
player_score_display.grid(pady=5,padx=5,row=6,column=1)

computer_score_label=Label(root,text="Computer",font=(12))
computer_score_label.grid(pady=5,padx=5,row=5,column=2)

computer_score_display=Label(root,text="",font=(12))
computer_score_display.grid(pady=5,padx=5,row=6,column=2)


computer_score=0
player_score=0

def rock():
    
    global computer_score
    global player_score
    
    computer_choice=random.choice(options)
    computer_choice_label.config(text=computer_choice)
    player_choice_label.config(text="Rock")
    
    if computer_choice=='Rock':
        result.config(text="Tie",fg="orange")
        
    elif computer_choice=='Paper':
        result.config(text="You lose",fg="red")
        computer_score+=1
        computer_score_display.config(text=computer_score)
    else:
        result.config(text="You win",fg="green")
        player_score+=1
        player_score_display.config(text=player_score)
    
    
    
def paper():
    
    global computer_score
    global player_score
    
    computer_choice=random.choice(options)
    computer_choice_label.config(text=computer_choice)
    player_choice_label.config(text="Paper")

    if computer_choice=='Rock':
        result.config(text="You win",fg="green")
        player_score+=1
        player_score_display.config(text=player_score)
        
    elif computer_choice=='Paper':
        result.config(text="Tie",fg="orange")
        
    else:
        result.config(text="You lose",fg="red")
        computer_score+=1
        computer_score_display.config(text=computer_score)
    
    
def scissors():
    
    global computer_score
    global player_score
    
    computer_choice=random.choice(options)
    computer_choice_label.config(text=computer_choice)
    player_choice_label.config(text="Scissors")
    
    if computer_choice=='Rock':
        result.config(text="You lose",fg="red")
        computer_score+=1
        computer_score_display.config(text=computer_score)
        
    elif computer_choice=='Paper':
        result.config(text="You win",fg="green")
        player_score+=1
        player_score_display.config(text=player_score)
        
    else:
        result.config(text="Tie",fg="orange")
    


buttonframe=Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

rock_button=Button(buttonframe,text='Rock',font=('Comic Sans', 16),command=rock,bg='lightgreen')
rock_button.grid(pady=5,padx=5,row=0,column=0)


paper_button=Button(buttonframe,text='Paper',font=('Comic Sans', 16),command=paper,bg='lightblue')
paper_button.grid(pady=5,padx=5,row=0,column=1)


scissors_button=Button(buttonframe,text='Scissors',font=('Comic Sans', 16),command=scissors,bg='lightpink')
scissors_button.grid(pady=5,padx=5,row=0,column=2)

buttonframe.grid(pady=5,padx=5,row=1,column=0,columnspan=3)


root.mainloop()