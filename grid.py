import numpy as np
import pygame 
from scipy import ndimage
import joblib

class Grid:
    """Grid array operaton class"""
    def __init__(self, width=1920, height=1080, scale=20, offset=1):
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.window_offset = 100
        # self.rows = self.height//self.scale
        self.rows = 28
        # self.columns = self.width//self.scale
        self.columns = 28
        self.grid_array = np.zeros((self.rows, self.columns))      
        # self.grid_array = np.random.randint(0, 2, (self.rows, self.columns))

    def render(self, screen=None, filter=False, sigma=1):
        """Renders the grid array"""
        for x in np.arange(self.columns):
            for y in np.arange(self.rows):
                rect = pygame.Rect(self.window_offset + x*self.scale, self.window_offset + 100 \
                    + y*self.scale, self.scale-self.offset, self.scale-self.offset)
                if filter == False:
                    if self.grid_array[y,x] == 0:
                        pygame.draw.rect(screen, (0,0,0), rect)
                    elif self.grid_array[y,x] > 0:
                        pygame.draw.rect(screen, (11,11,80), rect)
                else:
                    array = self.get_gaussianBlurerd_array(sigma=sigma)
                    color = (array[y,x]%255, array[y,x]%255, array[y,x]%255)
                    pygame.draw.rect(screen, color, rect)

                    
                    
    def update_array(self, x, y):
        """takes mouse position (x,y) and updates the grid"""
        m_pos = pygame.mouse.get_pos()
        j = (x - self.window_offset) // self.scale
        i = (y - self.window_offset) // self.scale
        if (m_pos[0] >= self.window_offset and m_pos[0] <= self.columns*self.scale + self.window_offset) \
            and (m_pos[1] >= self.window_offset and m_pos[1] <= self.rows*self.scale + self.window_offset):
            try:
                if self.grid_array[i,j] != None:
                    self.grid_array[i,j] = 255  #center cell ie clicked cell
                    # neighbor cells
                    self.grid_array[i-1,j-1] = 255
                    self.grid_array[i-1,j] = 255
                    self.grid_array[i-1,j+1] = 255
                    self.grid_array[i+1,j-1] = 255
                    self.grid_array[i+1,j] = 255
                    self.grid_array[i+1,j+1] = 255
                    self.grid_array[i,j-1] = 255
                    self.grid_array[i,j+1] = 255
                    
            except IndexError:
                pass
            
        # joblib.dump(self.grid_array, "array_dump.pkl")
            
    def reset_array(self):
        """reset the array to zeros"""
        self.grid_array = np.zeros((self.rows, self.columns))
        
    def get_gaussianBlurerd_array(self, sigma=1.0):
        """returns the gaussian blurred array"""
        return ndimage.gaussian_filter(self.grid_array, sigma=sigma)
        
        
    
    # Image Processing Stuffs
    def gaussian_blur(self):
        self.grid_array = ndimage.gaussian_filter(self.grid_array, sigma=4)
