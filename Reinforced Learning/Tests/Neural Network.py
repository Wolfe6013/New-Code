import pygame

# Initialize Pygame
pygame.init()

# Set display dimensions
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set title
pygame.display.set_caption("Chess Game")

# Define board dimensions
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define board
board = [    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]

# Define function to draw board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != '.':
                # Draw piece on board
                pygame.draw.circle(screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 30)
                pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 28)

# Define function to update display
def update_display():
    draw_board()
    pygame.display.update()

# Run game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    update_display()

# Define function to move piece
def move_piece(row1, col1, row2, col2):
    piece = board[row1][col1]
    board[row1][col1] = '.'
    board[row2][col2] = piece

# Define function to check if move is valid
def is_valid_move(row1, col1, row2, col2):
    piece = board[row1][col1]
    if piece == '.':
        return False
    if piece == 'P':
        # Check if pawn is moving forward
        if col1 == col2 and row2 == row1 - 1 and board[row2][col2] == '.':
            return True
        # Check if pawn is capturing diagonally
        if abs(col2 - col1) == 1 and row2 == row1 - 1 and board[row2][col2].islower():
            return True
    # TODO: Implement rules for other pieces
    return False

# Define function to get user input
def get_user_input():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = event.pos[1] // SQUARE_SIZE, event.pos[0] // SQUARE_SIZE
                return row, col

# Run game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get user input
            row1, col1 = get_user_input()
            row2, col2 = get_user_input()
            # Check if move is valid
            if is_valid_move(row1, col1, row2, col2):
                move_piece(row1, col1, row2, col2)
    update_display()

