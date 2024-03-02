class Block: 
    def __init__(self, course, done): 
        self.course = course
        self.done = done
        


    def verify(self):
        if self.done: 
            return True
    
class Partition: 
    def __init__(self, containers):
        self.containers = containers
        self.size = len(containers)
    
    def verify(self): 
        for container in self.containers: 
            if container.verify():
                return True
        return False
    

class Container: 
    def __init__(self, children):
        self.children = children
        self.size = 0        

    def verify(self): 
        for child in self.children: 
            if not child.verify(): 
                return False
        return True


stat = Block('STAT 1000', False)
cs = Block('CS 1503', True)
math280 = Block('MATH 0280', True)
math1180 = Block('MATH 1180', False)

math_req = Partition([Container([stat]), Container([cs, Partition([Container([math280]), Container([math1180])])])])


print(math_req.verify())

