class Block: 
    def __init__(self, course, done): 
        self.course = course
        self.done = done

    def __init__(self,course): 
        self.course = course
        self.done = False
        
    def finish(self):
        self.done = True
    
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
        for child in self.children: 
            if type(child) != "Block":
                print("The child is a block ")
            if type(child) != "Partition": 
                pass



partition1 = Partition([Container(Block('0280')), Container(Block('1180'))])






