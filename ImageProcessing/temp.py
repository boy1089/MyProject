import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab

while(True):
    
    screen = np.array(ImageGrab.grab(bbox = (0, 40, 800, 600)))
    cv2.imshow('test', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    

