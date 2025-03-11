import pygame
import random
import math
import time

# Initialize Pygame
pygame.init()

# Game screen dimensions
WIDTH, HEIGHT = 1900,1100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zombies.io')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Font for game over screen
font = pygame.font.SysFont("Arial", 36)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.health = 100
        self.last_shot_time = 0
        self.shooting_cooldown = 0.3  # Seconds between shots

    def update(self, keys):
        # Movement controls
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep the player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shooting_cooldown:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
            bullet = Bullet(self.rect.centerx, self.rect.centery, angle)
            self.last_shot_time = current_time
            return bullet
        return None  # No bullet if the cooldown is not over

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        self.angle = angle

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)

        # Remove bullet if it goes out of bounds
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left < 0 or self.rect.right > WIDTH:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 40)
        self.rect.y = random.randint(0, HEIGHT - 40)
        self.health = 50
        self.speed = 2

    def update(self):
        # Move towards the player
        player_x, player_y = player.rect.center
        angle = math.atan2(player_y - self.rect.centery, player_x - self.rect.centerx)
        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)

        # Check for collision with player
        if self.rect.colliderect(player.rect):
            player.health -= 1
            self.kill()

# Game over screen
def game_over_screen():
    screen.fill(BLACK)
    game_over_text = font.render("Game Over", True, WHITE)
    restart_text = font.render("Press R to Restart", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 3, HEIGHT // 3))
    screen.blit(restart_text, (WIDTH // 3, HEIGHT // 2))
    pygame.display.flip()

# Initialize game objects
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Main game loop
running = True
game_over = False

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button to shoot
                if not game_over:
                    bullet = player.shoot()
                    if bullet:
                        all_sprites.add(bullet)
                        bullets.add(bullet)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Restart the game
                game_over = False
                player.health = 100
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                enemies.empty()
                all_sprites.add(player)

    if not game_over:
        # Update player and bullets
        keys = pygame.key.get_pressed()
        player.update(keys)

        # Update bullets
        bullets.update()

        # Spawn enemies randomly
        if random.random() < 0.02:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Update enemies
        enemies.update()

        # Check bullet-enemy collisions
        for bullet in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    enemy.health -= 25
                    if enemy.health <= 0:
                        enemy.kill()

        # Check if player's health is 0
        if player.health <= 0:
            game_over = True
            game_over_screen()

        # Draw everything
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Draw player health
        pygame.draw.rect(screen, WHITE, (10, 10, 200, 20))
        pygame.draw.rect(screen, GREEN, (10, 10, player.health * 2, 20))

        pygame.display.flip()
    else:
        # Display game over screen
        game_over_screen()

pygame.quit()
