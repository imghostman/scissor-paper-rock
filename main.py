from tkinter import *

import PIL.Image
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissor Paper")
root.config(background="#9b95b6")

# picture
# rock_img = ImageTk.PhotoImage(image=PIL.Image.fromarray("rock-user.png"))
# paper_img = ImageTk.PhotoImage(image=PIL.Image.fromarray("paper-user.png"))
# scissor_img = ImageTk.PhotoImage(image=PIL.Image.fromarray("scissors-user.png"))
# rock_img_comp = ImageTk.PhotoImage(image=PIL.Image.fromarray("rock.png"))
# paper_img_comp = ImageTk.PhotoImage(image=PIL.Image.fromarray("paper.png"))
# scissor_img_comp = ImageTk.PhotoImage(image=PIL.Image.fromarray("scissors.png"))
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# INDICATORS
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# Messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)


# Update Messages
def updateMessage(x):
    msg['text'] = x


# update User Score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


# update Computer score

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


# Check WInner
def checkWin(player, computer):
    if player == computer:
        updateMessage("TIE")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass


# update choice
choices = ["rock", "paper", "scissor"]


def updateChoice(x):
    # for computer
    comp_choice = choices[randint(0, 2)]  # generate random number between 0 and 2
    if comp_choice == "rock":
        comp_label.configure(image=rock_img)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissor_img)

    # for  user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, comp_choice)


# Buttons
rock = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D",
              fg="White", command=lambda: updateChoice("rock")).grid(row=2, column=1)
scissor = Button(root, width=20, height=2, text="Scissor", bg="#FAD02E",
                 fg="White", command=lambda: updateChoice("paper")).grid(row=2, column=2)
paper = Button(root, width=20, height=2, text="Paper", bg="#0ABDE3",
               fg="White", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
