import pygame
import random
pygame.init()

window = pygame.display.set_mode((300, 350))  # 300, 350
pygame.display.set_caption('Fappy Bird')
pygame.display.set_icon(pygame.image.load('Gallery/flappy bird/bird.png'))

bg = pygame.image.load('Gallery/flappy bird/background.png')
bird = pygame.image.load('Gallery/flappy bird/bird.png')
birdUP = pygame.transform.rotate(bird, 30)
birdDOWN1 = pygame.transform.rotate(bird, -20)
pipeUP = pygame.image.load('Gallery/flappy bird/pipe.png')
pipeDOWN = pygame.transform.rotate(pipeUP, 180)
pipeUP_2 = pygame.image.load('Gallery/flappy bird/pipe.png')
pipeDOWN_2 = pygame.transform.rotate(pipeUP, 180)
over = pygame.transform.smoothscale(pygame.image.load('Gallery/flappy bird/message.png'), (300, 350))

x = 50
y = 220
acc = 1
vel = 5

power = 5
time = 4

jump = True
space = False

UPpipex = 300
UPpipey = -100
DOWNpipex = 300
DOWNpipey = 250

UPpipex_2 = 470
UPpipey_2 = -100
DOWNpipex_2 = 470
DOWNpipey_2 = 250

pipe_vel = 5

hit = False

player_score = 0


def display():
    if not hit:
        window.blit(bg, (0, -80))
        if not space and acc <= 7:
            window.blit(bird, (x, y))
        elif not space and acc > 7:
            window.blit(birdDOWN1, (x, y))
        if jump and space:
            window.blit(birdUP, (x, y))

        window.blit(pipeUP, (UPpipex, UPpipey))
        window.blit(pipeDOWN, (DOWNpipex, DOWNpipey))
        window.blit(pipeUP_2, (UPpipex_2, UPpipey_2))
        window.blit(pipeDOWN_2, (DOWNpipex_2, DOWNpipey_2))
        window.blit(pygame.font.SysFont('comicsans', 30, True).render('Your Score : ' + str(player_score), 1,
                                                                      (0, 0, 0)), (20, 20))
        pygame.display.update()
    if hit:
        window.blit(over, (0, 0))
        pygame.draw.rect(window, (0, 0, 0), (20, 10, 250, 40))
        window.blit(pygame.font.SysFont('comicsans', 30, True).render('Your Final Score : ' + str(player_score), 1,
                                                                      (0, 225, 0)), (22, 20))
        pygame.display.update()
        while True:
            for hit_event in pygame.event.get():
                if hit_event.type == pygame.QUIT:
                    exit()
                    break


while True:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            break
    if jump:
        if pygame.key.get_pressed()[pygame.K_SPACE] and y < 400:  # 340
            space = True
            acc = 1

    if jump and space and y > 5:
        y -= power * time
        time -= 1
        if time <= 0:
            jump = True
            space = False
            time = 4
        else:
            jump = True

    if not space and y < 340:
        y += (vel + acc)
        acc += 1

    UPpipex -= pipe_vel
    UPpipex_2 -= pipe_vel
    DOWNpipex -= pipe_vel
    DOWNpipex_2 -= pipe_vel

    if UPpipex < -pipeUP.get_width():
        UPpipex = 300
        UPpipey = random.randint(-150, 00)
        DOWNpipex = 300
        DOWNpipey = UPpipey + 100 + pipeUP.get_height()

    if UPpipex_2 < -pipeUP_2.get_width():
        UPpipex_2 = 300
        UPpipey_2 = random.randint(-150, 0)
        DOWNpipex_2 = 300
        DOWNpipey_2 = UPpipey_2 + 100 + pipeUP_2.get_height()

    if UPpipex < x + bird.get_width() / 2 < UPpipex + pipeUP.get_width():
        if UPpipey + pipeUP.get_height() < y + bird.get_height() / 2 < DOWNpipey:
            hit = False
        else:
            hit = True
    if UPpipex_2 < x + bird.get_width() / 2 < UPpipex_2 + pipeUP_2.get_width():
        if UPpipey_2 + pipeUP.get_height() < y + bird.get_height() / 2 < DOWNpipey_2:
            hit = False
        else:
            hit = True
    if not hit and x == UPpipex:
        player_score += 1
    if not hit and x == UPpipex_2:
        player_score += 1
    if hit:
        print('hit')

    display()
