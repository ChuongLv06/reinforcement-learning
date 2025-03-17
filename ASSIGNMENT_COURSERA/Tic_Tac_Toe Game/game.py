import pygame
import sys


# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ và bàn cờ
SIZE = 15  # Kích thước bàn cờ (15x15)
CELL_SIZE = 40  # Kích thước ô cờ
WIDTH, HEIGHT = SIZE * CELL_SIZE, SIZE * CELL_SIZE
LINE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caro Truyền Thống")
screen.fill(WHITE)

# Bàn cờ
board = [[None for _ in range(SIZE)] for _ in range(SIZE)]
current_player = "X"

def draw_board():
    for i in range(SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT))
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))

def check_winner():
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] is not None:
                # Kiểm tra hàng ngang
                if j + 4 < SIZE and all(board[i][j + k] == board[i][j] for k in range(5)):
                    return board[i][j]
                # Kiểm tra hàng dọc
                if i + 4 < SIZE and all(board[i + k][j] == board[i][j] for k in range(5)):
                    return board[i][j]
                # Kiểm tra chéo chính
                if i + 4 < SIZE and j + 4 < SIZE and all(board[i + k][j + k] == board[i][j] for k in range(5)):
                    return board[i][j]
                # Kiểm tra chéo phụ
                if i - 4 >= 0 and j + 4 < SIZE and all(board[i - k][j + k] == board[i][j] for k in range(5)):
                    return board[i][j]
    return None

def draw_x_o():
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == "X":
                pygame.draw.line(screen, RED, (j * CELL_SIZE + 10, i * CELL_SIZE + 10), 
                                 ((j + 1) * CELL_SIZE - 10, (i + 1) * CELL_SIZE - 10), 3)
                pygame.draw.line(screen, RED, ((j + 1) * CELL_SIZE - 10, i * CELL_SIZE + 10), 
                                 (j * CELL_SIZE + 10, (i + 1) * CELL_SIZE - 10), 3)
            elif board[i][j] == "O":
                pygame.draw.circle(screen, BLUE, (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5, 3)

def main():
    global current_player
    running = True
    winner = None
    while running:
        screen.fill(WHITE)
        draw_board()
        draw_x_o()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if board[row][col] is None:
                    board[row][col] = current_player
                    current_player = "O" if current_player == "X" else "X"
                    winner = check_winner()
        
        if winner:
            print(f"{winner} thắng!")
            pygame.time.delay(2000)
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
