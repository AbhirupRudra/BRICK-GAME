import pygame, sys
from game import Game
from colors import Colors
import time

pygame.init()

title_font = pygame.font.Font(None, 30)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
pause_surface = title_font.render("PAUSED", True, Colors.white)
play_surface = title_font.render("PLAY", True, Colors.white)

btn_font = pygame.font.Font(None, 18)
start_txt = btn_font.render("START/", True, Colors.white)
restart_txt = btn_font.render("RESTART", True, Colors.white)
s_txt = btn_font.render("(S)", True, Colors.white)
pp1_txt = btn_font.render("PLAY/", True, Colors.white)
pp2_txt = btn_font.render("PAUSE", True, Colors.white)
pp_txt = btn_font.render("(P)", True, Colors.white)
music_txt = btn_font.render("MUSIC", True, Colors.white)
m_txt = btn_font.render("(M)", True, Colors.white)

sbtn_font = pygame.font.Font(None, 12)
fd_txt1 = sbtn_font.render("FIVE", True, Colors.white)
fd_txt2 = sbtn_font.render("DOWN", True, Colors.white)
down_txt = sbtn_font.render("DOWN", True, Colors.white)
left_txt = sbtn_font.render("LEFT", True, Colors.white)
right_txt = sbtn_font.render("RIGHT", True, Colors.white)
rotate_txt = sbtn_font.render("ROTATE", True, Colors.white)

score_rect = pygame.Rect(240, 55, 120, 30)
next_rect = pygame.Rect(240, 215, 120, 100)
start_game = False
pp = True
pp_time = 0.0

screen = pygame.display.set_mode((370, 680))
pygame.display.set_caption("BRICK GAME ~ ABHIRUP RUDRA")

clock = pygame.time.Clock()

