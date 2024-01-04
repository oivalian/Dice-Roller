import random as r
import tkinter as tk
import ttkbootstrap as ttk


def dice_roll():
    dice = ("⚀", "⚁", "⚂", "⚃", "⚄", "⚅")
    output_string.set(r.choice(dice))


# window / root
window = ttk.Window(themename='darkly')
window.iconbitmap('content/dice.ico')
window.title('Dice Roller')
window.geometry("350x400")
window.maxsize(350, 400)
window.minsize(350, 400)


# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font='Verdana 130', textvariable=output_string)
output_label.pack(pady=5)

# button
content_frame = ttk.Frame(master=window)
roll_button = ttk.Button(master=content_frame, text='Roll Die', width=30, command=dice_roll)
roll_button.pack(pady=5)
content_frame.pack()

# main
window.mainloop()
