
import pygame as py

py.init()

# ----------Set up the display-----------
display_width, display_height = 800, 600
screen = py.display.set_mode(
    (display_width, display_height),
    py.RESIZABLE
)
py.display.set_caption("Route Maker")


# ---------Grid class-------------
class Grid:
    def __init__(self, x, y, size=(10, 10)):
        self.x = x
        self.y = y
        self.size = size

    # Update grid cell positions
    def update(self, width = py.display.get_window_size()[0], height = py.display.get_window_size()[1]):
        global holds_panel_height

        # Calculate the gap between cells based on the new window size
        self.width = width 
        self.height = (height - holds_panel_height)
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

grid = Grid(0, 0, (25, 25)) 

# --------------Main loop-------------- 
run = True
while run:
    # ----------Event handling-------------
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        elif event.type == py.VIDEORESIZE:
            display_width, display_height = event.size

    # ---- Mouse ----

    if py.mouse.get_pressed() == True:
        mouse_down = True
    else:
        mouse_down = False
 
    

    # -----------Panel-------------
    display_width, display_height = py.display.get_window_size()
    panel_surface_pos = 

    # Panel surface
    holds_panel_width = display_width
    holds_panel_height = 100
    holds_panel = py.Surface((holds_panel_width, holds_panel_height))
    holds_panel.fill(("#c8c8c8"))

    # Resizing with mouse
    mouse_grab_area = py.Rect(0, 0, holds_panel_width, 20).move(0, )
    

    if mouse_grab_area.collidepoint(py.mouse.get_pos()):
        ready_to_drag = True
        print("true")
    else:
        ready_to_drag = False
        print("false")

    # if ready_to_drag == True:
    #     py.mouse.set_cursor(py.SYSTEM_CURSOR_SIZENESW)
    #     print("ready")

    # else:
    #     py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

    
    
    

    # Drawing on the panel
    py.draw.line(holds_panel, ("#000000"), (0, 0), (holds_panel_width, 0), 2)
    
    grid.update(display_width, display_height)
    
    # -----------Drawing for the main screen-------------
    screen.fill(("#ffffffff"))


    for cell in grid.grid:
        py.draw.circle(screen, ("#000000"), cell, 2)

    

    # ------------------------     
    # Update the display
    screen.blit(holds_panel, (0, display_height - holds_panel_height))
    py.display.flip()