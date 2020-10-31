import pygame

pygame.init()

# wlasciwosci okna gry
res = [1000, 586]
window = pygame.display.set_mode(res)
pygame.display.set_caption("Student VS Kibice")

# parametry postaci


# width = 100
# height = 140

clock = pygame.time.Clock()
score = 0


# animacja postaci
idle = pygame.image.load('right1.png')
moveLeft = [pygame.image.load('lewo1.png'), pygame.image.load('lewo2.png'), pygame.image.load('lewo3.png'),
            pygame.image.load('lewo4.png'), pygame.image.load('lewo5.png'), pygame.image.load('lewo6.png'),
            pygame.image.load('lewo7.png'), pygame.image.load('lewo8.png'), pygame.image.load('lewo9.png'),
            pygame.image.load('lewo10.png')]
moveRight = [pygame.image.load('prawo1.png'), pygame.image.load('prawo2.png'), pygame.image.load('prawo3.png'),
             pygame.image.load('prawo4.png'), pygame.image.load('prawo5.png'), pygame.image.load('prawo6.png'),
             pygame.image.load('prawo7.png'), pygame.image.load('prawo8.png'), pygame.image.load('prawo9.png'),
             pygame.image.load('prawo10.png')]
attackMove = [pygame.image.load('attack1.png'), pygame.image.load('attack2.png'), pygame.image.load('attack3.png')]
attackMoveL = [pygame.image.load('attack1L.png'), pygame.image.load('attack2L.png'), pygame.image.load('attack3L.png')]
wallpaper = pygame.image.load('tlo.png')
fanMoveL = [pygame.image.load('kibicl.png'), pygame.image.load('kibic1l.png'), pygame.image.load('kibic2l.png'),
            pygame.image.load('kibic3l.png')]
fanMoveR = [pygame.image.load('kibicP.png'), pygame.image.load('kibic1P.png'), pygame.image.load('kibic2P.png'),
            pygame.image.load('kibic3P.png')]

livesImg = [pygame.image.load('zycie0.png'), pygame.image.load('zycie1.png'), pygame.image.load('zycie2.png'), pygame.image.load('zycie3.png')]


