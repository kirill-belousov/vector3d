class Vector:
	from math import sqrt
	x = double()
	y = double()
	z = double()
	
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z
	
	def __eq__(self, other):
		if self.x == other.x and self.y == other.y and self.z == other.z: return True
		else: return False
	
	def __len__(self):
		return self.length()
	
	
	def __add_(self, o):
		return Vector((self.x + o.x), (self.y + o.y), (self.z + o.z))
	
	def __sub__(self, o):
		return Vector((self.x - o.x), (self.y - o.y), (self.z - o.z))
	
	def __mul__(self, o):
		return Vector((self.x * o.x) + (self.y * o.y) + (self.z * o.z))
	
	def __iadd__(self, o):
		self.x += o.x
		self.y += o.y
		self.z += o.z
	
	def __isub__(self, o):
		self.x -= o.x
		self.y -= o.y
		self.z -= o.z
	
	def __neg__(self):
		return Vector(-self.x, -self.y, -self.z)
	
	def length(self):
		return sqrt(self.x^2 + self.y^2 + self.z^2)