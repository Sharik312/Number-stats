import pygame, random, time # importing libraries
pygame.font.init() # initialising pygame font
pygame.init() # initialising pygame

# Creating color variables
RED = 255, 0, 0
GREEN  = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 255, 255, 255
WHITE = 0, 0, 0

# Assigning screen size variables
SC_WIDTH, SC_LENGTH = 600, 600

# Main function
def main():
    
    running = True
    while running:
        for event in pygame.event.get(): 
            if event == QUIT: # checking for quit
                running = False
            



"""

Back-End Task:
create function that will take in 2 parameters (num_range, user_guess)
num_range will be the range of numbers
create 3 ranges (1-10, 1-100, 1-1000)
then check if correct using user guess
return False/True if user is correct or not
num_range will be 1,2,3

"""
