import pygame as py
py.init()

screen = py.display.set_mode((900, 900), py.RESIZABLE)
py.display.set_caption("Route Maker")

class Grid:
    def __init__(self, x, y, size=(10, 10)):
        self.x = x
        self.y = y
        self.size = size

    # Update grid cell positions
    def update(self):
        width, height = py.display.get_window_size()
        self.width = width
        self.height = height
        
        gapx = self.width // self.size[0]
        gapy = self.height // self.size[1]
        self.gap = min(gapx, gapy)
        centrex = (self.width - (self.size[0] * gapx)) // 2
        centrey = (self.height - (self.size[1] * gapy)) // 2
        print(centrex, centrey)
        self.x = centrex
        self.y = centrey
        self.grid = []
        for w in range(self.size[0]):
            for h in range(self.size[1]):  
                self.grid.append((self.x + w * self.gap, self.y + h * self.gap))




run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        elif event.type == py.VIDEORESIZE:
            screen = py.display.set_mode((event.w, event.h), py.RESIZABLE)

    screen.fill((0, 0, 0))
    grid = Grid(0, 0, (20, 10))
    grid.update()

    for cell in grid.grid:
        py.draw.circle(screen, (255, 255, 255), cell, 2)
    

    #print(grid.grid)
    
    # redraw your content here

    py.display.flip()
    