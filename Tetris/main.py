import pygame


class Game:  # Game class
    def __init__(self, screen_display):  # Class's constructor
        self.screen = screen_display
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Closing the game
                self.running = False

            if event.type == pygame.MOUSEBUTTONUP:
                match event.button:
                    case 1:  # Left click
                        x, y = pygame.mouse.get_pos()
                        print(x, y)
                    case 2:  # Middle click
                        pass
                    case 3:  # Right click
                        pass
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:  # Right arrow
            pass
        if keys[pygame.K_DOWN]:  # Down arrow
            pass
        if keys[pygame.K_LEFT]:  # Left arrow
            pass

    def update(self):
        pass

    def display(self):
        self.screen.fill("white")
        pygame.display.update()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)  # 60 FPS


# Lancement de la page

pygame.init()  # initialisation des modules pygame
screen = pygame.display.set_mode((1080, 720))  # screen de 1080 pixel sur 720
pygame.display.set_caption("T'triste")
pygame.display.set_icon(pygame.image.load("images/logo.png"))
game = Game(screen)
game.run()
# Début 


# Fin
pygame.quit()
