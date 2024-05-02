from classes.pole import pole
class pole_list():

    def __init__(self):
        self.head= None
        self.tail= None

    
    def add_to_head(self, node:pole):
        if (self.head == None):
            self.head= node
            self.tail= node
        else:
            node.front_pole = self.head
            self.head.behind_pole= node
            self.head= node