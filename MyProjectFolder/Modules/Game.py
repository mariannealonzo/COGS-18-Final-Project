import random
import Grid

'''
This class represents our game and keeps track
of the game state.
'''
class Game:

    '''
    This method initializes a game object.
    '''
    def __init__(self):
        self.num_ships = 5
        self.over = False
        self.grid = []
        self.ship_locations = []
    
    '''
    This method randomly generates unique locations
    for ships.
    '''
    def place_ships(self):
        current_ships = []
        while len(current_ships) < 5:
            #selecting random row and column for ship
            row = random.randint(0, len(self.grid) - 1)
            col = random.randint(0, len(self.grid) - 1)
            # checking for uniqueness of ship location
            if ((row, col) not in current_ships):
                current_ships.append((row, col))
        self.ship_locations = current_ships

    '''
    This method displays the current grid to the player.
    '''
    def show_grid(self):
        for row in self.grid:
            print("".join(row))
    
    '''
    This method generates the grid and ships, and lets the 
    user play the game.
    '''
    def play(self):
        # creating our grid
        display = Grid.Grid()
        display.make_grid()
        self.grid = display.display
        # generating ships
        self.place_ships()
        print("Let the Battle Begin!")
        self.show_grid()
        count = 0
        while (not self.over):
            # getting player's row/col selections
            print("Possible row values: 0, 1, 2, 3, 4")
            print("Possible column values: 0, 1, 2, 3, 4")
            row = int(input("Enter your row : "))
            # check to make sure input is valid
            if not self.check_boundary(row):
                print("That is not a valid row")
                continue
            col = int(input("Enter your column : "))
            # check to make sure input is valid
            if not self.check_boundary(col):
                print("That is not a valid column")
                continue
            # checking if hit or miss
            if (row, col) in self.ship_locations:
                self.grid[row][col] = "X"
                count += 1
                self.show_grid()
                print("You took down a ship!")
            else:
                self.grid[row][col] = "O"
                self.show_grid()
                print("You missed, fire again!")
            # updating game state
            if count >= 5:
                self.over = True
        print("Good job you won your Battle!")
        # return for unit testing
        return count

    def check_boundary(self, val):
        if val < 0 or val > 4:
            return False
        return True
        

'''
This function creates a game object
and starts the game for a player.
'''
def start():
    game1 = Game()
    game1.play()
