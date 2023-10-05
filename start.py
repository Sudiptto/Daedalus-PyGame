import sys, pygame
pygame.init()

size = width, height = 720, 540
speed = [1,0] # cant do decimals
#black = 0, 0, 0

white = 255,255,255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()