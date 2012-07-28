import pygame
import time
import curses

pygame.init()

up = pygame.mixer.Sound('no-hunger.wav')
down = pygame.mixer.Sound('no-problem.wav')

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.clear()
screen.addstr("Ready to accept up or down to play sounds or q to quit!")

while True:
	event = screen.getch()
	if event == ord('q'):
		break
	elif event == curses.KEY_UP:
		screen.clear()
		screen.addstr("You pressed up")
		up.play()
	elif event == curses.KEY_DOWN:
		screen.clear()
		screen.addstr("You pressed down")
		down.play()
	else:
		screen.clear()
		screen.addstr("You didn't press up, down or q to quit.")

curses.endwin()
