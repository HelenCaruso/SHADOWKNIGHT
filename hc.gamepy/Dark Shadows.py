#Silent House
#Dark Shadows
#Annie Cao,Helen Caruso
#This game is about a knight defeating a ghost. The knight's goal is to escape the house by not getting possessed by the ghost. 

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"Dark Shadows")
bk = Image("haunted house.jpg",game)
bk.resizeTo(game.width, game.height)

ghost=Image("ghost.png",game)
ghost.resizeTo(game.width-640,game.height-350)
ghost.moveTo(ghost.x-150,ghost.y-150)

knight=Image("knight.png",game)
knight.resizeTo(game.width-650,game.height-400)

title=Image("title.png",game)
title.resizeTo(game.width-525,game.height-450)
title.moveTo(title.x+55,title.y-245)

playgame=Image("playgame.png",game)
playgame.resizeTo(game.width-500,game.height-450)
playgame.moveTo(playgame.x+255,playgame.y-95)

backg1=Image("backg1.jpg",game)
backg1.resizeTo(game.width, game.height)

backg2=Image("backg2.jpg",game)
backg2.resizeTo(game.width, game.height)

castle=Image("castle.jpg",game)
castle.resizeTo(game.width, game.height)


key=Image("key.png",game)
key.resizeTo(game.width-555,game.height-475)
key.moveTo(key.x+225,key.y+240)

#title screen
while not game.over:
    game.processInput()
    bk.draw()
    title.draw()
    playgame.draw()
    
    if playgame.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
        
    game.update(30)
    
game.over=False
#Level 1 - game loop
while not game.over:
    game.processInput()
    backg1.draw()
    ghost.draw()
    knight.draw()
    backg1.visble=False
    
    game.update(30)
    
game.over=False
    
#Level 2 - game loop
while not game.over:
    game.processInput()
    backg2.draw()
    ghost.draw()
    knight.draw()
    ghost=[]

    backg2.visble=False
    
    game.update(30)
#winning screen
while not game.over:
    game.processInput()
    castle1.draw()
    knight.draw()
    castle.visble=False

    game.update(30)
    

    

game.over=False

    




game.quit()
