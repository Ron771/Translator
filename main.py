# TO TRANSLATE LANGUAGES USING Google Translate API
from googletrans import Translator
from tkinter import *
from tkinter import messagebox

# Display translated text on a prompt
# messagebox.showinfo(message="TRANSLATED TEXT: " + translated_text.text)


# Function to clear the text boxes
def clear():

	text_entry1.delete("1.0", END)
	text_entry2.delete("1.0", END)


def translate():
	translator = Translator()
	txt = text_entry1.get('1.0', END)

	dest_v = change_dropdown()
	src_v = change_srcdropdown()
	try:

		result = translator.translate(txt, src=src_v, dest=dest_v)
		print(result.text)
		text_entry2.insert('end', result.text)
	except:
		messagebox.showinfo(message="Text Field Blank ")
		print("An exception occurred")


# Invoke call to class to view a window
window = Tk()
# Set dimensions of window and title
window.geometry("550x350")
window.title("Ronald's-Language Translator")

# Import the Translator class which will read the input and translate
# Default translation is done by detection of input and to english
translator_object = Translator()
# Title of the app
title_label = Label(window, text="Ronald's Language Translator Using Python", font=("Times New Roman", 12)).pack()
# Other desired font:Gayathri
# Read inputs
# Text input
text_label = Label(window, text="Text to translate:").place(x=10, y=20)
text_entry1 = Text(window, width=40, height=5, font=("Ubuntu Mono", 12))
text_entry1.place(x=130, y=20)
# Source language input
psrc_label = Label(window, text="Source language (empty: auto-detect):").place(x=10, y=120)
# src_entry = Text(window, width=20, height=1, font=("Ubuntu Mono", 12))
# src_entry.place(x=275, y=120)
# Destination input

clickedsrc = StringVar(window)
optionssrc = {"en", "de", "fr", "ga"}
dropsrc = OptionMenu(window, clickedsrc, *optionssrc) .place(x=300, y=120)

dest_label = Label(window, text="Target language (empty: english-default):").place(x=10, y=150)
# dest_entry = Text(window, width=20, height=1, font=("Ubuntu Mono", 12))
# dest_entry.place(x=300, y=150)

clicked = StringVar(window)
options = {"en", "de", "fr", "ga"}
drop = OptionMenu(window, clicked, *options) .place(x=300, y=150)
# drop.pack()




# initial menu text
clickedsrc.set("en")
clicked.set("en")
print ( clickedsrc.get)

# Translate function and clear function activated through buttons
# button1 = Button(window, text='Translate', bg='Turquoise', command=translate_function).place(x=160, y=190)
button1 = Button(window, text='Translate', bg='Turquoise', command=translate).place(x=160, y=190)
button2 = Button(window, text='Clear', bg='Turquoise', command=clear).place(x=270, y=190)
# close the app
text_label2 = Label(window, text="Translated Text:").place(x=10, y=230)
text_entry2 = Text(window, width=40, height=5, font=("Ubuntu Mono", 12))
text_entry2.place(x=130, y=230)



def change_dropdown(*args):
    print(clicked.get() )
    # text_entry1.delete("1.0", END)
    # text_entry2.delete("1.0", END)
    return clicked.get()

# link function to change dropdown
clicked.trace('w', change_dropdown)

def change_srcdropdown(*args):
    print(clickedsrc.get() )
    # text_entry1.delete("1.0", END)
    # text_entry2.delete("1.0", END)
    return clickedsrc.get()

window.mainloop()

'''
import googletrans
from googletrans import Translator
print(googletrans.LANGUAGES)
'''

