
#morsecode

import board
import digitalio
import time
import sys

led = digitalio.DigitalInOut(board.D2)
led.direction = digitalio.Direction.OUTPUT

def dot():
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(1.0)
    
def dash():
    led.value = True
    time.sleep(2.0)
    led.value = False
    time.sleep(1.0)

# .-
def A():
    dot()
    dash()

# -...
def B():
    dash()
    dot()
    dot()
    
# -.-.
def C():
    dash()
    dot()
    dash()
    dot()

# -..
def D():
    dash()
    dot()
    dot()

# .    
def E():
    dot()
    
#  ..-.
def F():
    dot()
    dot()
    dash()
    dot()

# --.
def G():
    dash()
    dash()
    dot()
# ....
def H():
    dot()
    dot()
    dot()
    dot()

    
def I():
    dot()
    dot()

# .---    
def J():
    dot()
    dash()
    dash()
    dash()

## -.-
def K():
    dash()
    dot()
    dash()

# .-..
def L():
    dot()
    dash()
    dot()
    dot()

# --
def M():
    dash()
    dash()
    
def N():
    dash()
    dot()

# ---
def O():
    dash()
    dash()
    dash()

# .--.
def P():
    dot()
    dash()
    dot()

# --.-
def Q():
    dash()
    dash()
    dot()
    dash()

#.-.
def R():
    dot()
    dash()
    dot()

# ...
def S():
    dot()
    dot()
    dot()
# -
def T():
    dash()
    
# ..-
def U():
    dot()
    dot()
    dash()
    
# ...-
def V():
    dot()
    dot()
    dot()
    dash()
    
# .--
def W():
    dot()
    dash()
    dash()

# -..-
def X():
    dash()
    dot()
    dot()
    dash()

# -.--   
def Y():
    dash()
    dot()
    dash()
    dash()

# --..

def Z():
    dash()
    dash()
    dot()
    dot()
    
def setup():
    print('starting')
    morsecode = {'a' : A, 'b' : B, 'c':C, 'd':D, 'e':E, 'f':F, 'g':G, 'h':H, 'i':I, 'j':J, 'k':K, 'l':L, 
                    'm':M, 'n':N, 'o':O, 'p':P, 'q':Q, 'r':R, 's':S, 't':T,
                    'u':U, 'v':V, 'w':W, 'x':X, 'y':Y, 'z':Z}
    print('finished setup')
    return morsecode

while True:
    code = setup()
    word = input("Enter the encoded word: ")
    word = word.lower() #converts to lowercase
    
    if word == 'exit':
        break
        
    for elem in word:
        myfunc = code[elem]
        myfunc()
        time.sleep(3.0)

