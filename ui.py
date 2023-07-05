"""UI objects"""

import pygame


class Button:
    """Button Class having multiple methods"""
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.w = w
        self.h = h
        self.text = text
        self.font_size = 20      
        self.color = (25,25, 25)
        self.hover_color = (0, 50, 50)
        self.initial_color = self.color
        self.clicked_color = (125,75,125)
        self.text_color = (155,155,0)
        self.anchor = "center"
        self.clicked = False

    def Update(self):
        """Updates the button if hovered or clicked. If clicked, returns True."""
        action = False
        m_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(m_pos):
            self.color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.color = self.clicked_color
                action = True   
        else:
            self.color = self.initial_color
        return action
    
    def render(self, screen):
        """render button and returns boolean flag, ie either pressed or not"""
        action = self.Update()
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text = font.render(self.text, True, self.text_color)
        textRect = text.get_rect()
        (textRect.x, textRect.y) = self.rect.x+18, self.rect.y+15
        screen.blit(text, textRect)
        return action



class TextUI:
    """A class for rendering text UI"""
    def __init__(self, text, position, fontColor, anchor="center"):
        self.text = text
        self.position = position
        self.fontColor = fontColor
        self.anchor = anchor
        self.fontSize = 20
        self.font = 'freesansbold.ttf'
        
    def render(self, screen, value=""):
        """method for rendering the text"""
        font = pygame.font.Font(self.font, self.fontSize)
        text = font.render(self.text + value, True, self.fontColor)
        textRect = text.get_rect()
        textRect.left, textRect.top = self.position[0], self.position[1]
        # setattr(textRect, self.anchor, self.position)
        screen.blit(text, self.position)
        
        