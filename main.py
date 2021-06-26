import pygame
import sys
import random
isp=0
final_list=[0,0,0,0]
noizect=0
pygame.init()
pygame.mixer.init()
WIN=pygame.display.set_mode((750,750))
clock=pygame.time.Clock()
pygame.font.init()
pygame.mixer.init()
game_font=pygame.font.Font(None,40)
game_font1=pygame.font.Font(None,60)
level_ct=1
limit=10
high_score=0
#song
shoot=pygame.mixer.Sound("audio/Gun+Silencer.mp3")
hit=pygame.mixer.Sound("audio/Grenade+1.mp3")
ding=pygame.mixer.Sound("audio/loose.mp3")
loose=pygame.mixer.Sound("audio/mixkit-retro-arcade-lose-2027.wav")
bg_sound=pygame.mixer.Sound("audio/guitar-background-beat.mp3")
#load image
bg_surface=pygame.image.load("assets/background-black.png")
bg_surface=pygame.transform.scale(bg_surface,(750,750))
yellow_ship=pygame.image.load("assets/pixel_ship_yellow.png")
yellow_ship_rect=yellow_ship.get_rect(midbottom=(375,750))
yellow_ship_move=10
score_ct=0
life_ct=10
red_ship=pygame.image.load("assets/pixel_ship_red_small.png").convert()
red_ship_list=[]
SPAWNRED=pygame.USEREVENT+2
pygame.time.set_timer(SPAWNRED,3000)
blue_ship=pygame.image.load("assets/pixel_ship_blue_small.png").convert()
blue_ship_list=[]
SPAWNBLUE=pygame.USEREVENT+3
pygame.time.set_timer(SPAWNBLUE,2000)

yellow_ship=pygame.image.load("assets/pixel_ship_yellow.png")
yellow_ship_rect=yellow_ship.get_rect(midbottom=(375,750))
yellow_ship_move=10

yellow_bullet=[]
red_bullet=[]
MAX_BULLETS=3
def collision(yellow_bullet,red,blue):
    for i in yellow_bullet:
        if(red.colliderect(i)):
            yellow_bullet.remove(i)
            return (True)
        if (blue.colliderect(i)):
            yellow_bullet.remove(i)
            return (True)
    return(False)
def levdisp(level_ct):
    level = game_font.render(f'LEVEL:{int(level_ct)}', True, (255, 255, 255))
    level_rect = level.get_rect(center=(370, 100))
    WIN.blit(level, level_rect)
def scoredisp(score_ct):
    score=game_font.render(f'SCORE:{int(score_ct)}', True, (255, 255, 255))
    score_rect =score.get_rect(center=(100, 100))
    WIN.blit(score,score_rect)
def lifedisp(life_ct):
    life=game_font.render(f'LIVES:{int(life_ct)}', True, (255, 255, 255))
    life_rect =life.get_rect(center=(650, 100))
    WIN.blit(life,life_rect)
def create_red():
    random_red_pos = random.randint(10,740)
    red=red_ship.get_rect(midtop=(random_red_pos,0))
    return(red)
def move_red(red_list):
    for i in red_list:
        i.centery+=3
    return(red_list)
def draw_red(red_list):
    for i in red_list:
        WIN.blit(red_ship,i)
def create_blue():
    random_blue_pos = random.randint(10,740)
    blue=blue_ship.get_rect(midtop=(random_blue_pos,0))
    return(blue)
def move_blue(blue_list):
    for i in blue_list:
        i.centery+=3
    return(blue_list)
def draw_blue(blue_list):
    for i in blue_list:
        WIN.blit(blue_ship,i)
def handle_bullets(yellow_bullet):
    for i in yellow_bullet:
        i.y-=5
def  yellow_bullet_movement(yellow_bullet):
    for i in yellow_bullet:
        if(i.y<=0):
            yellow_bullet.remove(i)
        pygame.draw.rect(WIN,(255,255,0),i)
