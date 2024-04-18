import pgzrun
import os


cwd = os.getcwd()
apple = Actor("img")

def draw():
    screen.clear()
    apple.draw()

pgzrun.go()
