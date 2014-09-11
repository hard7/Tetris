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

		self.root.after_idle(self.tick)
		self.root.bind('<KeyPress>', self.press_key)
		self.root.mainloop()
		
	def tick(self):
		self.root.after(200, self.tick)
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
			
			
		self.vis.reset()
		self.vis.draw(self.relief.get_all(), 'powder blue')
		if self.figure:
			self.vis.draw(self.figure.get_all(), 'gray')
		
		
	def press_key(self, event):
		print 'pressed key'
	
	
	
	def try_stand_figure(self):
		if self.relief.have_collision(self.figure.get_all()):
			self.figure.rollback()
			self.relief.extend(self.figure.get_all())
			self.relief.remove_filled_lines()
			return True
		return False
		
Game()