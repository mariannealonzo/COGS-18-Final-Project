#import pytest
import Game

'''
Test for place_ships() method

This tests to make sure that 5 ships were generated 
on the grid. This also ensures that the ship locations
are unique.

def test_unique_ships():
    game1 = Game.Game()
    game1.grid = [(0,0), (2,4), (3,1), (4,2), (2,3)]
    assert game1.place_ships() == 5
'''
'''
Test for play() method

This tests to make sure that all 5 ships were
destroyed when the game state is set to over.
Ensures game is running correctly.

def test_game_over():
    game1 = Game.Game()
    #// increment count x5
    assert game1.check_game_over() == True

'''

''' Test whether playeer input is within boundaries of our grid '''

def test_validLowerBoundary():
    game1 = Game.Game()
    assert game1.check_boundary(0) == True 

def test_invalidLowerBoundary():
    game1 = Game.Game()
    assert game1.check_boundary(-1) == False

def test_validUppeerBoundary():
    game1 = Game.Game()
    assert game1.check_boundary(4) == True 

def test_invalidUpperBoundary():
    game1 = Game.Game()
    assert game1.check_boundary(5) == False



