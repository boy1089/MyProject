import time
from directkeys import PressKey, ReleaseKey, W,A,S,D

while(True):
    
    PressKey(W)
    time.sleep(3)
    ReleaseKey(W)
    time.sleep(3)
    

