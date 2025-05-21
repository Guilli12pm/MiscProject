import pygame
import random, math
import sys

WIDTH, HEIGHT = 500,500
MARGIN = 50
BOX_SIZE = WIDTH-2*MARGIN
BACKGROUND = (0,0,0)
FRAME_COLOR = (255,255,255)
INSIDE_COLOR = (0,0,255)
OUTSIDE_COLOR = (255,0,0)
CIRCLE_COLOR = (255,255,0)
TEXT_COLOR = (255,255,255)
POINT_RADIUS = 2
FPS = 500

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Monte Carlo PI Approximation")
clock = pygame.time.Clock()
font  = pygame.font.SysFont(None, 28)

bx, by = MARGIN, MARGIN
screen.fill(BACKGROUND)
pygame.draw.rect(screen,FRAME_COLOR,(bx,by,BOX_SIZE,BOX_SIZE),width=4)

####
#### Draw Quarter Circle
####
cx = bx
cy = by + BOX_SIZE
arc = []
for i in range(3):
    theta = (math.pi/2) * i/100
    x = cx + BOX_SIZE * math.cos(theta)
    y = cy - BOX_SIZE * math.sin(theta)
    arc.append((int(x),int(y)))
pygame.draw.lines(screen,CIRCLE_COLOR,False,arc,3)

pygame.display.flip()

inside_count = 0
total_count  = 0

run = True
while run:
    clock.tick(FPS)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    x = random.random()
    y = random.random()
    total_count += 1
    if math.sqrt(x**2 + y**2) <= 1:
        inside_count += 1
        color = INSIDE_COLOR
    else:
        color = OUTSIDE_COLOR

    px = bx + int(x * BOX_SIZE)
    py = by + BOX_SIZE - int(y * BOX_SIZE)

    pygame.draw.circle(screen, color, (px, py), POINT_RADIUS)

    pi_est = 4*inside_count/total_count
    txt_surf = font.render(f"Points: {total_count}   approx PI = {pi_est:.5f}",True, TEXT_COLOR, BACKGROUND)
    screen.fill(BACKGROUND,(0,0,WIDTH,30))
    screen.blit(txt_surf,(10,2))

    pygame.display.flip()

pygame.quit()
sys.exit()
