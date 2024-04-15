import pygame


class Camera():
    def __init__(self):
        self.offset = pygame.math.Vector2(0, 0)
        self.speed = 4


pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("final_py_chamber")
background = pygame.image.load('./background.png')

# 캐릭터 세팅하기
character = pygame.image.load('./character_ch.png')
character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = SCREEN_WIDTH/2 - character_width/2
character_y_pos = SCREEN_HEIGHT/2 - character_height/2

# 화면의 아이콘 정하기
# widowicon = pygame.image.load("icon.png")
# pygame.display.set_icon(windowicon)

clock = pygame.time.Clock()
camera = Camera()

playing = True
while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    ## 캐릭터 움직이기
    to_x = 0
    to_y = 0
    character_speed = 5

    keys = pygame.key.get_pressed()


    if not SCREEN_WIDTH< character_x_pos < :
        print('밖으로 나감')
        to_x = 0
    else:
        if keys[pygame.K_UP]:
            to_y = -5
            camera.offset.x = -5
        elif keys[pygame.K_DOWN]:
            to_y = +5
            camera.offset.x = +5
        elif keys[pygame.K_LEFT]:
            to_x = -5
            camera.offset.y = -5
        elif keys[pygame.K_RIGHT]:
            to_x = +5
            camera.offset.y = +5


    character_x_pos += to_x
    character_y_pos += to_y

    # 화면에 표시하기
    SCREEN.blit(background, (0,0))  ## 배경
    SCREEN.blit(character, (character_x_pos, character_y_pos))  ## 캐릭터

    pygame.display.flip()
    clock.tick(60)