def game_over(keys_pressed,isp,life_ct,yellow_ship_rect,score_ct,level_ct,final_list,high_score):
    isp=1
    if(score_ct>high_score):
        high_score=score_ct
    red_ship_list.clear()
    blue_ship_list.clear()
    WIN.blit(bg_surface, (0, 0))
    levdisp(level_ct)
    scoredisp(score_ct)
    lifedisp(life_ct)
    gover=game_font1.render(f'GAME OVER', True, (255,0,0))
    gover_rect=gover.get_rect(center=(370,300))
    WIN.blit(gover,gover_rect)
    ss = game_font.render(f'SCORE:{score_ct}', True, (255,255, 0))
    ss_rect = ss.get_rect(center=(370, 250))
    WIN.blit(ss, ss_rect)
    hs = game_font.render(f'HIGH SCORE:{high_score}', True, (128,0,128))
    hs_rect = hs.get_rect(center=(370, 220))
    WIN.blit(hs, hs_rect)
    restart = game_font.render(f'TO  PLAY  AGAIN  PRESS  RETURN', True, (255, 255, 255))
    restart_rect = restart.get_rect(center=(370, 350))
    WIN.blit(restart,restart_rect)
    restart1 = game_font.render(f'TO QUIT PRESS ESCAPE', True, (255, 255, 255))
    restart_rect1 = restart.get_rect(center=(420,400))
    WIN.blit(restart1, restart_rect1)
    if(keys_pressed[pygame.K_RETURN]):
        bg_sound.play()
        isp=0
        yellow_ship_rect=yellow_ship.get_rect(midbottom=(375,750))
        final_list=[10,0,1,high_score]
        return (final_list)
    if (keys_pressed[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    pygame.display.update()
    return([life_ct,score_ct,level_ct,high_score])

def yellow_ship_movement(keys_pressed):
    if(keys_pressed[pygame.K_RIGHT] and yellow_ship_rect.right<=750):
        yellow_ship_rect.centerx+=yellow_ship_move
    if (keys_pressed[pygame.K_LEFT] and yellow_ship_rect.left>=0):
        yellow_ship_rect.centerx-=yellow_ship_move
    if (keys_pressed[pygame.K_UP] and yellow_ship_rect.top>=0):
        yellow_ship_rect.centery-= yellow_ship_move
    if (keys_pressed[pygame.K_DOWN] and yellow_ship_rect.bottom <=750):
        yellow_ship_rect.centery+= yellow_ship_move
bg_sound.play()
while(True):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if(event.key==pygame.K_SPACE and isp==0 ):
                shoot.play()
                bullet=pygame.Rect(yellow_ship_rect.centerx,yellow_ship_rect.centery,5,20)
                yellow_bullet.append(bullet)
        if (event.type == SPAWNRED and isp==0):
            red_ship_list.append(create_red())
        if (event.type == SPAWNBLUE and isp==0):
            blue_ship_list.append(create_blue())
    if (life_ct<=0):
        if(noizect==0):
            ding.stop()
            bg_sound.stop()
            loose.play()
            noizect=1
        isp=1
        keys_pressed = pygame.key.get_pressed()
        final_list=game_over(keys_pressed,isp,life_ct,yellow_ship_rect,score_ct,level_ct,final_list,high_score)
        life_ct=final_list[0]
        score_ct=final_list[1]
        level_ct=final_list[2]
        high_score=final_list[3]
        if(life_ct>0):
            isp=0
            noizect=0
    if(isp==0):
        for i in red_ship_list:
            if(collision(yellow_bullet,i,i)==True):
                hit.play()
                red_ship_list.remove(i)
                score_ct+=1
            elif (yellow_ship_rect.colliderect(i)):
                ding.play()
                red_ship_list.remove(i)
                life_ct -= 1
            if(i.bottom>=750):
                ding.play()
                red_ship_list.remove(i)
                life_ct-=1
        for i in blue_ship_list:
            if(collision(yellow_bullet,i,i)==True):
                 hit.play()
                 blue_ship_list.remove(i)
                 score_ct+=1
            elif (yellow_ship_rect.colliderect(i)):
                ding.play()
                blue_ship_list.remove(i)
                life_ct -= 1
            if (i.bottom >= 750):
                ding.play()
                blue_ship_list.remove(i)
                life_ct -= 1
        keys_pressed = pygame.key.get_pressed()
        WIN.blit(bg_surface,(0,0))
        WIN.blit(yellow_ship,yellow_ship_rect)
        if(score_ct>limit):
            limit+=10
            level_ct+=1
        levdisp(level_ct)
        scoredisp(score_ct)
        lifedisp(life_ct)
        yellow_ship_movement(keys_pressed)
        handle_bullets(yellow_bullet)
        yellow_bullet_movement(yellow_bullet)
        blue_ship_list = move_blue(blue_ship_list)
        draw_blue(blue_ship_list)
        red_ship_list=move_red(red_ship_list)
        draw_red(red_ship_list)
        pygame.display.update()
        clock.tick(120)
