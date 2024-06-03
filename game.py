from random import randint
from globals import *


class Bird:
	def __init__(self, color=(220, 220, 0)):
		self.alive = True
		self.color = color
		self.vel = -HEIGHT
		self.height = H_HEIGHT
		self.x = WIDTH // 3
		self.radius = WIDTH // 15

	def update(self, ground, dt):
		self.vel += g * dt
		self.height = min(self.height + self.vel * dt, ground - self.radius)

		if self.height < self.radius:
			self.height = self.radius
			self.vel = 0

		if not self.alive: self.color = (120, 120, 120)
		else: self.color = (220, 220, 0)


class Pipe:
	def __init__(self, color=(0, 200, 0), x=WIDTH):
		self.color = color
		self.x = x
		self.height = randint(HEIGHT // 5 * 2, HEIGHT // 5 * 4)
		self.width = WIDTH // 4
		self.gap = HEIGHT // 4
		self.passed = False

	def update(self, speed, dt):
		self.x -= speed * dt

		if self.x <= - WIDTH // 4:
			self.x = WIDTH+WIDTH//4
			self.height = randint(HEIGHT // 5 * 2, HEIGHT // 5 * 4)
			self.passed = False


class Environment:
	def __init__(self, speed=WIDTH//3):
		self.Bird = Bird()
		self.Pipe1, self.Pipe2 = Pipe(), Pipe(x=WIDTH+H_WIDTH+WIDTH//4)
		self.speed = speed
		self.points = 0
		self.ground = False
		self.ground_height = HEIGHT // 6 * 5
		self.ground_color = (128, 64, 48)

	def update(self, dt):
		self.Bird.update(self.ground_height, dt)
		self.collide()

		if self.Bird.alive:
			self.Pipe1.update(self.speed, dt)
			self.Pipe2.update(self.speed, dt)
		

	def collide(self):
		if self.Bird.alive:
			if self.Bird.x >= self.Pipe1.x and self.Bird.x <= self.Pipe1.x + self.Pipe1.width:
				if self.Bird.height + self.Bird.radius >= self.Pipe1.height or \
				   self.Bird.height - self.Bird.radius <= self.Pipe1.height - self.Pipe1.gap:
					self.Bird.alive = False
			elif self.Bird.x > self.Pipe1.x + self.Pipe1.width and not self.Pipe1.passed:
				self.Pipe1.passed = True
				self.points += 1

			if self.Bird.x >= self.Pipe2.x and self.Bird.x <= self.Pipe2.x + self.Pipe2.width:
				if self.Bird.height + self.Bird.radius >= self.Pipe2.height or \
				   self.Bird.height - self.Bird.radius <= self.Pipe2.height - self.Pipe2.gap:
					self.Bird.alive = False
			elif self.Bird.x > self.Pipe2.x + self.Pipe2.width and not self.Pipe2.passed:
				self.Pipe2.passed = True
				self.points += 1
		
		if self.Bird.height + self.Bird.radius >= self.ground_height:
			self.Bird.alive = False
			self.ground = True
