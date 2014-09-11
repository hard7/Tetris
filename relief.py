#using python2

class Relief:
	def __init__(self):
		self.line_count= 20
		self.line_count_ext= self.line_count * 2
		self.line_capacity= 10
		self.lines= []
		self.fill_empty_lines()
	
	def append(self, point):
		if self.check_empty(point):
			x, y= point
			self.lines[y].add(x)
			
	def extend(self, point_array):
		for point in point_array:
			self.append(point)
	
	def check_empty(self, point):
		is_empty= True		
		x,y = point
		if x<0 or x>= self.line_capacity:
			return False
		if y<0:				#free up border
			return False
		
		if x in self.lines[y]:
			is_empty= False
		return is_empty
		
	def have_collision(self, point_array):
		for point in point_array:
			if not self.check_empty(point):
				return True
		return False
		
	def remove_filled_lines(self):
		for line in self.lines:
			if len(line) == self.line_capacity:
				self.lines.remove(line)
		self.fill_empty_lines()
	
	def get_all(self):
		res= []
		for y in range(self.line_count_ext):
			for x in self.lines[y]:
				res.append((x,y))
		return res
		
	def fill_empty_lines(self):
		while self.line_count_ext > len(self.lines):
			self.lines.append(set())
	
	def overload(self):
		for i in range(self.line_count, self.line_count_ext):
			if len(self.lines[i]):
				return True
		return False
		