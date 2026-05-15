
import pygame as py

py.init()

# Set up the display
width, height = 800, 600
screen = py.display.set_mode(
    (width, height),
    py.RESIZABLE
)
py.display.set_caption("Route Maker")


holds_panel_width = 20
holds_panel_height = 20
holds_panel = py.Surface((holds_panel_width, holds_panel_height))

# Class to create a grid of points on the screen
class Grid:
    def __init__(self, x, y, size=(10, 10)):
        self.x = x
        self.y = y
        self.size = size

    # Update grid cell positions
    def update(self, width = py.display.get_window_size()[0], height = py.display.get_window_size()[1]):

        # Calculate the gap between cells based on the new window size
        self.width = width 
        self.height = height
        self.gapx = self.width // self.size[0]
        self.gapy = self.height // self.size[1]
        self.gap = (min(self.gapx, self.gapy))
        
        # Adjust the position of the grid
        self.x = (self.width - self.gap * (self.size[0] - 1)) // 2
        self.y = (self.height - self.gap * (self.size[1] - 1)) // 2

        # Add the postions of the grid cells to the grid list
        self.grid = []
        for w in range(self.size[0]):
            for h in range(self.size[1]):  
                self.grid.append((self.x + w * self.gap, self.y + h * self.gap))

grid = Grid(0, 0, (20, 10)) # Create a grid with 20 columns and 10 rows

# Main loop
run = True
while run:
    # Event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        elif event.type == py.VIDEORESIZE:
            width, height = event.size
 
    width, height = py.display.get_window_size()

    # -----------Panel-------------

    # Panel surface
    holds_panel_width = width
    holds_panel_height = 50
    holds_panel = py.Surface((holds_panel_width, holds_panel_height))
    holds_panel.fill((200, 200, 200)) # Fill the panel with a color


    screen.fill((255, 255, 255))
    
    grid.update(width, height)

    

    for cell in grid.grid:
        py.draw.circle(screen, (0, 0, 0), cell, 2)

    
    print(height)
    screen.blit(holds_panel, (0, height - holds_panel_height)) # Draw the panel on the screen

    py.display.flip()