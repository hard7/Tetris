#using python2

import Tkinter

class Visual:
	def __init__(self, root):
		self.w= 10
		self.h= 20
		self.cell_pixel= 20
		self.root= root
		arg= {}
		arg['width']= self.cell_pixel * self.w
		arg['height']= self.cell_pixel * self.h
		self.canvas= Tkinter.Canvas(root, **arg)
		self.reset()
		self.canvas.pack()
		
	def draw(self, paintedFields, color='yellow'):
		for paintedField in paintedFields:
			self.fill_cell(paintedField, color)
		
	def fill_cell(self, point, color):
		x,y = point
		l = self.cell_pixel
		loX, loY= x*l, (self.h-y-1)*l
		var= [loX, loY, loX+l, loY+l]
		idx= self.canvas.create_rectangle(*var, fill= color)

	def reset(self):
		l = self.cell_pixel
		self.canvas.delete("all")
		self.canvas.create_rectangle(1, 1, l*self.w, l*self.h)
		for i in range(self.w):
			self.canvas.create_line(l*i, 0, l*i, l*self.h)
			
		for j in range(self.h):
			self.canvas.create_line(0, l*j, l*self.w, l*j)