game = Game()
game.music()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 500)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 233<=mouse[0]<=247 and 473<=mouse[1]<=487:
				start_game = True
			if 183<=mouse[0]<=197 and 473<=mouse[1]<=487:
				pp = not pp
				pp_time = time.time()
			if 133<=mouse[0]<=147 and 473<=mouse[1]<=487:
				game.music()
			if game.game_over == True and start_game == True:
				game.game_over = False
				start_game = False
				game.reset()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				start_game = True
			if event.key == pygame.K_p:
				pp = not pp
				pp_time = time.time()
			if event.key == pygame.K_m:
				game.music()
			if game.game_over == True and start_game == True:
				game.game_over = False
				start_game = False
				game.reset()
		if event.type == pygame.MOUSEBUTTONDOWN and start_game == True and pp == True:
			if 85<=mouse[0]<=115 and 535<=mouse[1]<=565 and game.game_over == False:
				game.move_down(5, True)
			if 85<=mouse[0]<=115 and 605<=mouse[1]<=635 and game.game_over == False:
				game.move_down(1, True)
			if 50<=mouse[0]<=80 and 570<=mouse[1]<=600 and game.game_over == False:
				game.move_left()
			if 120<=mouse[0]<=150 and 570<=mouse[1]<=600 and game.game_over == False:
				game.move_right()
			if 245<=mouse[0]<=295 and 560<=mouse[1]<=610 and game.game_over == False:
				game.rotate()
		if event.type == pygame.KEYDOWN and start_game == True and pp == True:
			if event.key == pygame.K_f and game.game_over == False:
				game.move_down(5, True)
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down(1, True)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False and start_game == True and pp == True:
			game.move_down(1, False)

	# MOUSE POSITION VALUES
	mouse = pygame.mouse.get_pos()

	# SCORES TAG
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	# BACKGROUND FILL
	screen.fill(Colors.light_orange)
	screen.blit(score_surface, (270, 20, 50, 50))
	screen.blit(next_surface, (277, 180, 50, 50))

	# GAME OVER TAG
	if game.game_over == True:
		screen.blit(game_over_surface, (240, 380, 50, 50))
	
	# PAUSE SURFACE
	if pp == False and start_game == True:
		screen.blit(pause_surface, (255, 380, 50, 50))

	# PLAY SURFACE
	if pp == True and start_game == True and (time.time() - pp_time <= 5):
		screen.blit(play_surface, (270, 380, 50, 50))

	# SCORE SURFACE
	pygame.draw.rect(screen, Colors.dark_green, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))

	# NEXT BLOCK SURFACE
	pygame.draw.rect(screen, Colors.dark_green, next_rect, 0, 10)
	game.draw(screen)

	# START/RESTART BUTTON
	pygame.draw.circle(screen, (255, 0, 0), [240, 480], 7, 0)
	if 233<=mouse[0]<=247 and 473<=mouse[1]<=487:
		pygame.draw.circle(screen, (245, 64, 64), [240, 480], 7, 0)
	screen.blit(start_txt, (222, 495, 50, 50))
	screen.blit(restart_txt, (217, 510, 50, 50))
	screen.blit(s_txt, (233, 525, 50, 50))

	# PLAY/PAUSE BUTTON
	pygame.draw.circle(screen, (0, 255, 0), [190, 480], 7, 0)
	if 183<=mouse[0]<=197 and 473<=mouse[1]<=487:
		pygame.draw.circle(screen, (83, 245, 83), [190, 480], 7, 0)
	screen.blit(pp1_txt, (174, 495, 50, 50))
	screen.blit(pp2_txt, (170, 510, 50, 50))
	screen.blit(pp_txt, (183, 525, 50, 50))

	# SOUND BUTTON
	pygame.draw.circle(screen, (0,255,0), [140, 480], 7, 0)
	if 133<=mouse[0]<=147 and 473<=mouse[1]<=487:
		pygame.draw.circle(screen, (83, 245, 83), [140, 480], 7, 0)
	screen.blit(music_txt, (120, 495, 50, 50))
	screen.blit(m_txt, (130, 510, 50, 50))

	# FULL DOWN BUTTON
	pygame.draw.circle(screen, (255, 0, 0), [100, 550], 15, 0)
	if 85<=mouse[0]<=115 and 535<=mouse[1]<=565:
		pygame.draw.circle(screen, (245, 64, 64), [100, 550], 15, 0)
	screen.blit(fd_txt1, (90, 515, 50, 50))
	screen.blit(fd_txt2, (87, 525, 50, 50))

	# STEP DOWN BUTTON
	pygame.draw.circle(screen, (255, 0, 0), [100, 620], 15, 0)
	if 85<=mouse[0]<=115 and 605<=mouse[1]<=635:
		pygame.draw.circle(screen, (245, 64, 64), [100, 620], 15, 0)
	screen.blit(down_txt, (87, 638, 50, 50))

	# LEFT SHIFT BUTTON
	pygame.draw.circle(screen, (255, 0, 0), [65, 585], 15, 0)
	if 50<=mouse[0]<=80 and 570<=mouse[1]<=600:
		pygame.draw.circle(screen, (245, 64, 64), [65, 585], 15, 0)
	screen.blit(left_txt, (53, 603, 50, 50))

	# RIGHT SHIFT BUTTON
	pygame.draw.circle(screen, (255, 0, 0), [135, 585], 15, 0)
	if 120<=mouse[0]<=150 and 570<=mouse[1]<=600:
		pygame.draw.circle(screen, (245, 64, 64), [135, 585], 15, 0)
	screen.blit(right_txt, (123, 603, 50, 50))

	# ROTATE BUTTON
	pygame.draw.circle(screen, (255, 0, 0), [270, 585], 25, 0)
	if 245<=mouse[0]<=295 and 560<=mouse[1]<=610:
		pygame.draw.circle(screen, (245, 64, 64), [270, 585], 25, 0)
	screen.blit(rotate_txt, (254, 613, 50, 50))


	pygame.display.update()
	clock.tick(60)
