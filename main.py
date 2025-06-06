import pygame

print('Setup Started')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('Setup Finished')

print('Game Started')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close game window
            quit()  # End pygame
