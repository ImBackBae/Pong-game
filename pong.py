import pygame
import keyboard
import random
import ctypes
import os
class Player():
	def __init__(self, coord_x):
		self.x = coord_x
		self.y = HEIGHT//2
		self.point = 0

	def move_up(self):
		if self.y - 75 > 0:
			self.y -= SIDE

	def move_down(self):
		if self.y + 75 < HEIGHT:
			self.y += SIDE

	def draw(self):
		pygame.draw.rect(screen, WHITE, (self.x, self.y-75, SIDE, 150))

class Ball():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.vel = [10, random.randint(-4, 4)*5]

	def collision(self, p1, p2):
		if self.y <= 20:
			self.vel[1] = -self.vel[1]
		elif self.y >= HEIGHT-20:
			self.vel[1] = -self.vel[1]

		if self.x <= 20:
			p2.point += 1
			self.restart()
		elif self.x >= WIDTH-20:
			p1.point += 1
			self.restart()

	def collision_with_player(self, player1, player2):
		if self.x == 50 and self.y in [i for i in range(player1.y-75, player1.y + 151)]:
			self.bounce()
		elif self.x == 1230 and self.y in [i for i in range(player2.y-75, player2.y + 151)]:
			self.bounce()

	def update(self):
		self.x += self.vel[0]
		self.y += self.vel[1]

	def bounce(self):
		self.vel[0] = -self.vel[0]
		self.vel[1] = random.randint(-4, 4)*5

	def draw(self):
		pygame.draw.circle(screen, WHITE, (self.x, self.y), (10))

	def restart(self):	
		self.x = WIDTH//2
		self.y = HEIGHT//2
		self.vel = [random.choice([1, -1])*10, random.randint(-2, 2)*5]

def draw_points(p1, p2):
	font_point = pygame.font.SysFont('sitka', 200)
	
	show_p1 = font_point.render(str(p1), True, WHITE)
	show_p2 = font_point.render(str(p2), True, WHITE)
	p1_rect = show_p1.get_rect(centerx=WIDTH//4)
	p2_rect = show_p2.get_rect(centerx=WIDTH//2 + WIDTH//4)

	screen.blit(show_p1, p1_rect)
	screen.blit(show_p2, p2_rect)


def main():
	global WIDTH
	global HEIGHT
	global WHITE
	global BLACK
	global SIDE
	global screen

	WHITE = (255,255,255)
	BLACK = (0,0,0)
	WIDTH = 1280
	HEIGHT = 800
	SIDE = 20
	clock = pygame.time.Clock()

	pygame.init()
	screen = pygame.display.set_mode((WIDTH,HEIGHT), flags=pygame.SHOWN)
	running = True

	player1 = Player(SIDE)
	player2 = Player(WIDTH - SIDE*2)
	ball = Ball(WIDTH//2, HEIGHT//2)

	while running:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		player1.draw()
		player2.draw()
		
		ball.draw()
		ball.collision(player1, player2)
		ball.collision_with_player(player1, player2)
		ball.update()
		draw_points(player1.point, player2.point)
		for i in range(HEIGHT//50):
			pygame.draw.line(screen, WHITE, [WIDTH//2, i*50], [WIDTH//2, (i+1)*50 - 20], 5)
		if keyboard.is_pressed("w"):
			player1.move_up()
		elif keyboard.is_pressed("s"):
			player1.move_down()
		if keyboard.is_pressed("up"):
			player2.move_up()
		elif keyboard.is_pressed("down"):
			player2.move_down()
		clock.tick(50)
		pygame.display.flip()

main()
