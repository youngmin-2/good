from pynput import keyboard
import time
import os

isActive = True

position = {'x':16, 'y':9}

def key_press(key):
    global position
    if key == key.up:
        position['y'] -= 1
    if key == key.down:
        position['y'] += 1
    if key == key.left:
        position['x'] -= 1
    if key == key.right:
        position['x'] += 1

    if position['x'] < 6:
        position['x'] = 6

    if position['x'] > 26: 
        position['x'] = 26

    if position['y'] < 0:
        position['y'] = 0

    if position['y'] > 9:
        position['y'] = 9
        

def key_release(key):
    # print(f'{key} release')
    if key == keyboard.Key.esc:
        global isActive
        isActive = False
        return False



listener = keyboard.Listener(on_press=key_press,on_release=key_release)
listener.start()

print("갤러그 게임 시작")

guide = '     @                     @'
while isActive:
    print('     @@@@@@@@@@@@@@@@@@@@@@@')
    for k in range(10):
        for i in range(len(guide)):
            if position['x'] == i and position['y'] == k:
                print('★', end='')
            else:
                print(guide[i], end='')
        print()
    print('     @@@@@@@@@@@@@@@@@@@@@@@')
    

    time.sleep(0.1)
    os.system('cls')
    
del listener