import pygame


pygame.init()

# Setting up the grid dimensions
n = 10
cell_size = 45
grid_width = n * cell_size
grid_height = n * cell_size
bg = pygame.image.load('background1.jpg')

# Setting up display dimensions
screen = pygame.display.set_mode((grid_width, grid_height))
pygame.display.set_caption = ("Percolation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NAV_COLOR = (255, 255, 255, 0)
BLUE = (0, 255, 255)


# navigate the system
class navigate(object):
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))


# sites rules
class site(object):
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.open = False
        self.full = False

    def open_site(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))
        self.open = True


def full_site():
    pass


def draw_grid():
    # Drawing horizontal lines
    for y in range(0, grid_height, cell_size):
        pygame.draw.line(screen, WHITE, (0, y), (grid_width, y))

    # Drawing vertical lines
    for x in range(0, grid_width, cell_size):
        pygame.draw.line(screen, WHITE, (x, 0), (x, grid_height))


# def draw_sites():
#     # Draw sites
#     for y in range(0, grid_width, cell_size * 2):
#         pygame.draw.rect(screen, WHITE, (y, 0, cell_size, cell_size))

def redraw_game_window():
    screen.blit(bg, (0, 0))
    draw_grid()
    nav.draw(screen)
    for site in vis_site:
        site.open_site(screen)

    pygame.display.update()


# main loop
nav = navigate(0, 0, cell_size, cell_size, NAV_COLOR)
vis_site = []
full = []
run = True
while run:
    pygame.time.delay(100)

    keys = pygame.key.get_pressed()

    # full sites
    for openSite in vis_site:
        if openSite.y == 0:
            openSite.color = BLUE
            openSite.full = True
            full.append((openSite.x // cell_size, openSite.y))

        if (openSite.x // cell_size, openSite.y - cell_size) in full:
            openSite.color = BLUE
            openSite.full = True
            full.append((openSite.x // cell_size, openSite.y))

        if ((openSite.x // cell_size) - 1, openSite.y) in full:
            openSite.color = BLUE
            openSite.full = True
            full.append((openSite.x // cell_size, openSite.y))

        if ((openSite.x // cell_size) + 1, openSite.y) in full:
            openSite.color = BLUE
            openSite.full = True
            full.append((openSite.x // cell_size, openSite.y))

    # navigating the system
    if keys[pygame.K_LEFT] and nav.x > 0:
        nav.x -= cell_size
        nav.left = True
        nav.right = False
        nav.up = False
        nav.down = False
    if keys[pygame.K_RIGHT] and nav.x < (grid_width - nav.width):
        nav.x += cell_size
        nav.left = False
        nav.right = True
        nav.up = False
        nav.down = False
    if keys[pygame.K_UP] and nav.y > 0:
        nav.y -= cell_size
        nav.left = False
        nav.right = False
        nav.up = True
        nav.down = False
    if keys[pygame.K_DOWN] and nav.y < (grid_height - nav.height):
        nav.y += cell_size
        nav.left = False
        nav.right = False
        nav.up = False
        nav.down = True

    if keys[pygame.K_SPACE]:
        vis_site.append(site(nav.x, nav.y, cell_size, cell_size, BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redraw_game_window()

pygame.quit()