class Player:

    def __init__(self, location_x, location_y, width, height):
        self.width = width
        self.height = height
        self.location_x = location_x
        self.location_y = location_y
        self.move = 10
        self.jump = False
        self.jumpingScore = 10
        self.left = False
        self.right = False
        self.walkingScore = 0
        self.attack = False
        self.attackL = False
        self.attackingScore = 0
        self.hitbox = (self.location_x, self.location_y, 95, 150)
        self.lives = 3
        # self.time = False
        # self.walkedLeftRight = False

    def draw(self, window):
        if self.walkingScore + 1 >= 30:
            self.walkingScore = 0

        if self.attackingScore + 1 >= 9:
            # self.time = True
            self.attackingScore = 0

        if self.left:
            window.blit(moveLeft[self.walkingScore // 3], (self.location_x, self.location_y))
            self.walkingScore += 1
        elif self.right:
            window.blit(moveRight[self.walkingScore // 3], (self.location_x, self.location_y))
            self.walkingScore += 1

        elif self.attack:
            window.blit(attackMove[self.attackingScore // 3], (self.location_x, self.location_y))
            self.attackingScore += 1
        elif self.attackL:
            window.blit(attackMoveL[self.attackingScore // 3], (self.location_x, self.location_y))
            self.attackingScore += 1
        else:
            window.blit(idle, (self.location_x, self.location_y))
        self.hitbox = (self.location_x, self.location_y, 95, 150)
        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        window.blit(livesImg[self.lives], (self.location_x, self.location_y - 10))

    def hit(self, tekst, x):
        self.location_x = 800
        self.location_y = 430
        self.walkingScore = 0
        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render(tekst, 1, (255, 255, 255))
        window.blit(text, (x , 200))
        pygame.display.update()
        i = 0
        self.lives -= 1
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class Fan:

    def __init__(self, location_x, location_y, width, height, xk):
        self.location_x = location_x
        self.location_y = location_y
        self.width = width
        self.height = height
        self.xk = xk
        self.path = [self.location_x, self.xk]
        self.move = 5
        self.walkingScore = 0
        self.hitbox = (self.location_x, self.location_y, 28, 60)
        # self.visible = True

    def draw(self, window):
        if self.walkingScore + 1 >= 9:
            self.walkingScore = 0
        # if self.visible:
        if self.move > 0:
                if self.location_x < self.path[1]:
                    window.blit(fanMoveR[self.walkingScore // 3], (self.location_x, self.location_y))
                    self.location_x += self.move
                    self.walkingScore += 1
                    self.hitbox = (self.location_x, self.location_y, 60, 100)
                    # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)
                else:
                    self.move = self.move * -1
        else:
                if self.location_x > self.path[0]:
                    window.blit(fanMoveL[self.walkingScore // 3], (self.location_x, self.location_y))
                    self.location_x += self.move
                    self.walkingScore += 1
                    self.hitbox = (self.location_x, self.location_y, 70, 100)
                    # pygame.draw.rect(window, (255, 0, 0), self.hitbox, 3)
                else:
                    self.move = self.move * -1

    def stab(self, tekst, x, pos):
        # self.visible = False
        self.location_x = pos
        self.location_y = 430
        self.walkingScore = 0
        font1 = pygame.font.SysFont('comicsans', 50)
        text = font1.render(tekst, 1, (255, 255, 255))
        window.blit(text, (x, 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event1 in pygame.event.get():
                if event1.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


def draw_game():

    window.blit(wallpaper, (0, 0))
    text = font.render('Pokonani kibice: ' + str(score), 1, (255, 255, 255))
    window.blit(text, (750, 10))
    kibol.draw(window)
    jeff.draw(window)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
spaceCount = 0
kibol = Fan(0, 450, 64, 105, 1000 - 64)
jeff = Player(450, 430, 100, 140)
game = True


while game:

    clock.tick(30)
    keys = pygame.key.get_pressed()
    # if lives == 0: POZNIEJ
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            game = False
                                                            # if jeff.hitbox[0] + jeff.hitbox[2] > kibol.hitbox[0] + kibol.hitbox[2]:
                                                            #     jeffIsOnRight = True
                                                            #     jeffIsOnLeft = False
                                                            # if jeff.hitbox[0] + jeff.hitbox[2] < kibol.hitbox[0] + kibol.hitbox[2]:
                                                            #     jeffIsOnLeft = True
                                                            #     jeffIsOnRight = False

    if keys[pygame.K_LEFT] and jeff.location_x > jeff.move:
        if keys[pygame.K_SPACE]:
            spaceCount += 1
            if kibol.hitbox[0] + kibol.hitbox[2] > jeff.hitbox[0]:  # and kibol.move > 0:   and jeffIsOnLeft is False:
                if spaceCount <= 30:
                    if kibol.hitbox[0] + kibol.hitbox[2] > jeff.hitbox[0]:
                        kibol.stab('Pokonales kibola!', 100, res[0])
                        score += 1
                        if score % 4 and score >= 4:
                            kibol.move += 5
                else:
                    if kibol.hitbox[0] + kibol.hitbox[2] > kibol.hitbox[0] - 5:
                        jeff.hit("Kibol zrobil unik AAi Cie dopadl!", 250)
                                                                # else:
                                                                    # if jeff.hitbox[0] + jeff.hitbox[2] > kibol.hitbox[0] and kibol.move < 0:
                                                                        # jeff.hit("Kibol zaszedl Cie od tyu!", 300)
            jeff.attackL = True
            jeff.attack = False
            jeff.left = False
            jeff.right = False
        else:
            jeff.location_x -= jeff.move
            jeff.left = True
            jeff.right = False
    elif keys[pygame.K_RIGHT] and jeff.location_x < 1000 - jeff.width - jeff.move:
        if keys[pygame.K_SPACE]:
            spaceCount += 1
            if jeff.hitbox[0] + jeff.hitbox[2] > kibol.hitbox[0]:  # and kibol.move < 0: # and jeffIsOnRight is False:
                if spaceCount <= 30:
                    if jeff.hitbox[0] + jeff.hitbox[2] > kibol.hitbox[0]:
                        # i = i*-1
                        kibol.stab('Pokonales kibola!', 100, 0 - kibol.width)
                        score += 1
                        if score % 4 and score >= 4:
                            kibol.move += 5
                else:
                    if jeff.hitbox[0] + jeff.hitbox[2] > kibol.hitbox[0] - 5:
                        jeff.hit("Kibol zrobil unik i Cie dopadl!", 250)
            # else:
                # if kibol.hitbox[0] + kibol.hitbox[2] > jeff.hitbox[0] and kibol.move > 0:
                    # jeff.hit("Kibol zaszedl cie od tylu!", 300)
            jeff.attack = True
            jeff.attackL = False
            jeff.left = False
            jeff.right = False
        else:
            jeff.location_x += jeff.move
            jeff.left = False
            jeff.right = True
    else:
        spaceCount = 0
        if keys[pygame.K_SPACE]:
            jeff.attack = False
            jeff.attackL = False
            jeff.left = False
            jeff.right = False
        else:
            jeff.attack = False
            jeff.attackL = False
            jeff.attackingScore = 0
            jeff.walkingScore = 0

    if not jeff.jump:
        if keys[pygame.K_UP]:
            jeff.jump = True
            jeff.left = False
            jeff.right = False
            jeff.walkingScore = 0
    else:
        if jeff.jumpingScore >= -10:
            uj = 1
            if jeff.jumpingScore < 0:
                uj = -1
            jeff.location_y -= (jeff.jumpingScore ** 2) * 0.7 * uj
            jeff.jumpingScore -= 1
        else:
            jeff.jumpingScore = 10
            jeff.jump = False
    if jeff.hitbox[1] < kibol.hitbox[1] + kibol.hitbox[3] and jeff.hitbox[1] + jeff.hitbox[3] > kibol.hitbox[1]:
        if jeff.hitbox[0] + jeff.hitbox[2] > kibol.hitbox[0] and jeff.hitbox[0] < kibol.hitbox[0] + kibol.hitbox[2]:
            jeff.hit("Kibol Cie dopadl!", 400)
    draw_game()

pygame.quit()
