import pygame

class Window:
    """Window renderer class"""
    def __init__(self):
        pygame.init()
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 40
        self.running = True
    
    def handle_event(self):
        """handles the input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.running = False    
    
    def run(self):
        """Runs the main loop of the app."""
        while self.running:
            self.screen.fill((0,0,0))
            self.clock.tick(self.FPS)
            
            
            pygame.display.flip()
            self.handle_event()
    

if __name__ == "__main__":
    app = Window()
    app.run()