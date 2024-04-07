import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("final_py_chamber")

# 화면의 아이콘 정하기
# widowicon = pygame.image.load("icon.png")
#
# pygame.display.set_icon(windowicon)
clock = pygame.time.Clock()

playing = True
while playing:
    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # 키가 눌렸을 때

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("왼쪽 키 눌림")
            if event.key == pygame.K_RIGHT:
                print("오른쪽 키 눌림")

            if event.key == pygame.K_UP:
                print("위로 키 눌림")
            if event.key == pygame.K_DOWN:
                print("아래로 키 눌림")

        # 키가 떼졌을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("왼쪽 키 떼짐")
            if event.key == pygame.K_RIGHT:
                print("오른쪽 키 떼짐")

            if event.key == pygame.K_UP:
                print("위로 키 떼짐")
            if event.key == pygame.K_DOWN:
                print("아래로 키 떼짐")

        # 눌린 동안 처리 (계속)
        if keys[pygame.K_SPACE]:
            print("스페이스 키 눌림")
