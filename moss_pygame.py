import pygame as py
import os

py.init()

mouse_x, mouse_y = py.mouse.get_pos()
mousedown = False
wall_spots = []
clock = py.time.Clock()



def clear():
    os.system("cls")

def interactable_wall_1():
    
    WIDTH, HEIGHT = 1080, 720
    screen = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
    py.display.set_caption("Interactable_Wall_1()")


    does_offset = 1
    mousedown = False
    circle_pos = (screen.get_width() / 2, screen.get_height() - 80)
    circle_radius = 20
    y_hole_distance = 40
    x_hole_distance = y_hole_distance * 2
    


    for n in range(screen.get_height() - 100):
        if n % y_hole_distance == 0:
            does_offset += 1
            for i in range(screen.get_width()):
                if i % x_hole_distance == 0:
                    if does_offset % 2 == 0:
                        offset = x_hole_distance - x_hole_distance / 4
                    else:
                        offset = x_hole_distance / 4
                    wall_spots.append((i + offset, n + y_hole_distance / 2))




    run = True
    while run:
        
        
        
        mouse_x, mouse_y = py.mouse.get_pos()

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.MOUSEBUTTONDOWN:
                mousedown = True
                circle_pos = (mouse_x, mouse_y)
            elif event.type == py.MOUSEBUTTONUP:
                mousedown = False

        screen.fill("black")

        for i in wall_spots:
            py.draw.circle(screen, "red", i, 2)

        
        

        py.draw.circle(screen, "green", circle_pos, circle_radius)

        
        

        

        py.display.flip()
        clock.tick(60)


def main_menu():
    WIDTH, HEIGHT = 1080, 720
    screen = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
    py.display.set_caption("My Game")

    run = True
    while run:
        

        mouse_x, mouse_y = py.mouse.get_pos()
        mousedown = False
        spacing = 20

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.MOUSEBUTTONDOWN:
                mousedown = True
                
            elif event.type == py.MOUSEBUTTONUP:
                mousedown = False
        if mouse_y > spacing and mouse_y < (screen.get_height() - spacing) and mousedown:
            if mouse_x > spacing and mouse_x < ((screen.get_width() - (spacing * 4)) / 3) + spacing:
                run = False
                interactable_wall_1()
            elif mouse_x > ((screen.get_width() - (spacing * 4)) / 3) + (spacing * 2) and mouse_x < (screen.get_width() - (spacing * 4)) / 3 * 2 + (spacing * 2):
                run = False
                print("interactable_wall_2()")
            elif mouse_x > ((screen.get_width() - (spacing * 4)) / 3) * 2 + (spacing * 3) and mouse_x < ((screen.get_width() - (spacing * 4)) / 3) * 3 + (spacing * 3):
                run = False
                print("interactable_wall_3()")
        
        


        screen.fill("grey30")

        

        py.draw.rect(screen, "deepskyblue", (spacing, spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))
        py.draw.rect(screen, "green2", (((screen.get_width() - (spacing * 4)) / 3) + (spacing * 2), spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))
        py.draw.rect(screen, "purple1", ((((screen.get_width() - (spacing * 4)) / 3) * 2) + (spacing * 3), spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))

        




        py.display.flip()

clear()
interactable_wall_1()
py.quit()