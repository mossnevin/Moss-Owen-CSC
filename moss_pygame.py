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
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
        



        screen.fill("grey30")

        spacing = 200

        py.draw.rect(screen, "deepskyblue", (spacing, spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))
        py.draw.rect(screen, "green2", (((screen.get_width() - (spacing * 4)) / 3) + (spacing * 2), spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))
        py.draw.rect(screen, "purple1", ((((screen.get_width() - (spacing * 4)) / 3) * 2) + (spacing * 3), spacing, (screen.get_width() - (spacing * 4)) / 3, screen.get_height() - (spacing * 2)))

        




        py.display.flip()

clear()
main_menu()
py.quit()