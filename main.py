#using python2

import Tkinter
from visual import Visual
from relief import Relief
from figure import Figure
from random import randint


def press_key(event):
	inp= event.char.upper()
	if inp == 'D': 
		pass
	if inp == 'A': 
		pass

def new_figure(relief):
	figure= Figure()
	fail= False
	if relief.have_collision(figure.get_all()):
		figure= None	
	return figure

def try_stand_figure(figure, relief):
	if relief.have_collision(figure.get_all()):
		figure.rollback()
		relief.extend(figure.get_all())
		relief.remove_filled_lines()
		figure= new_figure(relief)
		return True
	return False
			


def tick():
	root.after(500, tick)
	global figure
	if not figure:
		figure= Figure()
	figure.down_move()
	if try_stand_figure(figure, relief):
		figure= None
	
	vis.reset()
	vis.draw(relief.get_all(), 'powder blue')
	vis.draw(figure.get_all(), 'gray')
	
	

root= Tkinter.Tk()
vis= Visual(root)
relief= Relief()
figure= None

root.after_idle(tick)
root.bind('<KeyPress>', press_key)
root.mainloop()

