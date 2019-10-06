import tkinter as tk
import time
from ant import *



s = int(input("Enter the size of each cell: "))


field = Map(
	*list(map(int, input("Enter the size of map as \"height, width\": ").split())),
	s
)

ant = Ant(
	*list(map(int, input("Enter the position of ant as \"x, y\": ").split())),
	s,
	int(input("Enter the angle of ant (0 or 90 or 180 or 270): ")), 
	field,
	left_color='red'
)

root= tk.Tk()
root.title("Ant")
canvas = tk.Canvas(root, width=field.width * s, height=field.height * s, bg='black')
canvas.pack()

for y in range(field.height):
	for x in range(field.width):
		
		canvas.create_rectangle(x * s, y * s, x * s + s, y * s + s, fill=field.get[y][x].color)
root.update()

while True:
	old_x = ant.x
	old_y = ant.y
	
	ant.next()
	canvas.create_rectangle(old_x * s, old_y * s, old_x * s + s, old_y * s + s, fill=field.get[old_y][old_x].color)
	
	root.update()