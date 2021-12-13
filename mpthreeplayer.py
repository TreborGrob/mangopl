import tkinter as tk
import fnmatch
import os
import pygame.mixer
from pygame import mixer
from tkinter import filedialog
from tkinter import *

from snd.sound import Sound

# import vlc


canvas = tk.Tk()
canvas.title("Mango Player")
canvas.geometry("600x800")
canvas.config(bg='black')
pattern = "*.mp3"
folder_path = StringVar()

mixer.init()

prev_img = tk.PhotoImage(file="img/prev_img.png")
stop_img = tk.PhotoImage(file="img/stop_img.png")
play_img = tk.PhotoImage(file="img/play_img.png")
pause_img = tk.PhotoImage(file="img/pause_img.png")
next_img = tk.PhotoImage(file="img/next_img.png")
dir_img = tk.PhotoImage(file="img/dir_img.png")


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    dir_select = filedialog.askdirectory()
    folder_path.set(dir_select)
    return dir_select


path = browse_button()


def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(path + "\\" + listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(path + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(path + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


listBox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('ds-digital', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('ds-digital', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text='Prev', image=prev_img, bg='black', borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text='Stop', image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text='Play', image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text='Pause', image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text='Next', image=next_img, bg='black', borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

dirButton = tk.Button(canvas, text='Directory', image=dir_img, bg='black', borderwidth=0, command=browse_button)
dirButton.pack(pady=15, in_=top, side='left')


def show_value(i):
    i = vol.get()
    pygame.mixer.music.set_volume(i)
    Sound.volume_set(i)


vol = Scale(canvas, from_=0, to=100, orient=VERTICAL, resolution=1, command=show_value)
vol.place(x=25, y=310)
vol.set(100)
vol.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(path):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
