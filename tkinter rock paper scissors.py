#🪨📰✂️ with tkinter gui 
from tkinter import * 
from PIL import Image, ImageTk
import random

win = Tk()
win.title("Rock Paper Scissors")
icon = ImageTk.PhotoImage(file = "rps_img.jpg")
win.iconphoto(False, icon)
win.geometry("350x370")
win.minsize(350, 370)
win.maxsize(350, 370)
win.config(background="light grey")


rps_choices = ["rock", "paper", "scissors"]
user_score, com_score, tie_score = 0, 0, 0

msg = "💻: "+str(com_score)+"\t🤵: "+str(user_score)+"\t🏴: "+str(tie_score)
score_board = Label(win,
              text=msg,
              font= ("Noto Sans", 22, "bold"),
              background="#32a885",
              width=350,
              anchor=W,
              justify=CENTER
              )

score_board.pack()

def play_rps():
   user_choice = x.get()
   comp_choice = random.randint(0, 2)
      
   if user_choice == comp_choice:
      tie_game()
   elif((user_choice == 0 and comp_choice == 2) or
        (user_choice == 2 and comp_choice == 1) or
        (user_choice == 1 and comp_choice == 0)):
      user_win()
   else:
      com_win()
   

def user_win():
   global user_score, com_score, tie_score
   user_score += 1
   update_scoreboard(user_score, com_score, tie_score)
   print(" 🤺 wins! ")
   
def com_win():
   global com_score, user_score, tie_score
   com_score += 1
   update_scoreboard(user_score, com_score, tie_score)
   print(" 💻 wins! ")
  
def tie_game():
   global com_score, user_score, tie_score
   tie_score += 1
   update_scoreboard(user_score, com_score, tie_score)
   print(" 😛 ties! ")
   
def update_scoreboard(user_score, com_score, tie_score):
   msg = "💻: "+str(com_score)+"\t🤵: "+str(user_score)+"\t🏴: "+str(tie_score)
   score_board.config(text= msg)


# Create list of images. we cannot use PhotoImage directly inside
# radio button loop, for now at least.
rps_images = []
for choice in rps_choices:      
   image = Image.open(choice+'.png')
   resized_image = image.resize((100, 100))
   final_image = ImageTk.PhotoImage(resized_image)
   rps_images.append(final_image)

# generating radio buttons with respective images
x = IntVar()
for r in range(len(rps_choices)):
   radiobtn = Radiobutton(win,
                        text=rps_choices[r].capitalize(),
                        variable=x,
                        value=r,
                        font=("Noto Sans", 20),
                        image= rps_images[r],
                        width=350,
                        compound= 'right',
                        indicatoron = 0,
                        command=play_rps
                        )
   radiobtn.pack(anchor=NE)


win.mainloop()