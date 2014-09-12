#using python2

import Tkinter
from visual import Visual
from relief import Relief
from figure import Figure
from random import randint

class Game:
	def __init__(self):
		self.root= Tkinter.Tk()
		self.vis= Visual(self.root)
		self.relief= Relief()
		self.figure= None
		self.stand_latter= False
		
		self.root.after_idle(self.tick)
		self.root.bind('<KeyPress>', self.press_key)
		self.root.mainloop()
		
	def tick(self):
		self.root.after(300, self.tick)
		if not self.figure:
			self.figure= Figure()
			if self.relief.have_collision(self.figure.get_all()):
				print 'generate collision with relief'
				self.root.quit()
		
		self.figure.down_move()
		if self.try_stand_figure():
			self.figure= None
			if self.relief.overload():
				print 'You Fail'
				self.root.quit()
		
		self.redraw()		
	
	def redraw(self):
		self.vis.reset()
		self.vis.draw(self.relief.get_all(), 'navajo white')
		if self.figure:
			self.vis.draw(self.figure.get_all(), 'alice blue')
		
	def move_figure(self, method):
		method()
		if self.relief.have_collision(self.figure.get_all()):
			self.figure.rollback()
		else:
			self.redraw()
			self.stand_latter= True
		
	def press_key(self, event):
		if not self.figure:
			return
			
		inp= event.char.upper()
		
		if inp == 'D':
			self.move_figure(self.figure.right_move)
		elif inp == 'A': 
			self.move_figure(self.figure.left_move)	
		elif inp == 'S': 
			self.move_figure(self.figure.down_move)
		elif inp == 'E' or inp == ' ':
			self.move_figure(self.figure.right_turn)
		elif inp == 'Q':
			self.move_figure(self.figure.left_turn)
		elif inp == 'W':		
			while not self.relief.have_collision(self.figure.get_all()):
				self.figure.down_move()
			self.figure.rollback()
			self.redraw()
	
	def try_stand_figure(self):
		result= False
		if self.relief.have_collision(self.figure.get_all()):
			self.figure.rollback()
			if self.stand_latter:
				pass
			else:
				self.relief.extend(self.figure.get_all())
				self.relief.remove_filled_lines()
				result= True
		self.stand_latter= False
		return result
		
Game()