# I'm Yang. It's my first 2D game based on pygame.
"""
@author: Yang Zhou
"""

from Role import *

pygame.init()

# set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

filename = 'image/shoot.png'
plane_img = pygame.image.load(filename)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


player = Player()

background = pygame.image.load('background.bmp').convert()
game_over = pygame.image.load('gameover.bmp')

# load music

pygame.mixer.music.load('sound/game_music.wav')
game_over_sound = pygame.mixer.Sound('sound/game_over.wav')
game_over_sound.set_volume(0.3)
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
# make sprite group
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# score at first
score = 0
# keep run
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
# detect events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
# fill screen backgroound
    screen.fill(0)
    screen.blit(background, (0, 0))
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(int(score)), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    score += 1/60
    screen.blit(score_text, text_rect)
# once collide happened
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        player.is_hit = True
        break

# if not keep going and draw all things
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    pygame.display.update()
#record the score
font = pygame.font.Font(None, 48)
text = font.render('Score: ' + str(int(score)), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
game_over_sound.play()
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

