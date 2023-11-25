from pygame import mixer
from tkinter import *

root = Tk()
root.title("Music Player")
root.geometry("600x300")

mixer.init()
mixer.music.load("/Users/habeeb/Downloads/WhatsApp Audio 2023-04-01 at 17.55.18.mpeg")


def pause():
    mixer.music.pause()


def play():
    mixer.music.play()


def resume():
    mixer.music.unpause()


Label(root, text="Demo Music Player", font="lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=250, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Quit", command=quit).place(x=380, y=100)

root.mainloop()