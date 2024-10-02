import pygame
import time
pygame.font.init()

class Game:
	def __init__(self, screen, width, height):
		self.screen = screen
		self.font = pygame.font.Font("fonts/viner-hand-itc.ttf",150)
		self.message_color = pygame.Color("darkorange")
		self.WIDTH, self.HEIGHT = width, height

	# if player ran out of life or fell below the platform
	def _game_lose(self, player):
		player.game_over = True
		message = self.font.render('- 10 points', True, self.message_color)
		self.screen.blit(message,(self.WIDTH // 3 + 70, 70))
		pygame.display.update()
		#pygame.time.delay(10000)
	def _game_respawn(self, player):
		message = self.font.render('- 10 points', True, 'crimson')
		fail = self.font.render('Failed', True, 'crimson')
		gover = self.font.render('Game over', True, 'crimson')
		player.points -= 10
		if player.points < 0:
			player.points = 0
		if player.jump in player.jumps:
			player.jump += 1
		self.screen.blit(gover, (self.WIDTH // 3, 150))
		self.screen.blit(fail, (self.WIDTH // 3, 320))
		self.screen.blit(message, (self.WIDTH // 4, 450))
		pygame.display.update()
		pygame.time.delay(10000)
	def game_over(self):
		message = self.font.render('Game over!', True, 'crimson')
		self.screen.blit(message, (self.WIDTH // 4, 150))
		pygame.display.update()
		pygame.time.delay(10000)




	# if player reach the goal
	def _game_win(self, player):
		message = self.font.render('+ 50 points', True, self.message_color)
		player.points += 50
		self.screen.blit(message, (self.WIDTH // 4, 170))
		pygame.display.update()
		#pygame.time.delay(10000)
		#player.game_over = True
		#player.win = True
		#message = self.font.render('You Win!!', True, self.message_color)
		#self.screen.blit(message,(self.WIDTH // 3, 70))
		#player.points += 50
		#pygame.time.delay(10000)

	def ai_state(self, player):
		if player.rect.y >= self.HEIGHT - 30:
			self._game_respawn(player)
			return 'respawn'
		else:
			return None

	# checks if the game is over or not, and if win or lose
	def game_state(self, player, goal):
		if player.rect.y >= self.HEIGHT:
			self._game_respawn(player)
			return 'respawn'
		elif player.rect.colliderect(goal.rect):
			#self._game_win(player)
			return 'next'
		else:
			return None

	def show_life(self, player):
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		# life_rect = life_image.get_rect(topleft = pos)
		indent = 0
		for life in range(player.life):
			indent += life_size
			self.screen.blit(life_image, (indent, life_size))
	def show_score(self, player):
		life_size = 30
		indent = 0
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		message = self.font.render(f'Score: {player.points}', True, self.message_color)
		self.screen.blit(message, (1, 1))
		#pygame.display.update()
	def show_level(self, player):
		life_size = 30
		indent = 0
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		message = self.font.render(f'level: {player.level + 1}', True, self.message_color)
		self.screen.blit(message, (500, 1))
		#pygame.display.update()
	def show_jumps(self, player):
		life_size = 30
		indent = 0
		life_size = 30
		img_path = "assets/life/life.png"
		life_image = pygame.image.load(img_path)
		life_image = pygame.transform.scale(life_image, (life_size, life_size))
		message = self.font.render(f'jump: {player.jump}', True, self.message_color)
		self.screen.blit(message, (900, 1))
		#pygame.display.update()
	'''
	def _restart(self, player):
		player.game_over = False
		player.life = 5
		player
	'''