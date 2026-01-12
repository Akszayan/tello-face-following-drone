import pygame 

def init():
    pygame.init()
    win = pygame.display.set_mode((400,400)) 

def getKey(keyName) :
    ans= False
    
    keyInput = pygame.key.get_pressed()
    for eve in pygame.event.get(): pass 
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
        pygame.display.update()
    return ans

def main():
    if getKey('LEFT') :
        print('left key pressed')
    if getKey('RIGHT') :
        print('right key pressed')
    #if getKey('FRONT') :
     #   print('left key pressed')
    #if getKey('BACK') :
     #   print('left key pressed')

if __name__=='__main__':
    init() 
    while True :
        main()