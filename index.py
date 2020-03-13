import pygame

pygame.init()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('My First Game')

clock = pygame.time.Clock()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False

	#Game logic

	#Drawing
	screen.fill((255,255,255))

	#Update Screen
	pygame.display.flip()

	clock.tick(60)


pygame.quit()