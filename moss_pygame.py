import pygame as py
import os

py.init()

def clear():
    os.system("cls")

def main_menu():
    WIDTH, HEIGHT = 1080, 720
    screen = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
    py.display.set_caption("My Game")

    run = True
    while run:

        mouse_x, mouse_y = py.mouse.get_pos()
        mouse_down = False
        spacing = 20

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == py.MOUSEBUTTONUP:
                mouse_down = False
        if mouse_y > spacing and mouse_y < (screen.get_height() - spacing) and mouse_down:
            if mouse_x > spacing and mouse_x < ((screen.get_width() - (spacing * 4)) / 3) + spacing:
                running = False
                print("interactable_wall_1()")
            elif mouse_x > ((screen.get_width() - (spacing * 4)) / 3) + (spacing * 2) and mouse_x < (screen.get_width() - (spacing * 4)) / 3 * 2 + (spacing * 2):
                running = False
                print("interactable_wall_2()")
            elif mouse_x > ((screen.get_width() - (spacing * 4)) / 3) * 2 + (spacing * 3) and mouse_x < ((screen.get_width() - (spacing * 4)) / 3) * 3 + (spacing * 3):
                running = False
                print("interactable_wall_3()")
        



        screen.fill("grey30")

        

        py.draw.rect(screen, "deepskyblue", (spacing, spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))
        py.draw.rect(screen, "green2", (((screen.get_width() - (spacing * 4)) / 3) + (spacing * 2), spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))
        py.draw.rect(screen, "purple1", ((((screen.get_width() - (spacing * 4)) / 3) * 2) + (spacing * 3), spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))

        




        py.display.flip()

clear()
main_menu()
py.quit()