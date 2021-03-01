import pygame
import os, sys
from random import randrange


def load_image(name, colorkey=None):
    fullname = os.path.join('проект/data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image("bomb.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(500 - self.rect[2])
        self.rect.y = randrange(500 - self.rect[3])
        while True:
            self.rect.x = randrange(500 - self.rect[2])
            self.rect.y = randrange(500 - self.rect[3])
            if len(pygame.sprite.spritecollide(self, all_sprites, False)) == 1:
                break

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.image = load_image("boom.png")


class Sprite_Mouse_Location(pygame.sprite.Sprite):
    def __init__(self,x,y):
        Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)
        print(self.rect)


def main():
    pygame.display.set_caption("Boom them all")
    screen = pygame.display.set_mode([500, 500])

    for _ in range(20):
        Bomb(all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event.pos)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
pygame.quit()