import pygame 
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle settings
initial_paddle_width = 150
paddle_height = 25
paddle_speed = 20
paddle = pygame.Rect(W // 2 - initial_paddle_width // 2, H - paddle_height - 30, initial_paddle_width, paddle_height)

# Ball settings
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('music/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = []
color_list = []

for i in range(10):
    for j in range(4):
        # Generating regular blocks
        if random.random() < 0.8:  # 80% chance of generating a regular block
            block_list.append(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50))
            color_list.append((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        else:  # 20% chance of generating an unbreakable block
            block_list.append(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50))
            color_list.append((99, 141, 187))  # Blue color for unbreakable blocks

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Ball acceleration
ball_acceleration = 0.002

# Paddle shrink rate
paddle_shrink_rate = 0.01  

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]  # drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ball_radius)

    # Increase ball speed over time
    ball_speed += ball_acceleration
    
    # Shrink the paddle over time
    if paddle.width > 20:  
        paddle.width -= paddle_shrink_rate

    # Ball movement
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # Collision left
    if ball.centerx < ball_radius or ball.centerx > W - ball_radius:
        dx = -dx
    # Collision top
    if ball.centery < ball_radius + 50:
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        if hitColor != (100, 100, 100):  # Check if it's a regular block
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(FPS)