# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:24:36 2020

@author: HP
"""

import pytesseract       
from PIL import Image        
import pyttsx3 
from googletrans import Translator       
img = Image.open('text15.png')      
print(img)                           
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
result = pytesseract.image_to_string(img)    
with open('abc.txt',mode ='w') as file:      
      
                 file.write(result) 
                 print(result) 
                 
                 
                 