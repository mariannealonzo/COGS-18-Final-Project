'''
This class represents a Grid which will be used
in the Game class.
'''
class Grid:

    '''
    This method initializes a grid object.
    '''
    def __init__(self):
        self.rows = 5
        self.cols = 5
        self.display = []

    '''
    This method generates the grid
    which will be shown to the player.
    '''
    def make_grid(self):
        for num in range(5):
            self.display.append(["-", "-", "-", "-", "-"])

    
