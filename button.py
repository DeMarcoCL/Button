import tkinter as tk
from random import randint

def change_color():
    # generate a random RGB color
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'

    # change the button's background color
    button.config(bg=color)

# create the window and the button
root = tk.Tk()
button = tk.Button(root, text='Click me', command=change_color, bg='white', fg='black')
button.pack()

# start the main loop
root.mainloop()
