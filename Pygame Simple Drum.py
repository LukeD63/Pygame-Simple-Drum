# -*- coding: utf-8 -*-
Created on Tue Oct 17 16:28:03 2017

@author: Lukas Dillingham
"""


import pygame
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512) # changes sample rate and buffersize
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
grey = (105, 105, 105)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

screen = pygame.display.set_mode((1187, 525))
clock = pygame.time.Clock()

class button(object):
    """button class allows the placement of a colored button which can be pushed by the user
    """
    def __init__(self, text, x,y,w,h, pushed, color0, color1, border = 0):
        self.x, self.y, self.w, self.h = x, y, w, h
        # x, y is coords of top left position of rectangle, and w, h, is width height of rect.
        self.pushed = pushed
        self.border = border  # if boarder = 0 then rectangle is filled, 1 is not filled
        self.color0 = color0  # unpushed color
        self.color1 = color1  # pushed color
        self.coords = self.x, self.y
        Rect1 = (self.x, self.y, self.w, self.h)
        self.Return_rect = pygame.draw.rect(screen, (255, 0, 0), Rect1, self.border)
        font = pygame.font.SysFont("reesansbold.ttf", 14)
        width, height = font.size(text)
        self.txt = font.render(text, True, (0, 0, 0))
        xoffset = (self.w-width) // 2
        yoffset = (self.h-height) // 2
        self.coords = self.x + xoffset, self.y + yoffset

    def draw(self, screen):        
        Rect = (self.x, self.y, self.w, self.h)
        if self.pushed:
            pygame.draw.rect(screen, self.color1, Rect, self.border)
            screen.blit(self.txt, self.coords)
        else:
            pygame.draw.rect(screen, self.color0, Rect, self.border)
            screen.blit(self.txt, self.coords)
        
    def push(self):
        if self.pushed == False:
            self.pushed = True
        else:
            self.pushed = False
        self.draw(screen)
        
    def is_pushed(self):
        return self.pushed
        
    def button_rect(self): 
        #boarder_rectangle =  self.get_boarder_rect()
        return self.Return_rect

class CenteredText(object):
    """CenteredText class draws a rectangle with text centered
    in the middle
    """
    def __init__(self, text, font_size, x,y,w,h, color, border = 0):
        self.x, self.y, self.w, self.h = x, y, w, h
        # x, y is coords of top left position of rectangle, and w, h, is width height of rect
        self.border = border  # if boarder = 0 then rectangle is filled, 1 is not filled
        self.color = color
        self.font_size = font_size
        font = pygame.font.SysFont("reesansbold.ttf", self.font_size)
        width, height = font.size(text)
        xoffset = (self.w-width) // 2
        yoffset = (self.h-height) // 2
        self.coords = self.x + xoffset, self.y + yoffset
        self.txt = font.render(text, True, (0, 0, 0))
        
        
    def draw(self, screen):        
        Rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, self.color, Rect, self.border)
        screen.blit(self.txt, self.coords)
        
    def get_boarder_rect(self):
        Rect1 = (self.x, self.y, self.w, self.h)
        R = pygame.draw.rect(screen, (0, 0, 0), Rect1, self.border)
        return R
    
    def get_text(self):
        return self.text
    
class sample(object):
    '''sample class plays an audio file 
    '''
    def __init__(self, file):
        self.file = pygame.mixer.Sound(file)
    
    def play_sound(self):
        self.file.play()        

button_dict = {}
boarder_dict = {}

button_number = 0
for x in range(182, 1142, 30):
    for y in range(120, 460, 30):
        button_dict['button%s' % button_number] = button('', x, y, 20, 20, False, yellow, green, 0)
        boarder_dict['boarder%s' % button_number] = button('', x, y, 19, 19, False, red, red, 2)
        button_number += 1

button_dict['start_button'] = button('RUN', 50, 25, 120, 79, False, yellow, green, 0)
button_dict['Clear'] = button('CLEAR', 717, 25, 120, 79, False, yellow, green, 0)
button_dict['4'] = button('1/4', 422, 50, 50, 50, False, yellow, green, 0)
button_dict['8'] = button('1/8', 482, 50, 50, 50, False, yellow, green, 0)
button_dict['16'] = button('1/16', 542, 50, 50, 50, False, yellow, green, 0)
button_dict['32'] = button('1/32', 602, 50, 50, 50, False, yellow, green, 0)

sample_dict = {}
sample_num = 0
for s in range(0, 384):
    sample_dict['button%s' % s] = sample('sample%s.wav' % sample_num)
    sample_num += 1
    if sample_num > 11:
        sample_num = 0

step_boarder_dict = {}
step_boarder_number = 0
for x in range (177, 1080, 120):
    step_boarder_dict['step_boarder%s' % step_boarder_number] = CenteredText('', 14, x , 115, 120, 360, black, 1)  
    step_boarder_number += 1

label_dict = {}
label_dict['BPM'] = CenteredText('BPM', 20, 237, 25, 120, 20, black, 1)
label_dict['BPM erase'] = CenteredText('', 50, 238, 46, 118, 59, grey, 0)
label_dict['BPM Number'] = CenteredText('128', 50, 237, 46, 120, 59, black, 1)
label_dict['Length of step'] = CenteredText('Length Of Step', 20, 417, 25, 240, 20, black, 1)
label_dict['Length of step boarder'] = CenteredText('', 20, 417, 46, 240, 59, black, 1)
label_dict['Program Title'] = CenteredText('Pygame Simple Drum', 30, 897, 25, 240, 59, black, 1)
label_dict['By Lukas Dillingham'] = CenteredText('By Lukas Dillingham', 24, 897, 85, 240, 19, black, 1)
label_dict['Bass_Drum'] =  CenteredText('Bass Drum', 14, 50, 120, 120, 20, black, 1)
label_dict['Snare'] = CenteredText('Snare', 14, 50, 150, 120, 20, black, 1)
label_dict['Tom1'] = CenteredText('Tom', 14, 50, 180, 120, 20, black, 1)
label_dict['Tom2'] = CenteredText('Tom', 14, 50, 210, 120, 20, black, 1)
label_dict['Cymbal'] = CenteredText('Cymbal', 14, 50, 240, 120, 20, black, 1)
label_dict['Clap'] = CenteredText('Clap', 14, 50, 270, 120, 20, black, 1)
label_dict['Hi Hat'] = CenteredText('Hi Hat', 14, 50, 300, 120, 20, black, 1)
label_dict['Conga'] = CenteredText('Conga', 14, 50, 330, 120, 20, black, 1)
label_dict['Stick'] = CenteredText('Stick', 14, 50, 360, 120, 20, black, 1)
label_dict['Moracas'] = CenteredText('Moracas', 14, 50, 390, 120, 20, black, 1)
label_dict['Cowbell'] = CenteredText('Cowbell', 14, 50, 420, 120, 20, black, 1)
label_dict['Clave'] = CenteredText('Clave', 14, 50, 450, 120, 20, black, 1)

def game_loop():
    
    screen.fill((grey))
    
    #number keys for typing BPM
    number_keys = {K_1 : '1', K_2 : '2', K_3 : '3', K_4 : '4', K_5 : '5', K_6 : '6', \
                   K_7 : '7', K_8 : '8', K_9 : '9', K_0 : '0'}
    
    sound_queue_dict = {}

    for k in step_boarder_dict:
        step_boarder_dict[k].draw(screen)
    
    for k in button_dict:
         button_dict[k].draw(screen)
         
    for k in label_dict:
        label_dict[k].draw(screen)
        
    button_counter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]    
    button_dict['32'].push()
    button_dict['32'].draw(screen)
    sound_queue_dict['32'] = 0
    beats_per_bar_list =  ['4', '8', '16', '32']
    beats_per_bar_list_copy = ['4', '8', '16', '32']
    BPM = 120
    BPM_text = '128'
    BPM_text2 = ''
    change_timer = True   
    
    while True: # game loop
         
         mouse_pos = pygame.mouse.get_pos()
         
         if change_timer:
              for x in beats_per_bar_list:
                  if button_dict[x].is_pushed():
                      x_int = int(x)
                      divisor = x_int // 4
                      BPM_in_milliseconds = 60000 // BPM
                      milliseconds_per_step = BPM_in_milliseconds // divisor
              pygame.time.set_timer(pygame.USEREVENT, milliseconds_per_step)
              change_timer = False
          
         if button_dict['Clear'].is_pushed():
             for q in range (0, 384):
                 q_str = (str(q))
                 if button_dict['button%s' % q_str].is_pushed():
                     button_dict['button%s' % q_str].push()
                     button_dict['button%s' % q_str].draw(screen)
                     if 'button%s' % q_str in sound_queue_dict:
                         del sound_queue_dict['button%s' % q_str]
             button_dict['Clear'].push()
             button_dict['Clear'].draw(screen)
             
             
         for event in pygame.event.get():  
            if event.type == pygame.QUIT:   #allows for user to quit
                pygame.quit()
                return  
            
            if event.type == pygame.USEREVENT:  #timer
                
                for k in button_dict:
                    button_dict[k].draw(screen)
                
                if button_dict['start_button'].is_pushed():
                    for x in button_counter_list:
                        x_str = str(x)
                        boarder_dict['boarder%s' % x_str].draw(screen)                    
                    for w in button_counter_list:
                        w_str = str(w)
                        button_str = 'button' + w_str
                        if button_str in sound_queue_dict:
                            sample_dict[button_str].play_sound()

                    next_counter_list = []
                    for x in button_counter_list:
                         x += 12
                         next_counter_list.append(x)
                    button_counter_list = next_counter_list
                    if button_counter_list[0] > 380:
                         button_counter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]   
                else:
                    button_counter_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for k in button_dict:
                    if button_dict[k].button_rect().collidepoint(mouse_pos):
                        button_dict[k].push()
                        button_dict[k].draw(screen)
                        if button_dict[k].is_pushed():
                            sound_queue_dict[k] = 0
                        else:
                            del sound_queue_dict[k]    
                                                                 
                for i in beats_per_bar_list:
                    if button_dict[i].button_rect().collidepoint(mouse_pos):
                        beats_per_bar_list_copy.remove(i)
                        for l in beats_per_bar_list_copy:
                            if button_dict[l].is_pushed():
                                button_dict[l].push()
                                button_dict[l].draw(screen)
                        change_timer = True
                        beats_per_bar_list_copy = ['4', '8', '16', '32']

            if event.type == pygame.KEYDOWN:
                if event.key in number_keys: 
                    if len(BPM_text2) < 4:
                        BPM_text2 += number_keys[event.key]
                    print(BPM_text2)
                    if len(BPM_text2) == 3:
                        BPM_text_int = int(BPM_text2)
                        if BPM_text_int > 200:
                            BPM_text2 = '200'
                        if BPM_text_int < 100:
                            BPM_text2 = str(BPM_text_int)
                        if BPM_text_int < 20:
                            BPM_text2 = '20'
                        BPM_text = BPM_text2
                        BPM_text2 = ''      
                        label_dict['BPM erase'].draw(screen)
                        label_dict['BPM Number'] = CenteredText(BPM_text, 50, 178, 46, 118, 59, black, 1)
                        label_dict['BPM Number'].draw(screen)
                        BPM = int(BPM_text)
                        change_timer = True

         pygame.display.flip()
         clock.tick(60)

game_loop()