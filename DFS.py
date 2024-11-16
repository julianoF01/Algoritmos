import pygame
import time

# Configurações do grid
GRID_SIZE = 4  # Tamanho do grid (4x4)
CELL_SIZE = 50  # Tamanho de cada célula em pixels
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Grid predefinido com 1 e 0
grid_values = [
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 0, 1]
]

# Posição inicial da bolinha
ball_pos = [0, 0]  # [linha, coluna]

# Inicializa o Pygame
pygame.init()

# Cria a janela
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Movimento da Bolinha")

# Função para desenhar o grid
def draw_grid():
    for i in range(GRID_SIZE + 1):
        # Linhas horizontais
        pygame.draw.line(screen, (0, 0, 0), (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE))
        # Linhas verticais
        pygame.draw.line(screen, (0, 0, 0), (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE))

# Função para desenhar as células de acordo com o valor (1 ou 0)
def draw_cells():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            if grid_values[row][col] == 1:
                pygame.draw.rect(screen, (139, 69, 19), (x, y, CELL_SIZE, CELL_SIZE))  # Cor marrom
            else:
                pygame.draw.rect(screen, (0, 0, 255), (x, y, CELL_SIZE, CELL_SIZE))  # Cor azul

# Função para desenhar a bolinha
def draw_ball():
    x = ball_pos[1] * CELL_SIZE + CELL_SIZE // 2
    y = ball_pos[0] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)  # Cor verde


def find_path(grid, n, x, y):
    
    global ball_pos
    
    if x >= n or y >= n:
        return False

    ball_pos = [x, y]
    draw_screen()

    time.sleep(1)  # Aguarda meio segundo para ver o movimento

    if grid[x][y] == 0:
        return False

    if x == n - 1 and y == n - 1:
        return True

    # Move para baixo
    if find_path(grid, n, x + 1, y):  
        return True
    
    ball_pos = [x, y]
    draw_screen()
    time.sleep(1)  # Aguarda meio segundo para ver o movimento    
    
    # Move para direita
    if find_path(grid, n, x, y + 1):  
        return True
    
    ball_pos = [x, y]
    draw_screen()
    time.sleep(1)  # Aguarda meio segundo para ver o movimento

    return False

def draw_x():
    x = (GRID_SIZE - 1) * CELL_SIZE + CELL_SIZE // 2
    y = (GRID_SIZE - 1) * CELL_SIZE + CELL_SIZE // 2
    font = pygame.font.Font(None, 36)
    text = font.render("X", True, (255, 0, 0))  # Cor vermelha
    screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))  # Centraliza o "X"

# Função para atualizar a tela
def draw_screen():
    screen.fill((255, 255, 255))  # Limpa a tela (branco)
    draw_grid()
    draw_cells()
    draw_x()
    draw_ball()
    pygame.display.flip()  # Atualiza a tela

# Inicia o processo de busca
find_path(grid_values, GRID_SIZE, ball_pos[0], ball_pos[1])

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
