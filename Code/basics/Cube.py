class Cube:
    def __init__(self, x, y, z, size):
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        '''
        (x, y+size) .___________. (x+size, y+size) 
                    |           |
                    |   p       |
                    |           |
                    |           |
              (x,y) O___________. (x+size, y) 
           
        '''
    def contains(self, point):
        if (self.x < point[0] and point[0] < (self.x+self.size)) and (self.y < point[1] and point[1] < (self.y+self.size)) and (self.z < point[2] and point[2] < (self.z+self.size)): return True

    def intersect(self, range):
        return not(self.x>range.x+range.size or range.x>self.x+self.size or self.y>range.y+range.size or range.y>self.y+self.size or self.z>range.z+range.size or range.z>self.z+self.size)
