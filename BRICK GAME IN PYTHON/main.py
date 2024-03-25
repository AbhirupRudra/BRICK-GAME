import pygame,sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 30)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

btn_font = pygame.font.Font(None, 18)
start_txt = btn_font.render("START/", True, Colors.white)
restart_txt = btn_font.render("RESTART", True, Colors.white)
s_txt = btn_font.render("(S)", True, Colors.white)
pp1_txt = btn_font.render("PLAY/", True, Colors.white)
pp2_txt = btn_font.render("PAUSE", True, Colors.white)
pp_txt = btn_font.render("(P)", True, Colors.white)
music_txt = btn_font.render("MUSIC", True, Colors.white)
m_txt = btn_font.render("(M)", True, Colors.white)

score_rect = pygame.Rect(240, 55, 120, 30)
next_rect = pygame.Rect(240, 215, 120, 100)
start_game = False
pp = True

screen = pygame.display.set_mode((370, 550))
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
			if event.key == pygame.K_m:
				game.music()
			if game.game_over == True and start_game == True:
				game.game_over = False
				start_game = False
				game.reset()
		if event.type == pygame.KEYDOWN and start_game == True and pp == True:
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False and start_game == True and pp == True:
			game.move_down()

	mouse = pygame.mouse.get_pos()
	#Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	screen.fill(Colors.light_orange)
	screen.blit(score_surface, (270, 20, 50, 50))
	screen.blit(next_surface, (277, 180, 50, 50))

	if game.game_over == True:
		screen.blit(game_over_surface, (240, 380, 50, 50))

	pygame.draw.rect(screen, Colors.dark_green, score_rect, 0, 10)
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
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

	pygame.display.update()
	clock.tick(60)