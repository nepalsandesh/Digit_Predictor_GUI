import pygame
import numpy as np
from grid import Grid
from ui import Button, TextUI
# from ml import Model
from ml import predict
from scipy import ndimage
from joblib import load
import tensorflow as tf


class Window:
    """Window renderer class"""
    def __init__(self, model=None):
        pygame.init()
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.RESOLUTION = (self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 40
        self.running = True
        self.model=model
        self.sigma = 0.75
        
    
    def handle_events(self):
        """handles the input events"""
        if pygame.mouse.get_pressed()[0]:
            x_pos, y_pos = pygame.mouse.get_pos()
            self.grid.update_array(x_pos, y_pos - 100)
        
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
        self.grid = Grid()
        self.reset_button = Button(150, 850, 150, 50, "Reset Grid")
        self.gaussian_blur_button = Button(270, 800, 200, 50, "Gaussian Blur")
        self.predict_button = Button(800, 300, 100, 50, "Predict")
        self.gaussianSigma_plus_button = Button(1000, 800, 60,  60, "+")
        self.gaussianSigma_minus_button = Button(1080, 800, 60,  60, "-")
        self.predicted_text = TextUI("Prediction: ", (950,300), (255,255,255))
        self.sigma_value_text = TextUI("Sigma: ", (960,750), (255,255,255))
        self.app_name = TextUI("Digit Predictor GUI, v_1.0", (700, 50), (255,255,255))
        self.app_name.fontSize = 40
        self.sigma_value_text.fontSize = 40
        self.predicted_text.fontSize = 100
        self.gaussianSigma_plus_button.font_size = 40
        self.gaussianSigma_minus_button.font_size = 40 
        
        while self.running:
            self.screen.fill((60,60,90))
            self.clock.tick(self.FPS)
            self.app_name.render(self.screen)
            self.grid.render(screen=self.screen, filter=True, sigma=self.sigma)
            if self.reset_button.render(self.screen):
                self.grid.reset_array()
                
                
            # # Prediction only after clicking on 'Predict' Button
            # if self.predict_button.render(self.screen):
            #     final_array = ndimage.gaussian_filter(self.grid.grid_array, sigma=1)
            #     self.predicted_text.render(self.screen, str(self.model.predict_input(final_array)[0]))
            
            
            # # Everytime Prediction except if sum of the matrix is zero
            if self.grid.grid_array.sum() != 0:
                final_array = self.grid.get_gaussianBlurerd_array(sigma=self.sigma)
                # prediction = str(self.model.predict_input(final_array)[0])
                # prediction = str(predict(final_array, self.model)[0])
                prediction = str(predict(final_array, self.model))
                self.predicted_text.render(self.screen, prediction)
                
            # if self.gaussian_blur_button.render(self.screen):
            #     print("Hiiiii")
            #     if self.gaussian_blur_button.Update() == False:
            #         print("Hurray......")
            #         self.grid.gaussian_blur()
            
            
            # Customize and render Gaussian Blur Sigma
            self.sigma_value_text.render(self.screen, str(np.round(self.sigma, 2)))
            if self.gaussianSigma_plus_button.render(self.screen):
                self.sigma += 0.01
            elif self.gaussianSigma_minus_button.render(self.screen):
                self.sigma -= 0.01
                
            
            pygame.display.flip()
            self.handle_events()
    

if __name__ == "__main__":
    # # This is for creating and training a model
    # model = Model()
    # model.save_model()
    # # This is loading already trained and saved model
    # model = load('sgd_clf.joblib')
    # tensorflow model
    model = tf.keras.models.load_model('tf_keras/digit_predictor.model')
    
    app = Window(model=model)
    app.run()