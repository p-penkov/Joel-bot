import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((320, 480))  # Set screen resolution to a multiple of 320x480
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
running = True
dt = 0

# load images
player = pygame.image.load('images/blueship2.png').convert_alpha()  # Use convert_alpha() for transparent background
background = pygame.image.load('images/background_space.png').convert()
background = pygame.transform.scale(background, (320, 480))  # Stretch the background image to fit the resolution
player = pygame.transform.scale(player, (40, 40))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
background_pos = pygame.Vector2(0, 0)
background2_pos = pygame.Vector2(0, -screen.get_height())  # Initialize the second background position above the screen

# Start menu variables
start_menu = True
selected_option = 0
options = ["Start", "Quit"]
font = pygame.font.Font(None, 36)

# Background speed variables
background_speed = 20
background2_speed = 20
speed_increment = 0.5
max_speed = 100

paused = False

while running:
    # Start menu
    if start_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        start_menu = False
                    elif selected_option == 1:
                        running = False

        screen.blit(background, (background_pos.x, background_pos.y))  # Draw the first background
        screen.blit(background, (background2_pos.x, background2_pos.y))  # Draw the second background

        # Draw options
        for i, option in enumerate(options):
            text = font.render(option, True, (255, 255, 0) if i == selected_option else (255, 255, 255))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + i * 40))
            screen.blit(text, text_rect)

        # Reset the first background position when it reaches the bottom
        if background_pos.y >= screen.get_height():
            background_pos.y = -screen.get_height()

        # Reset the second background position when it reaches the bottom
        if background2_pos.y >= screen.get_height():
            background2_pos.y = -screen.get_height()

    # Game logic
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

        if not paused:
            screen.blit(background, (background_pos.x, background_pos.y))  # Draw the first background
            screen.blit(background, (background2_pos.x, background2_pos.y))  # Draw the second background
            screen.blit(player, player_pos)  # Draw the player ship on top of the background

            keys = pygame.key.get_pressed()
            # UP
            if keys[pygame.K_w]:
                if player_pos.y > 0:
                    player_pos.y -= 400 * dt
            # DOWN
            if keys[pygame.K_s]:
                if player_pos.y < screen.get_height() - player.get_height():
                    player_pos.y += 400 * dt
            # LEFT
            if keys[pygame.K_a]:
                if player_pos.x > 0:
                    player_pos.x -= 400 * dt
            # RIGHT
            if keys[pygame.K_d]:
                if player_pos.x < screen.get_width() - player.get_width():
                    player_pos.x += 400 * dt

            # Move the backgrounds down with increasing speed
            background_pos.y += background_speed * dt
            background2_pos.y += background2_speed * dt

            # Increase background speed over time
            if background_speed < max_speed and not start_menu:
                background_speed += speed_increment * dt
            if background2_speed < max_speed and not start_menu:
                background2_speed += speed_increment * dt

            # Reset the first background position when it reaches the bottom
            if background_pos.y >= screen.get_height():
                background_pos.y = -screen.get_height()

            # Reset the second background position when it reaches the bottom
            if background2_pos.y >= screen.get_height():
                background2_pos.y = -screen.get_height()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    dt = clock.tick(120) / 1000

pygame.quit()