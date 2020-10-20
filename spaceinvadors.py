
import pygame
pygame.init()

# fix bug at 210 & 212

# debug settings
showHitBoxes = True
showMouse = True

# actual code
width = 1536
height = 801

window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Space Invadors')
hearts = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/hearts.jpg')
fire = pygame.mixer.Sound('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Sounds/lasershot1.wav')
fire3 = pygame.mixer.Sound('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Sounds/lasershot2.wav')
explosion = pygame.mixer.Sound('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Sounds/explosion.wav')
pygame.mixer.music.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Sounds/Fade.mp3')
clock = pygame.time.Clock()


class spaceships:
    def __init__(self):
        self.w = 100
        self.h = 62
        self.x = int(width / 2 - 100 / 2)
        self.y = height - 62 - 80
        self.vel = 3
        self.image = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/spaceship.jpg')
        self.hitbox = (self.x + 16, self.y + 6, self.w - 32, self.h - 15)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x + 16, self.y + 6, self.w - 32, self.h - 15)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)


class lasers:
    def __init__(self, x, y, image):
        self.w = 10
        self.h = 24
        self.x = x
        self.y = y
        self.vel = 7
        self.image = image
        self.hitbox = (self.x + 1, self.y, self.w - 2, self.h - 1)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x + 1, self.y, self.w - 2, self.h - 1)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)


class alien1:
    explode = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/explosion.png')

    def __init__(self, x, y):
        self.w = 50
        self.h = 50
        self.x = x
        self.y = y
        self.vel = 1
        self.direction = 'right'
        self.image = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/alien1.jpg')
        self.hitbox = (self.x + 15, self.y + 21, self.w - 30, self.h - 42)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x, self.y + 5, self.w, self.h - 11)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)

    def destroy(self, window, lst):
        explosion.play()
        self.image = alien1.explode


class alien2(alien1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/alien2.jpg')
        self.hitbox = (self.x + 16, self.y + 16, self.w - 32, self.h - 32)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x, self.y, self.w, self.h)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)


class alien3(alien1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/alien3.png')
        self.hitbox = (self.x + 18, self.y + 25, self.w - 36, self.h - 39)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x + 4, self.y + 3, self.w - 8, self.h - 8)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)


class alien4(alien1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 60
        self.h = 60
        self.image = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/alien4.jpg')
        self.hitbox = (self.x + 5, self.y + 16, self.w - 10, self.h - 32)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x, self.y + 9, self.w, self.h - 17)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)


class alien5(alien1):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.w = 70
        self.h = 70
        self.image = pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/alien5.jpg')
        self.hitbox = (self.x + 2, self.y + 24, self.w - 4, self.h - 48)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if showHitBoxes is True:
            self.hitbox = (self.x, self.y + 18, self.w, self.h - 36)
            pygame.draw.rect(window, (255, 0, 0), self.hitbox, 1)


# aliens1 = alien1(200, 50)
# aliens2 = alien2(300, 50)
# aliens3 = alien3(400, 50)
# aliens4 = alien4(500, 50)
# aliens5 = alien5(600, 50)


def drawWindow(window, loop):
    clock.tick(144)
    window.fill((0, 0, 0))
    for alien in aliens:
        alien.draw(window)
        if alien.image == alien1.explode and loop == 20:
            aliens.remove(alien)
    spaceship.draw(window)
    # aliens1.draw(window)
    # aliens2.draw(window)
    # aliens3.draw(window)
    # aliens4.draw(window)
    # aliens5.draw(window)
    for laser in r_shots:
        laser.draw(window)
    if lives == 3:
        window.blit(hearts, (10, height - 50))
        window.blit(hearts, (70, height - 50))
        window.blit(hearts, (130, height - 50))
    if lives == 2:
        window.blit(hearts, (10, height - 50))
        window.blit(hearts, (70, height - 50))
    if lives == 1:
        window.blit(hearts, (10, height - 50))

    pygame.display.update()


run = True
lives = 3
cooldown = 0
loop = 0
r_shots = []
g_shots = []
aliens = []
spaceship = spaceships()
for i in [y for y in range(10, 190, 60)]:
    for j in [x for x in range(320, 1120, 80)]:
        if i == 10:
            aliens.append(alien3(j, i))
        elif i == 70:
            aliens.append(alien1(j, i))
        else:
            aliens.append(alien2(j, i))

while run:

    if cooldown > 0:
        cooldown += 1
    if cooldown == 100:
        cooldown = 0

    for alien in aliens:
        for laser in r_shots:
            if alien.hitbox[0] < laser.hitbox[0] + laser.hitbox[2] and alien.hitbox[0] + alien.hitbox[2] > laser.hitbox[0]:
                if alien.hitbox[1] < laser.hitbox[1] + laser.hitbox[3] and alien.hitbox[1] + alien.hitbox[3] > laser.hitbox[1]:
                    alien.destroy(window, aliens)
                    r_shots.remove(laser)
                    loop = 0

    for laser in r_shots:
        if laser.y >= 0:
            laser.y -= laser.vel
        else:
            r_shots.remove(laser)

    for alien in aliens:
        if alien.direction == 'left' and aliens[0].x > 200:  # FIX
            alien.x -= 1
        elif alien.direction == 'right' and max(a.x for a in aliens) < width - 200 - alien.w:
            alien.x += 1
        else:
            alien.y += 40
            if alien.direction == 'right':
                alien.direction = 'left'
            else:
                alien.direction = 'right'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT and cooldown == 0:
                fire.play()
                laser = lasers(int(spaceship.x + spaceship.w / 2 - 5), spaceship.y - 24 + 8, pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/laser1.png'))
                r_shots.append(laser)
                cooldown += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_RIGHT and cooldown == 0:
                # fire3.play()
                # for i in [0, 48, 96]:
                #     laser = lasers(int(spaceship.x + spaceship.w / 2 - 5), spaceship.y - 24 + 8 - i, pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/laser1.png'))
                #     r_shots.append(laser)
                # cooldown += 1
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and cooldown == 0:
                fire.play()
                laser = lasers(int(spaceship.x + spaceship.w / 2 - 5), spaceship.y - 24 + 8, pygame.image.load('C:/Users/Christian/OneDrive/Documents/Coding/Python_Code/Space Invadors/Images/laser1.png'))
                r_shots.append(laser)
                cooldown += 1

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    pygame.mouse.set_visible(showMouse)

    if keys[pygame.K_ESCAPE]:
        run = False
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and spaceship.x >= 200:
        spaceship.x -= spaceship.vel
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and spaceship.x <= width - 200 - spaceship.w:
        spaceship.x += spaceship.vel
    if keys[pygame.K_m]:
        pygame.mixer.music.play(-1)

    drawWindow(window, loop)
    loop += 1

pygame.quit()