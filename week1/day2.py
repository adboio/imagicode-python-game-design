import pygame

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Imagicode Clicker")
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
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.clicks = 0
        self.is_small = True
        self.is_big = False
    
    def go_big(self):
        self.image = pygame.Surface((60, 60))
        self.image.fill(GREEN)
        self.is_small = False
        self.is_big = True

    def go_small(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.is_big = False
        self.is_small = True

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
                    if s.is_small:
                        s.go_big()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for s in clicker_sprites:
                clicks += 1
                if s.is_big:
                    s.go_small()

    screen.fill(BLACK)
    clicker_sprites.draw(screen)
    draw_text(screen, "Score: " + str(clicks), 24, WIDTH / 2, HEIGHT - 30)
    pygame.display.flip()

pygame.quit()

