import pygame, sys, random

#=================================================================================
# Before anything I would like to thank you for trying this program out. I really
# appreciate it! The coin flip race will start as soon as you start the program up.
# There are a bunch of variables that allow you to change the settings of the race.
# You can change the number of AI players just from adding or removeing 2 lines of code.
# I trust that you can figure it out. You can edit this program as much as you like.
#
# Coin Flip Program made by: Tyler Dillard, 2022
#==================================================================================

#General Stuff
pygame.init()
clock = pygame.time.Clock()

# Window Settings
screenWidth = 400
screenHeight = 400

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Coin Flip")

# Colors
black = pygame.Color(0, 0, 0)
darkgrey = pygame.Color(50, 50, 50)

# Font
font = pygame.font.Font(None, 40)

# Important Variables (CF stands for Coin Flip by the way)
end = False # Most important variable, decides if the players should keep flipping coins or not.

cf_limit = 15 # How many points a player needs to get before ending the game.

cf_winChance = 50 # The value can range from 0 to 100

cl_delay = 1 # The amount of seconds between coin flips

# The Coin Flip Player Class, handles the code for all Coin Flip player
class cf_player():
    def __init__(self, x, y, width, height):
        # Decides the position and size of the instance.
        self.rect = pygame.Rect(x - (width/2), y - (height/2), width, height)
        
        self.points = 0 # Counts how many times an instance wins a coin flip
        
        self.roll = 0 # Value that determines whether a player has won a coin flip or not
        
    def tick(self, r, g, b):
        global end
        # This funtion activates every time the end variable is false
        if end != True:
            self.roll = random.randint(0,100)
            # Checks to see if the roll is sucessful or not
            if self.roll >= cf_winChance: # Result is determined by the values of self.roll and cf_winchance
                self.points = self.points + 1
                # When a player's points is more or equal to cf_limit, end will be switched to true. Stopping all players from rolling and gaining points
                if self.points >= cf_limit:
                    end = True
                    print("The game as ended.")
        
        # Draws the instance and the text for displaying the instance's score.
        pygame.draw.rect(screen, (r, g, b), self)
        self.text = font.render(str(self.points), True, black)
        screen.blit(self.text, self.rect.topleft)
        
# cf_player instances.
# (x, y, width, height)
P1 = cf_player(100, 100, 50, 50)
P2 = cf_player(200, 100, 50, 50)
P3 = cf_player(300, 100, 50, 50)
P4 = cf_player(100, 200, 50, 50)
P5 = cf_player(200, 200, 50, 50)
P6 = cf_player(300, 200, 50, 50)

print("Everything seems to be funtioning well...")

# Game Loop
while True:
    for event in pygame.event.get():
        #Allow you to close the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Adds a small delay between coin flips.
    if end != True:
        pygame.time.wait(cl_delay * 1000)
    
    # Draws program elements
    screen.fill(darkgrey)
    
    # Draws the cf_player instances.
    # (r, g, b)
    P1.tick(255, 0, 0)
    P2.tick(0, 255, 0)
    P3.tick(0, 0, 255)
    P4.tick(255, 255, 0)
    P5.tick(0, 255, 255)
    P6.tick(255, 0, 255)
    
    # Updates the screen.
    pygame.display.flip()
    clock.tick(60)