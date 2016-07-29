import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]
 
 
def random_color(colors):
		return random.choice(colors)
	
pygame.init()

SCREEN_WIDTH = 800
SCRENEN_HEIGHT = 600

screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("CityScroller")

done = False

clock = pygame.time.Clock()

class Building():

	def __init__(self, x_point, y_point, width, height, color):
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = height
		self.color = color
		
	
	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

list_building = []
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(BLUE)
	
	my_building = Building( 2, 3, 30, 70, BLUE)
	
	list_building.append(my_building)


	for my_building in list_building:
		my_building.draw()

