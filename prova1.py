import pygame, sys, time, random



pygame.init()

display_widht = 800
display_height = 600
block_size = 10

gameDisplay = pygame.display.set_mode((display_widht,display_height)) #grandezza finestra

pygame.display.set_caption("Gioco potente!") #da un nome alla finestra 


black = (0, 0, 0)
white = (255, 255, 255)
red  = (255, 0, 0) 
green = (0, 255, 0)
blue = (0, 0, 255)


font = pygame.font.SysFont(None, 40)

def messageToScreen1(message, color):
    text = font.render(message, True, color)
    gameDisplay.blit(text, (display_widht-480, display_height-400))
def messageToScreen2(message, color):
    text = font.render(message, True, color)
    gameDisplay.blit(text, (display_widht-600, display_height-300))
def punti(message, color):
    text = font.render(message, True, color)
    gameDisplay.blit(text, (display_widht-480, display_height-580))
def score(message, color):
    text = font.render(message, True, color)
    gameDisplay.blit(text, (display_widht-390, display_height-580))

go = 10.0
stop = 0

clock = pygame.time.Clock()


def gameLoop():
	main_x = display_widht/2
	main_y = display_height/2
	main_x_change = 0
	main_y_change = 0
        n = 0
	randEnemyX =round(random.randrange(10, display_widht-block_size)/block_size)*block_size #posizione random nemico
        randEnemyY =round(random.randrange(10, display_height-block_size)/block_size)*block_size

	gameExit = False
	gameOver = False

	while not gameExit:
	  while gameOver == True:

	    messageToScreen1("Game Over", white)
            messageToScreen2("premi R per ripetere o Q per chiudere", green)
	    pygame.display.update()

	    for event in pygame.event.get():
	        if event.key == pygame.K_r:
	        	gameLoop()
	        if event.key == pygame.K_q:
	        	gameOver = False
		        gameExit = True

  	  for event in pygame.event.get():
  	    if event.type == pygame.QUIT: #se X premuto allora chiudi finestra
	       gameExit = True

	    if event.type == pygame.KEYDOWN: #se l'evento e' di pressione di un tasto allora 
 
	       if event.key == pygame.K_LEFT: #se freccia sinistra premuta allora vai a sinistra 
	          main_x_change = -(go)
	          main_y_change = stop

	       elif event.key == pygame.K_RIGHT: #se freccia sinistra premuta allora vai a destra
	          main_x_change = go
	          main_y_change = stop

	       elif event.key == pygame.K_UP: #se freccia sinistra premuta allora vai sopra 
	          main_y_change = -(go)
	          main_x_change = stop

	       elif event.key == pygame.K_DOWN: #se freccia sinistra premuta allora vai sotto
	          main_y_change = go
	          main_x_change = stop

               elif event.key == pygame.K_a: #se freccia sinistra premuta allora vai sotto
                  main_y_change = stop
                  main_x_change = stop

          if main_x >= display_widht or main_x <=10 or main_y >= display_height or main_y <=10:
             gameOver = True

	  main_x += main_x_change
	  main_y += main_y_change


  	  gameDisplay.fill(red) #imposta lo sfondo rosso
          #disegno bordi e giocatore
          pygame.draw.rect(gameDisplay, white, (main_x, main_y, block_size, block_size)) #player
          pygame.draw.rect(gameDisplay, green, (0, 0, 10, 600))
          pygame.draw.rect(gameDisplay, green, (0, 590, 800, 10))
          pygame.draw.rect(gameDisplay, green, (790, 0, 10, 600))
          pygame.draw.rect(gameDisplay, green, (0, 0, 800, 10))
          pygame.draw.rect(gameDisplay, black, (randEnemyX, randEnemyY, block_size, block_size)) #nemico
          punti("Punti=", white)
          score(str(n), white)
          pygame.display.update() #ciclo for infinito che aggiorna la finestra 

          if main_x == randEnemyX and main_y == randEnemyY :
            randEnemyX = round(random.randrange(10, display_widht-block_size)/block_size)*block_size #posizione random nemico
            randEnemyY = round(random.randrange(10, display_height-block_size)/block_size)*block_size
            punti("Punti=", white) #aggiornamento punteggio
            n = n+10
          clock.tick(30)

	pygame.quit()
	quit()
    
gameLoop()
