
import sys
import pygame
import chess_Pieces

def load_images():
    pieces_images = {}
    
    pieces_images['white_pawn'] = pygame.image.load('pieces/white_pawn.png')
    pieces_images['white_rook'] = pygame.image.load('pieces/white_rook.png')
    pieces_images['white_queen'] = pygame.image.load('pieces/white_queen.png')
    pieces_images['white_king'] = pygame.image.load('pieces/white_king.png')
    pieces_images['white_knight'] = pygame.image.load('pieces/white_knight.png')
    pieces_images['white_bishop'] = pygame.image.load('pieces/white_bishop.png')
    
    pieces_images['black_pawn'] = pygame.image.load('pieces/black_pawn.png')
    pieces_images['black_rook'] = pygame.image.load('pieces/black_rook.png')
    pieces_images['black_queen'] = pygame.image.load('pieces/black_queen.png')
    pieces_images['black_king'] = pygame.image.load('pieces/black_king.png')
    pieces_images['black_knight'] = pygame.image.load('pieces/black_knight.png')
    pieces_images['black_bishop'] = pygame.image.load('pieces/black_bishop.png')
    
    return pieces_images


def main():
    # print('Hello World!')
    pygame.init()

    # Windows size
    screen = pygame.display.set_mode((800, 800))
    # whites
    white_pawns = {}
    white_rooks = {}
    white_knights = {}     
    white_bishops = {}
    
    
    # blacks
    black_pawns = {}
    black_rooks = {}
    black_knights = {}
    black_bishops = {}
    # images
    
    images = load_images()
    
    # SET POSITIONS ON THE BOARD
    # Pieces
    for x in range(2):
        white_rooks['white_rook_' + str(x+1)] = chess_Pieces.Piece('Rook', 1, 'white', images.get('white_rook'))
        white_knights['white_knight_' + str(x+1)] = chess_Pieces.Piece('Knight', 1, 'white', images.get('white_knight'))
        white_bishops['white_bishops_' + str(x+1)] = chess_Pieces.Piece('Bishop', 1, 'white', images.get('white_bishop'))
        
        black_rooks['black_rook_'+ str(x+1)] = chess_Pieces.Piece('Rook', 1, 'black', images.get('black_rook'))
        black_knights['black_knight_' + str(x+1)] = chess_Pieces.Piece('Knight', 1, 'black', images.get('black_knight'))
        black_bishops['black_bishop_' + str(x+1)] = chess_Pieces.Piece('Bishop', 1, 'black', images.get('black_bishop'))
    
    # Pawns
    for x in range(8):
        white_pawns['white_pawn_' + str(x+1)] = chess_Pieces.Piece('Pawn', 1, 'white', images.get('white_pawn'))
        black_pawns['black_pawn_' + str(x+1)] = chess_Pieces.Piece('Pawn', 1, 'black', images.get('black_pawn'))
    
    # One off's
    black_king = chess_Pieces.Piece('King', 1, 'black', images.get('black_king'))
    black_queen = chess_Pieces.Piece('Queen', 1, 'black', images.get('black_queen'))
    white_king = chess_Pieces.Piece('King', 1, 'white', images.get('white_king'))
    white_queen = chess_Pieces.Piece('Queen', 1, 'white', images.get('white_queen'))
    

    
        
    # print(black_pawns.get('black_pawn_8').color)
    
    # print(black_king.health)
    # black_king.health = 0
    # print(black_king.health)
    

    # Draw the chess board
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (128, 128, 128)
            pygame.draw.rect(screen, color, (col * 100, row * 100, 100, 100))

    
    # square + 20
    numb = 0
    # Initial positions
    # Pawns
    for x in range(8):
        screen.blit(white_pawns.get('white_pawn_' + str(x+1)).image, (20 + numb, 620))
        screen.blit(black_pawns.get('black_pawn_' + str(x+1)).image, (20 + numb, 120))
        numb += 100
    
    
    # Update the screen
    pygame.display.flip()

    # Wait for the user to close the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        


if __name__ == '__main__':
    main()