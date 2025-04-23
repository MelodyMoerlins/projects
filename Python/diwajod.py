import pygame, sys, random,time

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Pong")

font = pygame.font.Font('freesansbold.ttf',32)
start = time.time()
width = 1280
height = 960
you = 4
other = 4
wins = "test"

def movement():
    global ball_speed_x, ball_speed_y,you,other
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= width:
        if ball.left <= 0:
            you += 1
        elif ball.right >= width:
            other += 1
        if you == 5 or other == 5:
            if you == 5:
                winner("player 2")
            else:
                winner("player 1")
        else:
            ball_restart()
    
    if ball.colliderect(player) or ball.colliderect(opp):
        ball_speed_x *= -1

def playeranimation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def playeranimation2():
    opp.y += opp_speed
    if opp.top <= 0:
        opp.top = 0
    if opp.bottom >= height:
        opp.bottom = height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (width/2,height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

def winner(wins):
    global ball_speed_x, ball_speed_y
    ball.center = (width/2,height/2)
    ball_speed_x = 0
    ball_speed_y = 0
    txt = f"{wins} wins!"
    winnertext = font.render(txt, True, (255,255,255), (0,0,0))
    winnerRect = winnertext.get_rect()
    winnerRect.center = (width/2,height/2)
    screen.blit(winnertext, winnerRect)


screen = pygame.display.set_mode((width, height))

ball = pygame.Rect(width/2 - 15, height/2-15,30,30)

player = pygame.Rect(width-20, height/2-70, 10, 270)
opp = pygame.Rect(10, height/2-70, 10, 270)
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opp_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opp_speed += 7
            if event.key == pygame.K_w:
                opp_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opp_speed -= 7
            if event.key == pygame.K_w:
                opp_speed += 7

        
    playeranimation()
    playeranimation2()
    movement()
    timer = time.time()-start
    timer = str(f"{timer: .0f}")
    text = font.render(timer, True,(255,255,255),bg_color)
    textRect = text.get_rect()
    textRect.center = (width/2 - 5, 30)

    otherprint = font.render(str(other), True, (255,255,255), bg_color)
    otherRect = otherprint.get_rect()
    otherRect.center = (30,30)

    youprint = font.render(str(you), True, (255,255,255), bg_color)
    youRect = youprint.get_rect()
    youRect.center = (width-30,30)

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opp)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2,0), (width/2,height))
    screen.blit(text, textRect)
    screen.blit(youprint, youRect)
    screen.blit(otherprint, otherRect)

    pygame.display.flip()
    clock.tick(60)
