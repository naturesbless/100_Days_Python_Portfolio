import pandas as pd
from tkinter import *

# ---------------------------- Constants and Word List ------------------------------- # 

word_list = pd.read_csv('./data/french_words.csv')

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

CARD_FRONT = './images/card_front.png'
CARD_BACK = './images/card_back.png'
RIGHT = './images/right.png'
WRONG = './images/wrong.png'

timer = None

# ---------------------------- Word Generation Mechanism ------------------------------- # 
french_word = ""
english_word = ""

def random_words():
    global words
    words = word_list.sample()
    canvas.itemconfig(card_image, image=card_front_image)
    french_word = words.iloc[0]['French']
    canvas.itemconfig(language_text, text="French", fill = 'black')
    canvas.itemconfig(word_text, text=french_word, fill = 'black')
    start_timer()
    return french_word

# ---------------------------- Flash Card Flipping Mech ------------------------------- # 
def start_timer():
    global timer
    timer = window.after(3000, card_flip)

def card_flip():
    canvas.itemconfig(card_image, image=card_back_image)
    english_word = words.iloc[0]['English']
    canvas.itemconfig(language_text, text="English", fill = 'white')
    canvas.itemconfig(word_text, text=english_word, fill = 'white')

    
# --------------------------------- Flash Card UI ------------------------------------- # 
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file=CARD_FRONT)
card_back_image = PhotoImage(file=CARD_BACK)
card_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Press to Begin", font=(FONT_NAME, 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


right_image = PhotoImage(file=RIGHT)
right_button = Button(image=right_image, highlightthickness=0, command=random_words)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_words)
wrong_button.grid(row=1,column=0)

window.mainloop()