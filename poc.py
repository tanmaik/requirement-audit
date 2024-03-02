class Block: 
    def __init__(self, course): 
        self.course = course

class Partition: 
    def __init__(self, containers):
        if type(containers) != 'list':
            raise TypeError('Containers must be a list')
        self.containers = containers
        self.size = len(containers)
         

            

class Container: 

    def __init__(self, children):
        self.children = children
        self.size = 0        
    
    def verify(self): 
        if self.children:
            return True




partition1 = Partition([Container(Block('0280')), Container(Block('1180'))])






