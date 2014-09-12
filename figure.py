#using python2

from copy import deepcopy
from random import choice
import re

FIGURES= (\
'''
|.#.|.#.|...|.#.|
|###|.##|###|##.|
|...|.#.|.#.|.#.|
'''
, \
'''
|.##|...|.#.|#..|
|.#.|###|.#.|###|
|.#.|..#|##.|...|
'''
, \
'''
|##.|..#|.#.|...|
|.#.|###|.#.|###|
|.#.|...|.##|#..|
'''
, \
'''
|##|
|##|
'''
, \
'''
|##.|.#.|
|.##|##.|
|...|#..|
'''
, \
'''
|.##|#..|
|##.|##.|
|...|.#.|
'''
, \
'''
|....|.#..|
|####|.#..|
|....|.#..|
|....|.#..|
'''
)

class State:
	def __init__(self, point, variant):
		self.global_marker= list(point)
		self.variant= variant
		
class Figure:
	def __init__(self):
		self.figure_variants= []
		raw_fig= choice(FIGURES)
		#print raw_fig
		variants= zip(*[filter(None, row.split('|')) 
		for row in filter(None, raw_fig.split('\n'))])
		for variant in variants:
			figure_variant=[]
			for y in range(len(variant)):
				figure_variant.extend(
				[(f.start(), y) for f in re.finditer('#', variant[y])])
			self.figure_variants.append(tuple(figure_variant))
		self.figure_variants= tuple(self.figure_variants)
		self.variant_count= len(self.figure_variants)
		self.cur_state= State((3, 21), 0)
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
	
	def left_turn(self):
		self.prev_state= deepcopy(self.cur_state)
		idx= self.cur_state.variant - 1
		self.cur_state.variant= idx % self.variant_count	#that's cool
	
	def right_turn(self):
		self.prev_state= deepcopy(self.cur_state)
		idx= self.cur_state.variant + 1
		self.cur_state.variant= idx % self.variant_count
		
	def rollback(self):
		 self.cur_state= deepcopy(self.prev_state)
		 self.prev_state= None
		 
	def get_all(self):
		gx, gy= self.cur_state.global_marker
		return [(gx+x, gy-y) for x,y in self.figure_variants[self.cur_state.variant]]

Figure()