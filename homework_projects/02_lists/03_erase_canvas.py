import pygame

WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
ERASER_SIZE = 40
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Erase Canvas")

cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE
grid = [[BLUE for _ in range(rows)] for _ in range(cols)]


def draw_grid():
    for x in range(cols):
        for y in range(rows):
            pygame.draw.rect(
                screen, grid[x][y], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


running = True
eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
erasing = False

while running:
    screen.fill(WHITE)
    draw_grid()
    pygame.draw.rect(screen, WHITE, eraser_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                erasing = False

    if erasing:
        eraser_rect.center = pygame.mouse.get_pos()
        for x in range(cols):
            for y in range(rows):
                cell_rect = pygame.Rect(
                    x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if eraser_rect.colliderect(cell_rect):
                    grid[x][y] = WHITE

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
