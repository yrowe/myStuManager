class Students(object):
	#相当于C里的结构体，好传数据
    def __init__(self, id='', name='', gender='', grade='', major='', score=''):
    	self.id = id
    	self.name = name
    	self.gender = gender
    	self.grade = grade
    	self.major = major
    	self.score = score
