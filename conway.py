import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def initialize_grid():
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.9, 0.1])

def draw_grid(surface, grid):
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x, y] == 1:
                pygame.draw.rect(surface, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(surface, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def update_grid(grid):
    new_grid = grid.copy()
    for x in range(1, GRID_WIDTH - 1):
        for y in range(1, GRID_HEIGHT - 1):
            neighbors = grid[x - 1:x + 2, y - 1:y + 2].sum() - grid[x, y]
            if grid[x, y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    clock = pygame.time.Clock()
    running = True
    paused = False
    grid = initialize_grid()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN and paused:
                x, y = pygame.mouse.get_pos()
                x //= CELL_SIZE
                y //= CELL_SIZE
                if event.button == 1:  # Left click to set cells to "on"
                    grid[x, y] = 1
                elif event.button == 3:  # Right click to set cells to "off"
                    grid[x, y] = 0
                screen.fill(BLACK)  # Update the screen immediately
                draw_grid(screen, grid)
                pygame.display.flip()

        if not paused:
            screen.fill(BLACK)
            draw_grid(screen, grid)
            grid = update_grid(grid)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
