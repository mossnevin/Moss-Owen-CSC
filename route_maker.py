
import pygame as py
import os, json as js


py.init()

# ----------Set up the display-----------
display_width, display_height = 800, 600
screen = py.display.set_mode(
    (display_width, display_height),
    py.RESIZABLE
)
py.display.set_caption("Route Maker")

#holds panel dimensions
holds_panel_width = display_width
holds_panel_height = 100


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

# --------------Holds dictionary and size, colour, and type variables-------------- 
with open("inventory.json", "r") as f:
    holds_data = js.load(f)

size_properies = {
    "Small": 10,
    "Medium": 20,
    "Large": 30
}

colour_properies = {
    "Black": "#000000",
    "Blue": "#0000ff",
    "Red": "#ff0000",
    "Green": "#31b431",
    "Yellow": "#ffff00",
    "Purple": "#BD5DBD",
    "orange": "#FF9100"
    
}




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

    mouse_down = py.mouse.get_pressed()[0]
 
    

    # -----------Panel-------------
    display_width, display_height = py.display.get_window_size()
    panel_surface_pos = screen

    # Panel surface
    holds_panel_width = display_width
    holds_panel = py.Surface((holds_panel_width, holds_panel_height))
    holds_panel.fill(("#c8c8c8"))

    # Resizing with mouse
    
    mouse_grab_area = py.Rect(0, display_height - holds_panel_height - 5, holds_panel_width, 10)
    

    if mouse_grab_area.collidepoint(py.mouse.get_pos()):
        ready_to_drag = True
    else:
        ready_to_drag = False

    if ready_to_drag:
        py.mouse.set_cursor(py.SYSTEM_CURSOR_SIZENS)
    else:
        py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

    print(mouse_down, ready_to_drag)
    if mouse_down and ready_to_drag:
        new_mouse_y = py.mouse.get_pos()[1]
        new_height = display_height - new_mouse_y
        min_h = 20
        max_h = max(40, display_height - 40)
        holds_panel_height = max(min_h, min(max_h, new_height))
        

    # Drawing on the panel
    py.draw.line(holds_panel, ("#000000"), (0, 0), (holds_panel_width, 0), 2)
    
    grid.update(display_width, display_height)
    
    #Diplay holds on the panel
    for hold in holds_data:
        hold_size = size_properies[hold["size"]]
        hold_colour = colour_properies[hold["colour"]]
        py.draw.circle(holds_panel, hold_colour, (hold_size, holds_panel_height // 2), hold_size // 2)


    # -----------Drawing for the main screen-------------
    screen.fill(("#ffffffff"))


    for cell in grid.grid:
        py.draw.circle(screen, ("#000000"), cell, 2)

    

    # ------------------------     
    # Update the display
    screen.blit(holds_panel, (0, display_height - holds_panel_height))
    py.display.flip()