import pygame

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Clicker Game")
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')
clicks = 0


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Clicker(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.clicks = 0


clicker_sprites = pygame.sprite.Group()
clicker1 = Clicker(WIDTH / 2, HEIGHT / 2)
clicker_sprites.add(clicker1)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for s in clicker_sprites:
                if s.rect.collidepoint(pos):
                    clicks += 1

    screen.fill(BLACK)
    clicker_sprites.draw(screen)
    draw_text(screen, "Score: " + str(clicks), 24, WIDTH / 2, HEIGHT - 30)
    pygame.display.flip()

pygame.quit()

