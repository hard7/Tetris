#using python2

from copy import deepcopy

class State:
	def __init__(self, side):
		self.global_marker= [3, 21]
		self.side= side
		
		self.local_map= [[True] * self.side] * self.side

class Figure:
	def __init__(self):
		self.reset()
		
		
	def reset(self):
		self.side= 3
		self.cur_state= State(self.side)
		self.prev_state= None
	
	def down_move(self):
		self.prev_state= deepcopy(self.cur_state)
		self.cur_state.global_marker[1] -= 1
		
	
	def left_move(self):
		self.prev_state= deepcopy(self.cur_state)
		self.cur_state.global_marker[0] -= 1
	
	def right_move(self):
		self.prev_state= deepcopy(self.cur_state)
		self.cur_state.global_marker[0] += 1
		
	def rollback(self):
		 self.cur_state= deepcopy(self.prev_state)
		 self.prev_state= None
		 
	def get_all(self):
		res= []
		for y in range(self.side):
			for x in range(self.side):
				if self.cur_state.local_map[y][x]:
					gx, gy= self.cur_state.global_marker
					res.append((gx+x, gy-y))
		return res