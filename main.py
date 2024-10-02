import pygame, sys
from settings import *
from world import World
import os
pygame.init()
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
ranges = [[i, i + 150] for i in range(50, 3350, 150)]

#print(ranges)
class Platformer:
	def __init__(self):
		self.level = 0
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()
		self.player_event = False
		self.images = os.listdir('assets/terrain/background')
		self.bg_img = pygame.image.load('assets/terrain/background/1.jpg')
		self.bg_img = pygame.transform.scale(self.bg_img, (self.WIDTH, self.HEIGHT))
		self.state = None
		self.points = 100
		self.glevel = 0
		self.gjump = 0
	def respwan(self, player):
		#print(self.world.player2.sprite.rect.x)
		#print(self.world.player2.sprite.rect.x)
		for range in ranges:
			if range[0] <= player.sprite.rect.x < range[1]:
				player.sprite.rect.x = range[0]
		'''
		if self.world.player2.sprite.rect.x % 100 > 50:
			self.world.player2.sprite.rect.x -= (self.world.player2.sprite.rect.x % 100 + 20)
		else:
			self.world.player2.sprite.rect.x -= 50
		'''
		player.sprite.rect.y = 300
	def respawn2(self, player):
		player.sprite.rect.x = player.start[0]
		player.sprite.rect.y = player.start[1]

	def update_screen(self):
		self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()
		self.bg_img = pygame.transform.scale(self.bg_img, (self.WIDTH, self.HEIGHT))
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	def main(self):
		self.update_screen()
		self.world = World(world_map[self.glevel], self.screen, self.WIDTH, self.HEIGHT)
		self.world.player2.sprite.points = self.points
		self.world.player2.sprite.jump = self.gjump
		self.world.player2.sprite.level = self.glevel
		self.bg_img = pygame.image.load('assets/terrain/background/' + self.images[self.glevel])
		self.bg_img = pygame.transform.scale(self.bg_img, (self.WIDTH, self.HEIGHT))
		right_count = 0
		self.ai_event = None
		while True:
			if self.world.player2.sprite.jump > 302:
				break
			#print(self.world.player1.sprite.rect.y)
			self.screen.blit(self.bg_img, (0, 0))
			self.ai_event = None
			if abs(self.world.player1.sprite.rect.x + 5) < self.world.player2.sprite.rect.x:
				self.ai_event = 'space'
			if self.world.player1.sprite.rect.y <= 450 and self.ai_event == 'space':
				self.ai_event = 'right'
			if abs(self.world.player1.sprite.rect.x + 5) >= self.world.player2.sprite.rect.x:
				self.ai_event = None
			if abs(self.world.player1.sprite.rect.x + 5) > self.world.player2.sprite.rect.x:
				self.ai_event = 'space'
			if self.world.player1.sprite.rect.y <= 450 and self.ai_event == 'space':
				self.ai_event = 'left'
			if self.world.player1.sprite.rect.x == self.world.player2.sprite.rect.x:
				self.ai_event = None
			if self.world.player2.sprite.jump_fail():
				self.ai_event = 'right'
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.player_event = "left"
					if event.key == pygame.K_RIGHT:
						self.player_event = "right"
					if event.key == pygame.K_SPACE:
						self.world.player2.sprite.jump += 1
						self.player_event = "space"
				elif event.type == pygame.KEYUP:
					self.player_event = False

			state, state2 = self.world.update(self.player_event, self.ai_event)
			if state == 'restart':
				break
			if state == 'next':
				break
			if state == 'respawn' or state2 == 'respawn':
				#self.respawn2(self.world.player2)
				#self.respawn2(self.world.player1)
				break
			if state2 == 'respawn':
				self.respawn2(self.world.player1)
			pygame.display.update()
			self.clock.tick(60)
		if self.world.player2.sprite.jump > 302:
			self.world.game.game_over()
			return
		if state == 'next':
			self.glevel = self.world.player2.sprite.level + 1
			self.gjump = self.world.player2.sprite.jump
			self.level %= 6
			self.main()
		if state == 'restart' or state == 'respawn' or state2 == 'respawn':
			self.points = self.world.player2.sprite.points
			self.glevel = 0
			self.gjump = self.world.player2.sprite.jump
			self.main()


if __name__ == "__main__":
	play = Platformer()
	play.main()