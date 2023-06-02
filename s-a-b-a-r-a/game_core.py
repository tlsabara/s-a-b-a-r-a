import pygame

pygame.init()
core_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Secrets at Brotherhood Alpha Rune Arch')

core_window_control_close = True

core_player_position_x = 400
core_player_position_y = 300

core_config_player_step_move = 1


r = 255
g = 255
b = 255

while core_window_control_close:
    pygame.time.delay(4)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            core_window_control_close = False

    core_player_comand = pygame.key.get_pressed()
    if core_player_comand[pygame.K_UP]:
        r = 255 if r < 2 else r - 1
        core_player_position_y -= core_config_player_step_move
    if core_player_comand[pygame.K_DOWN]:
        b = 255 if b < 8 else b - 7
        core_player_position_y += core_config_player_step_move
    if core_player_comand[pygame.K_LEFT]:
        g = 255 if g < 4 else g - 3
        core_player_position_x -= core_config_player_step_move
    if core_player_comand[pygame.K_RIGHT]:
        g = 255 if g < 4 else g - 3
        core_player_position_x += core_config_player_step_move
    core_player_position_init = (core_player_position_x, core_player_position_y)

    core_screen.fill((0,0,0))





    pygame.draw.circle(core_screen, (r, g, b), core_player_position_init, 15)
    pygame.display.update()

pygame.quit()