import pygame
import numpy as np
import time

class Grid:
    """Grid array operaton class"""
    def __init__(self, width=1920, height=1080, scale=20, offset=1):
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.rows = self.height//self.scale
        self.columns = self.width//self.scale
        self.grid_array = np.zeros((self.rows, self.columns))        

    def render(self, screen=None):
        """Renders the grid array"""
        for x in np.arange(self.columns):
            for y in np.arange(self.rows):
                rect = pygame.Rect(x*self.scale, y*self.scale, self.scale-self.offset, self.scale-self.offset)
                pygame.draw.rect(screen, (100,100,100), rect)


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
        grid = Grid()
        while self.running:
            self.screen.fill((0,0,0))
            self.clock.tick(self.FPS)
            
            grid.render(screen=self.screen)
            
            
            pygame.display.flip()
            self.handle_event()
    

if __name__ == "__main__":
    app = Window()
    app.run()