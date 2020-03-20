from tkinter import *
import sys, os
from pygame import mixer

def play():
	fname = entry.get()
	mixer.init()

	mixer.music.load(fname)
	mixer.music.set_volume(0.5)
	mixer.music.play()

def pause():
	mixer.music.pause()

def resume():
	mixer.music.unpause()

def exit():
	if mixer.get_init():
		mixer.music.stop()
	sys.exit()

def addVol():
	vol = mixer.music.get_volume()
	if (vol < 0.95):
		mixer.music.set_volume(vol+0.05)
	else:
		mixer.music.set_volume(1.0)

def subVol():
	vol = mixer.music.get_volume()
	if (vol > 0.05):
		mixer.music.set_volume(vol-0.05)
	else:
		mixer.music.set_volume(0.0)

def mute():
	mixer.music.set_volume(0.0)

def gd():
	label1 = Label(win,text="Enter File Name: ",font=("arial",10,"bold"))
	label1.grid(row=0,column=1,columnspan=2)

	global entry
	entry = Entry(win,width=40)
	entry.grid(row=0,column=3,columnspan=3)

	button = Button(win,text="Play",command=play)
	button.grid(row=1,column=0,sticky=E)

	button = Button(win,text="Pause",command=pause)
	button.grid(row=1,column=1,sticky=E)

	button = Button(win,text="Resume",command=resume)
	button.grid(row=1,column=2,sticky=E)

	button = Button(win,text="+ Vol",command=addVol)
	button.grid(row=1,column=3,sticky=E)

	button = Button(win,text="- Vol",command=subVol)
	button.grid(row=1,column=4,sticky=W)

	button = Button(win,text="Mute",command=mute)
	button.grid(row=1,column=4,sticky=E)

	button = Button(win,text="Exit",command=exit)
	button.grid(row=1,column=5,sticky=E)

if __name__ == '__main__':
	win = Tk()
	#win.geometry("400x100")
	win.title("Music Player")
	gd()

	win.mainloop()