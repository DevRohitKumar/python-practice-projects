"""
Author: Rohit Kumar

"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random, string

win = Tk()

dark_bg_color = "#1a1919"
normal_btn_bg = "#f76f25"
active_btn_bg = "#f58447"
win.title("Generate random password")
icon = ImageTk.PhotoImage(file = "lock.png")
win.iconphoto(False, icon)
win.geometry("500x200")
win.resizable(0, 0)
win.config(background=dark_bg_color)

# Label area to show password
txt_area = Label(win,
                text="Select length of your password",
                font= ("Noto Sans", 18, 'italic'),
                justify=CENTER,
                bg=dark_bg_color,
                fg="#e6f0ec",
                )
txt_area.pack()

# Radio buttons
pwd_len_list = [8, 16, 20, 24, 32]
rad_btn = IntVar()
for p in range(len(pwd_len_list)):
    digit_len = pwd_len_list[p]
    radiobtn = Radiobutton(win,
                            text= str(digit_len) + " digits",
                            variable=rad_btn,
                            value=digit_len,
                            font=("Noto Sans", 15, 'bold'),
                            bg=dark_bg_color,
                            fg="#e6f0ec",
                            # activebackground=normal_btn_bg,
                            # activeforeground=dark_bg_color,
                            indicatoron = 0,
                            padx=8
                            )
    radiobtn.pack(side=LEFT, anchor=E)

# Collect all the characters 
lc_chars = [*string.ascii_lowercase]
uc_chars = [*string.ascii_uppercase]
numbers = [*string.digits]
spsl_chars = [*string.punctuation]
spsl_chars.remove('\\')

def generate_password():
    # selecting at least one character of each type
    single_lc_char = random.choice(lc_chars)
    single_uc_char = random.choice(uc_chars)
    single_number = random.choice(numbers)
    single_spsl_char = random.choice(spsl_chars)
    
    all_chars = numbers + lc_chars + uc_chars + spsl_chars

    temp_pass_str = single_lc_char + single_number + single_uc_char + single_spsl_char
    
    selected_pwd_length = rad_btn.get()
    if selected_pwd_length > 0:
        for x in range(selected_pwd_length - 4):
            temp_pass_str += random.choice(all_chars)
            
        final_pwd = ''.join(random.sample(temp_pass_str,len(temp_pass_str)))
        txt_area.config(text=final_pwd) 
        copy_btn.config(state= NORMAL)
    else:
        messagebox.showwarning(
            title="Something is missing", 
            message="Please choose your desired password length"
            )

def copy_password():
    copied_pwd = txt_area['text']
    win.clipboard_clear()
    win.clipboard_append(copied_pwd)
   
# Button to copy password to clipboard
copy_btn = Button(win,
                  text= "Copy Password",
                  font= ("Noto Sans", 16),
                  bg= normal_btn_bg,
                  activebackground= active_btn_bg,
                  command=copy_password,
                  state= DISABLED
                  )
copy_btn.place(relx=.2, rely=.85, anchor="c")

# Button for password generate
pwd_btn = Button(win,
                 text="Generate password",
                 font= ("Noto Sans", 16),
                 bg= normal_btn_bg,
                 activebackground= active_btn_bg,
                 command=generate_password
                 )
pwd_btn.place(relx=.77, rely=.85, anchor="c")




win.mainloop()