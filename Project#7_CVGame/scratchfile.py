import numpy as np
import pygame, sys
import cv2 as cv
import time    
import threading
from cvzone.HandTrackingModule import HandDetector

# Initialize Camera
cap = cv.VideoCapture(0)
shapex = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))  
shapey = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) 
hand_y = shapey // 2  # Default hand position
frame = np.zeros((shapey, shapex, 3), dtype=np.uint8)  # Initialize blank frame
lock = threading.Lock()  # Prevent race conditions

def process_video():
    """Handles video capturing and hand tracking in a separate thread."""
    global hand_y, frame
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    while True:
        success, img = cap.read()
        if not success:
            continue  # Skip if frame is not available
        
        img = cv.flip(img, 1)  # Flip to match player movement
        hands, _ = detector.findHands(img, True)  # Detect hands

        if hands:
            landmark = hands[0]['lmList']
            hand_y = int(landmark[9][1])  # Get Y-coordinate of wrist
        else:
            hand_y = shapey // 2  # Default position if no hand detected

        with lock:
            frame = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Store latest frame

# Start video processing thread
video_thread = threading.Thread(target=process_video, daemon=True)
video_thread.start()

# Initialize Pygame
pygame.init()
H, W = shapey, shapex
screen = pygame.Surface((W, H))  # Hidden surface for drawing the game
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Game Objects
ball = pygame.Rect(W / 2 - 15, H / 2 - 15, 30, 30)
player1 = pygame.Rect(20, H / 2 - 35, 10, 70)  # Left paddle
player2 = pygame.Rect(W - 30, H / 2 - 35, 10, 70)  # Right paddle
light_grey = (200, 200, 200)
ball_speed_x, ball_speed_y = 5, 5
opponent_speed = 7
score = 0
score_colour = (0, 255, 0)
font = pygame.font.SysFont("Arial", 30)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv.destroyAllWindows()
            pygame.quit()
            sys.exit()

    # Update player1 position based on hand tracking
    player1.y = hand_y - player1.height // 2  # Center paddle to hand

    # Keep player within bounds
    player1.y = max(0, min(H - player1.height, player1.y))

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # AI Opponent Movement
    if player2.bottom < ball.bottom:
        player2.y += opponent_speed
    elif player2.top > ball.top:
        player2.y -= opponent_speed

    # Ball Collisions
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
    if ball.top <= 0 or ball.bottom >= H:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= W:
        ball_speed_x *= -1

    # Draw Game Elements on Pygame Surface
    screen.fill((0, 0, 0, 0))  # Transparent background
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.aaline(screen, light_grey, (W / 2, 0), (W / 2, H))

    # Display Score
    text = font.render(f'Score {score}', True, score_colour)
    screen.blit(text, (W - 150, 10))

    # Convert Pygame Surface to OpenCV Format
    game_surface = pygame.surfarray.array3d(screen)  # Convert Pygame to NumPy array
    game_surface = np.rot90(game_surface)  # Rotate for OpenCV format
    

    # Fetch Latest Camera Frame
    with lock:
        frame_copy = frame.copy()

    # Blend Game with Camera Feed
    alpha = 0.5  # Transparency level
    frame=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
    overlay = cv.addWeighted(frame_copy, 1 - alpha, game_surface, alpha, 0)

    # Show Final Output
    cv.imshow("Pong with Camera Feed", overlay)

    if cv.waitKey(1) & 0xFF == 27:
        break

    clock.tick(60)  # Maintain 60 FPS

# Cleanup
cap.release()
cv.destroyAllWindows()
pygame.quit()
sys.exit()
