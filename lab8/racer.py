import pygame
from pygame.locals import *
import random


pygame.init()

# Window settings
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Racer')

# Colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# Road and marker sizes
road_width = 300
marker_width = 10
marker_height = 50

# Lane coordinates
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# Road and edge markers
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (395, 0, marker_width, height)

# For animating movement of the lane markers
lane_marker_move_y = 0

# Player's starting coordinates
player_x = 250
player_y = 400

# Frame settings
clock = pygame.time.Clock()
fps = 100

# Game settings
gameover = False
speed = 1
score = 0

# Class for the player's vehicle
class PlayerVehicle(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/car.png')
        self.image = pygame.transform.scale(image, (45, 90))  # Scale image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Class for vehicles on the road
class Vehicle(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (int(new_width), int(new_height)))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Class for coins
class Coin(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('images/coin.png')
        self.image = pygame.transform.scale(image, (30, 30))  # Scale image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Sprite groups
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# Create the player's car
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# Load the vehicle images
vehicle_images = [pygame.image.load('images/' + image_filename) for image_filename in ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']]

# Load the crash image
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()

# Load the coin image
coin_image = pygame.image.load('images/coin.png')

# Game loop
running = True
while running:
    
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        # Move the player's car using the left/right arrow keys
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
                
            # Check for collisions with vehicles
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True
                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
            
    # Draw the grass
    screen.fill(green)
    
    # Draw the road
    pygame.draw.rect(screen, gray, road)
    
    # Draw the edge markers
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)
    
    # Draw the lane markers
    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        
    # Draw the player's car
    player_group.draw(screen)
    
    # Add a vehicle
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
                
        if add_vehicle:
            lane = random.choice(lanes)
            image = random.choice(vehicle_images)
            vehicle = Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)
    
    # Add coins randomly
    if len(coin_group) < 5:
        if random.random() < 0.01:  # Adjust the probability to control coin generation rate
            lane = random.choice(lanes)
            coin = Coin(lane, height / -2)
            coin_group.add(coin)
    
    # Move the vehicles
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        if vehicle.rect.top >= height:
            vehicle.kill()
            if score > 0 and score % 5 == 0:
                speed += 0.1
    
    # Draw the vehicles
    vehicle_group.draw(screen)
    
    # Move the coins
    for coin in coin_group:
        coin.rect.y += speed
        if coin.rect.top >= height:
            coin.kill()
        if pygame.sprite.collide_rect(player, coin):
            coin.kill()
            score += 10
    
    # Draw the coins
    coin_group.draw(screen)
    
    # Display the score
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    screen.blit(text, text_rect)
    
    # Check for collisions with vehicles
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
            
    # Display game over
    if gameover:
        screen.blit(crash, crash_rect)
        pygame.draw.rect(screen, red, (0, 50, width, 100))
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Game over. Play again? (Enter Y or N)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)
            
    pygame.display.update()

    # Wait for user's input to play again or exit
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # Reset the game
                    gameover = False
                    speed = 1
                    score = 0
                    vehicle_group.empty()
                    coin_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    # Exit the game
                    gameover = False
                    running = False

pygame.quit()
