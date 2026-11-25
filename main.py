import pygame

pygame.init()

WINDOW_SIZE = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Ananas in RTF")

background_image = pygame.image.load("assets/background.png")
background_image = pygame.transform.scale(background_image, WINDOW_SIZE)
screen.blit(background_image, (0, 0))
pygame.display.flip()

run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            key = e.key
            if key == pygame.K_UP or key == pygame.K_w:
                print(f"Нажата клавиша вверх: {pygame.key.name(key)}")
            if key == pygame.K_DOWN or key == pygame.K_s:
                print(f"Нажата клавиша вниз: {pygame.key.name(key)}")
            if key == pygame.K_LEFT or key == pygame.K_a:
                print(f"Нажата клавиша влево: {pygame.key.name(key)}")
            if key == pygame.K_RIGHT or key == pygame.K_d:
                print(f"Нажата клавиша вправо: {pygame.key.name(key)}")


        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = e.pos
            button = e.button

            print(f"Позиция мыши: {pos}")
            print(f"Идентификатор кнопки мыши: {button}")

pygame.quit()