# Turorial from http://www.codingwithruss.com/pygame/how-to-use-joysticks-in-pygame/

import pygame

pygame.init()

# initialise the joystick module
pygame.joystick.init()

# define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Joysticks")

# define font
font_size = 30
font = pygame.font.SysFont("Futura", font_size)


# function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# create clock for setting game frame rate
clock = pygame.time.Clock()
FPS = 60

# create empty list to store joysticks
joysticks = []

# create player rectangle
x = 350
y = 200
speed = 5
size = 40
player = pygame.Rect(x, y, size, size)

# define player colour
color = "royalblue"

# game loop
run = True
while run:

    clock.tick(FPS)

    # update background
    screen.fill(pygame.Color("midnightblue"))

    # draw player
    player.topleft = (x, y)
    pygame.draw.rect(screen, pygame.Color(color), player)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.JOYDEVICEADDED:
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)

        # change player colour with buttons
        for joystick in joysticks:
            if joystick.get_button(0):
                color = "royalblue"
            if joystick.get_button(1):
                color = "crimson"
            if joystick.get_button(2):
                color = "fuchsia"
            if joystick.get_button(3):
                color = "forestgreen"

            # player movement with analogue sticks
            horiz_move = joystick.get_axis(0)
            vert_move = joystick.get_axis(1)

            # Dead zone (stick drift)
            horiz_move = horiz_move if abs(horiz_move) > 0.2 else 0
            vert_move = vert_move if abs(vert_move) > 0.2 else 0

            # Normalize diagonal movement
            magnitude = (horiz_move**2 + vert_move**2)**0.5
            if magnitude > 0:
                horiz_move /= magnitude
                vert_move /= magnitude

            x += horiz_move * speed
            y += vert_move * speed

        # quit program
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.flip()

pygame.quit()
