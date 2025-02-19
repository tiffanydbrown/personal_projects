import pygame
import random

pygame.init()

s_width = 400
s_height = 250

screen = pygame.display.set_mode((s_width, s_height))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)


class Player(pygame.sprite.Sprite):
  def __init__(self, image):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(image, (40, 40))
    self.rect = self.image.get_rect()
    self.rect.bottomleft = (0, s_height)

  def update(self):
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
      self.rect.y -= 5
    if keystate[pygame.K_DOWN]:
      self.rect.y += 5
    if keystate[pygame.K_LEFT]:
      self.rect.x -= 5
    if keystate[pygame.K_RIGHT]:
      self.rect.x += 5

    # Prevent player from leaving boundary
    if self.rect.left <= 0:
      self.rect.left = 0
    if self.rect.bottom >= s_height:
      self.rect.bottom = s_height
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.right >= s_width:
      self.rect.right = s_width


class Enemy(pygame.sprite.Sprite):
  def __init__(self, image, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(image, (40, 40))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.speed = 1

  def update(self, target):
    if self.rect.x > target.rect.x:
      self.rect.x -= self.speed
    elif self.rect.x < target.rect.x:
      self.rect.x += self.speed

    if self.rect.y > target.rect.y:
      self.rect.y -= self.speed
    elif self.rect.y < target.rect.y:
      self.rect.y += self.speed


def draw_text(color, text, font, size, x, y, surface):
    font_name = pygame.font.match_font(font)
    Font = pygame.font.Font(font_name, size)
    text_surface = Font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)


# IMPORT IMAGES:
try:
    player_img = pygame.image.load('images/elephant.png')
    enemy_img = pygame.image.load('images/snake.png')
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    quit()


# CREATING SPRITE GROUPS:
allSprites = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()

# CREATING OBJECTS:
player = Player(player_img)
enemy = Enemy(enemy_img, 50, 50)

# ADD OBJECTS TO GROUPS:
allSprites.add(player)
enemySprites.add(enemy)
allSprites.add(enemy)

time = 0
reset = 0
game_state = "Play"
total_time_limit = 30

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()

    if game_state == "Lose":
      # BLIT GAMEOVER BACKGROUND TO SCREEN
      screen.fill(white)
      draw_text(black, "Game Over!", "arial", 40, s_width // 2, s_height // 2, screen)
    else:
      screen.fill(white)

      # COLLISIONS
      collisions = pygame.sprite.spritecollide(player, enemySprites, False)
    if collisions:
      game_state = "Lose"

      # TIMER FOR PLAYER:
      remaining_time = max(0, total_time_limit - int(pygame.time.get_ticks() / 1000))
      draw_text(black, f"Time: {remaining_time}s", "arial", 20, s_width // 2, 20, screen)

      # TEN SECOND TIMER FOR ENEMY:
    milliseconds = pygame.time.get_ticks() - reset
    if milliseconds >= 10000:
      reset += 10000
      enemy = Enemy(enemy_img, random.randint(0, s_width), random.randint(0, s_height))
      enemySprites.add(enemy)
      allSprites.add(enemy)

      # DRAWING TO SCREEN:
      allSprites.draw(screen)

      # UPDATE GROUPS:
      allSprites.update()
      enemySprites.update(player)

  clock.tick(60)  # 60 FPS
  pygame.display.flip()
