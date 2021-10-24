import pygame
from pygame.locals import *
from random import randint

#pygame inits
pygame.init()
pygame.mixer.init()

SCREEN_SIZE = (1200, 720)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("social credit score test")

#fonts
font0 = pygame.font.SysFont("Liberation mono", 50, True)
font1 = pygame.font.SysFont("Liberation mono", 25, True)

#music
music = pygame.mixer.Sound("mus/redsun.wav")
square_sfx = pygame.mixer.Sound("mus/square.wav")
music.set_volume(0.2)

#sounds
up15_sfx = pygame.mixer.Sound("mus/15up.wav")
down15_sfx = pygame.mixer.Sound("mus/ROCK.wav")
lose_sfx = pygame.mixer.Sound("mus/lose.wav")

#sound channels
channel_0 = pygame.mixer.Channel(0)
channel_1 = pygame.mixer.Channel(1)
channel_2 = pygame.mixer.Channel(2)

#game clock
game_clock = pygame.time.Clock()

class test():
	""" Interactive test class """
	def __init__(s):
		global font0, font1
		
		s.bcg0 = pygame.image.load("vis/test1.jpg").convert()
		s.bcg1 = pygame.image.load("vis/test2.jpg").convert()
		s.bcg2 = pygame.image.load("vis/test3.jpg").convert()
		s.bcg3 = pygame.image.load("vis/test4.jpg").convert()
		s.bcg4 = pygame.image.load("vis/test5.jpg").convert()
		s.bcg5 = pygame.image.load("vis/test6.jpg").convert()
		s.bcg6 = pygame.image.load("vis/test7.png").convert()
		
		s.text_win = font0.render("GOOD COMRADE! GLORY TO THE CCP!", False, (255, 0, 0))
		s.bcg_win = pygame.image.load("vis/win.png").convert()
		
		s.text_lose = font0.render("YOU LOSE, PREPARE FOR EXECUTION", False, (255, 0, 0))
		s.bcg_lose = pygame.image.load("vis/lose.png").convert()
		
		s.img_wock = pygame.image.load("vis/wock.png").convert()
		s.img_xina = pygame.image.load("vis/xina.png").convert()

		s.up_15 = pygame.image.load("vis/15.png").convert()
		s.down_15 = pygame.image.load("vis/15down.png").convert()

		s.text0 = font0.render("SOCIAL CREDID SCORE TEST", False, (255, 255, 255))
		s.text01 = font0.render("BEGIN", False, (255, 255, 255))
		
		s.text1 = font0.render("IS COUNTRY A TAIWAN???", False, (255, 0, 0))
		s.text11 = font1.render("1. IS'NT", False, (255, 0, 0))
		s.text12 = font1.render("2. IS", False, (255, 0, 0))
		
		s.text2 = font0.render("HOW LONG CAN YOU PLAY GAMES IN WEEK?", False, (255, 0, 0))
		s.text21 = font1.render("1. Less 1 Hour", False, (255, 0, 0))
		s.text22 = font1.render("2. Less 5 Hours", False, (255, 0, 0))
		s.text23 = font1.render("3. No more than 3 Hours", False, (255, 0, 0))
		s.text24 = font1.render("4. No more than 4 Hrs", False, (255, 0, 0))
		
		s.text3 = font0.render("HOW MANY CHILD'S CAN YOU HAVE?", False, (255, 0, 0))
		s.text31 = font1.render("1. Less than 1.5", False, (255, 0, 0))
		s.text32 = font1.render("2. Less than 5", False, (255, 0, 0))
		s.text33 = font1.render("3. No more than 2", False, (255, 0, 0))
		s.text34 = font1.render("4. No more than 4", False, (255, 0, 0))
		
		s.text4 = font0.render("DO YOU LOVE CHILI SAUCE?????", False, (255, 0, 0))
		s.text41 = font1.render("1. YES, GLORY TO THE CP", False, (255, 0, 0))
		s.text42 = font1.render("2. Very good, Xi Jinping Great leader", False, (255, 0, 0))
		s.text43 = font1.render("3. I am American", False, (255, 0, 0))
		s.text44 = font1.render("4. YES, CHINA GREAT NATION!!", False, (255, 0, 0))
		
		s.text5 = font0.render("Can you dance in public, on squares??", False, (255, 0, 0))
		s.text51 = font1.render("1. YES, if you have permit", False, (255, 0, 0))
		s.text52 = font1.render("2. Never", False, (255, 0, 0))
		s.text53 = font1.render("3. Yes", False, (255, 0, 0))
		s.text54 = font1.render("4. Only during national holidays", False, (255, 0, 0))
		
		s.text6 = font0.render("Do you know this image?", False, (255, 0, 0))
		s.text61 = font1.render("1. yes", False, (255, 0, 0))
		s.text62 = font1.render("2. NO, NEVER, GLORY TO THE CCP", False, (255, 0, 0))
				
		s.time_clicked = 0
		
		s.state = 0
		s.state2 = 0
	
		s.score = 0
		
		s.sfx_playing = False
		s.square_play = False
		s.sfx_lose = False
		s.sfx_win = False
		
	def draw(s):
		""" Draws appropriate images on the screen """
		global screen, up15_sfx, down15_sfx, square_sfx, lose_sfx
		time_now = pygame.time.get_ticks()
		if s.state2 == 1:
			screen.blit(s.up_15, (0, 0))
			screen.blit(s.img_xina, (50, 50))
			if not s.sfx_playing:
				s.score += 1
				channel_1.play(up15_sfx)
				s.sfx_playing = True
				
			if time_now - s.time_clicked > 2000:
				s.state2 = 0
		elif s.state2 == 2:
			screen.blit(s.down_15, (0, 0))
			screen.blit(s.img_wock, (50, 50))
			if not s.sfx_playing:
				s.score -= 1
				channel_1.play(down15_sfx)
				s.sfx_playing = True
			if time_now - s.time_clicked > 2000:
				s.state2 = 0
				
		if s.state2 == 0:
			if s.state == 0:
				s.sfx_playing = False
				screen.blit(s.bcg0, (0, 0))
				screen.blit(s.text0, (220, 50))
				screen.blit(s.text01, (500, 500))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 1:
				s.sfx_playing = False
				screen.blit(s.bcg1, (0, 0))
				screen.blit(s.text1, (220, 50))
				screen.blit(s.text11, (100, 500))
				screen.blit(s.text12, (600, 500))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 2:
				s.sfx_playing = False
				screen.blit(s.bcg2, (0, 0))
				screen.blit(s.text2, (0, 50))
				screen.blit(s.text21, (100, 500))
				screen.blit(s.text22, (600, 500))
				screen.blit(s.text23, (100, 600))
				screen.blit(s.text24, (600, 600))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 3:
				s.sfx_playing = False
				screen.blit(s.bcg3, (0, 0))
				screen.blit(s.text3, (220, 50))
				screen.blit(s.text31, (100, 500))
				screen.blit(s.text32, (600, 500))
				screen.blit(s.text33, (100, 600))
				screen.blit(s.text34, (600, 600))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 4:
				s.sfx_playing = False
				screen.blit(s.bcg4, (0, 0))
				screen.blit(s.text4, (220, 50))
				screen.blit(s.text41, (100, 500))
				screen.blit(s.text42, (600, 500))
				screen.blit(s.text43, (100, 600))
				screen.blit(s.text44, (600, 600))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 5:
				s.sfx_playing = False
				screen.blit(s.bcg5, (0, 0))
				screen.blit(s.text5, (220, 50))
				screen.blit(s.text51, (100, 500))
				screen.blit(s.text52, (600, 500))
				screen.blit(s.text53, (100, 600))
				screen.blit(s.text54, (600, 600))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 6:
				if not s.square_play:
					channel_0.play(square_sfx, 50)
					s.square_play = True
				s.sfx_playing = False
				screen.blit(s.bcg6, (0, 0))
				screen.blit(s.text6, (220, 50))
				screen.blit(s.text61, (100, 500))
				screen.blit(s.text62, (600, 500))
				s.time_clicked = pygame.time.get_ticks()
			elif s.state == 7 and s.score < 4:
				#if not s.sfx_lose:
				#	channel_2.play(lose_sfx)
				#	s.sfx_lose = True
				screen.blit(s.bcg_lose, (0, 0))
				screen.blit(s.img_wock, (50, 50))
				screen.blit(s.text_lose, (220, 50))
			elif s.state == 7 and s.score >= 4:
				screen.blit(s.bcg_win, (0, 0))
				screen.blit(s.img_xina, (50, 50))
				screen.blit(s.text_win, (220, 600))
		
			
		#elif s.screen == 2:
			
	def update(s, num):
		""" Updates the state variable, responsible for images shown in draw() """
		s.state = num
	
	def set_state2(s, num):
		""" Changes the state2 vaiable, responsible for UP/DOWN points image """
		s.state2 = num
	
		
		
change = 0	
game = test()

GAME_RUNNING = True;
channel_0.play(music, 50)
while GAME_RUNNING:
	
	game_clock.tick(30)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			GAME_RUNNING = False
		if game.state < 7:
			if event.type == pygame.MOUSEBUTTONDOWN and game.state2 == 0 and game.state > 0:
				change += 1
				if randint(1, 10) < 8:
					game.set_state2(1)
				else:
					game.set_state2(2)
			elif event.type == pygame.MOUSEBUTTONDOWN and game.state2 == 0 and game.state == 0:
				change += 1

	#screen.blit(game.bcg0, (0, 0))
	game.update(change)
	game.draw()
	

	pygame.display.update()



pygame.mixer.quit()
pygame.quit()
