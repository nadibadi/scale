# build scale world

# pilot level

import pygame
import sys
import os
import time

pygame.init()
# GLOBALS
unit= 50
screenWidth= unit* 11
screenHeight= unit* 13
screen= pygame.display.set_mode((screenWidth,screenHeight+100))
pygame.display.set_caption('SCALE')
clock= pygame.time.Clock()
FPS= 60
heroSpeed= 4
keysXAllowed= {pygame.K_LEFT: -heroSpeed, pygame.K_RIGHT: heroSpeed, pygame.K_a: -heroSpeed, pygame.K_d: heroSpeed}

def main():
    
    running= True
    menuScreen= True
    tutorialScreen= False
    tutResultScreen= False
    helpScreen= False
    gameScreen= False
    

    while running:
        print('SCALING LADDERS prototype initiated. Have fun playing!')
        ### MENU ###

        menu(menuScreen)

        tutorial(tutorialScreen)

        tutResult(tutResultScreen, str(0))

        helpKeys(helpScreen)


def helpKeys(helpScreen):
    while helpScreen:
        screen.fill('white')
        # move
        text= 'move keys'
        position= screenHeight*0.1
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'grey',border= 'darkgrey',text= text,textsize= 30,textcolour= 'black')

        text= 'arrow keys'
        position= screenHeight*0.2
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'black',border= 'darkgrey',text= text,textsize= 30,textcolour= 'white')

        text= 'WASD'
        position= screenHeight*0.3
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'black',border= 'darkgrey',text= text,textsize= 30,textcolour= 'white')

        # action
        text= 'action keys'
        position= screenHeight*0.5
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'grey',border= 'darkgrey',text= text,textsize= 30,textcolour= 'black')

        text= 'space'
        position= screenHeight*0.6
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'black',border= 'darkgrey',text= text,textsize= 30,textcolour= 'white')

        text= 'shift'
        position= screenHeight*0.7
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'black',border= 'darkgrey',text= text,textsize= 30,textcolour= 'white')

        text= 'p'
        position= screenHeight*0.8
        xsize= 4 * unit
        Button(size= (xsize, unit),xpos= screenWidth*0.5-unit*2,ypos= position,colour= 'black',border= 'darkgrey',text= text,textsize= 30,textcolour= 'white')

        xsize= 4 * unit
        menuBUTTON= Button(size= (xsize, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*1,colour= 'grey',border= 'black',text= 'MENU',textsize= 30,textcolour= 'black')
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if menuBUTTON.rect.collidepoint(event.pos):
                    helpScreen= False
                    menuScreen= True
                    menu(menuScreen)
        
        pygame.display.update()

def menu(menuScreen):
# MENU
    logo= pygame.image.load(os.path.join("images","logo.png"))
    logoRect= logo.get_rect()
    logoRect.center= (screenWidth*0.5,screenHeight*0.28)

    # HERO
    heroMenu= Hero("hero.png",0.5,-90/unit,(screenHeight*0.28+185)/unit)
    heroSpeed= 3
    gravity= 0.5
    jumpHeight=8

    stop= False

    while menuScreen:
        # DRAW
        screen.fill('white')

        ### HERO ANIMATION ###
        bottom=pygame.rect.Rect((-100,screenHeight*0.28+unit*2),(screenWidth+200,unit*0.6))
        top=pygame.rect.Rect((185,screenHeight*0.28+unit*2 - 230),(unit,unit*0.6))
        idot=pygame.rect.Rect((185+unit,screenHeight*0.28+unit*2 - 170),(30,unit*0.6))
        um=pygame.rect.Rect((215+unit,screenHeight*0.28+unit*2 - 150),(100,unit*0.6))
        lm=pygame.rect.Rect((315+unit,screenHeight*0.28+unit*2 - 50),(125,unit*0.6))

        floors= [bottom,top,idot,um,lm]

        floorCollideList= list()
        floorHit= 0
        heroMenu.rect.bottom += 1
        for floorIdx, floor in enumerate(floors):
            if floor.collidepoint(heroMenu.rect.midbottom):
                floorHit= floorIdx
                tmp= True
                floorCollideList.append(tmp)
            else:
                tmp= False
                floorCollideList.append(tmp)
            
        heroMenu.rect.bottom -= 1
        if any(floorCollideList):
            floorCollide= True
        else:
            floorCollide= False

        # FALLING
        if not stop:
            if not heroMenu.fall:
                if not floorCollide:
                    heroMenu.fall= True
            if heroMenu.fall:
                heroMenu.ypos+= heroMenu.fall_vel
                heroMenu.fall_vel += gravity
                if floorCollide:
                    heroMenu.fall= False
                    heroMenu.ypos= floors[floorHit].top - 1
                    heroMenu.fall_vel= 0

        ladder= pygame.rect.Rect((185,screenHeight*0.28+unit*2 - 230),(unit,250))

        if heroMenu.xpos > screenWidth + 20:
            heroMenu.xpos = - 50

        if heroMenu.xpos > 210 and heroMenu.xpos < 220:
            stop= True
            heroMenu.movey(-1)

        if heroMenu.ypos <= ladder.top-1:
            stop= False
        ### HERO ANIMATION END ###


        # buttons

        startBUTTON= Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*0.60,colour= 'grey',border= 'black',text= 'GAME',textsize= 30,textcolour= 'black')
        helpBUTTON= Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*0.73,colour= 'grey',border= 'black',text= 'HELP',textsize= 30,textcolour= 'black')
        quitBUTTON= Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*0.86,colour= 'grey',border= 'black',text= 'QUIT',textsize= 30,textcolour= 'black')
        
        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startBUTTON.rect.collidepoint(event.pos):
                    menuScreen= False
                    tutorialScreen= True
                    tutorial(tutorialScreen)
                if helpBUTTON.rect.collidepoint(event.pos):
                    menuScreen= False
                    helpScreen= True
                    helpKeys(helpScreen)
                if quitBUTTON.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()


        # DRAW
        # update screen
        screen.blit(logo,logoRect)
        if not stop:
            heroMenu.movex(1,heroSpeed)
        heroMenu.draw()
        pygame.display.update()
        clock.tick(FPS)


#### SCREEN FUNCTIONS ####
def tutorial(tutorialScreen):
    # draw floors
    floors= list()
    floorParameters= [
        (0,0,11,True),(4,0,4, True), (3,5,1,True), (4,7,1,True), 
        (5,9,3,True), (6,0,2,True), (9,5,5,True), (10,3,1,True), 
        (11,0,2,True), (11,5,2,False), (12,8,3,True) 
                ]
    for p in floorParameters:
        floor= Floor(p[0],p[1],p[2],p[3])
        floors.append(floor)


    # draw door
    door= pygame.rect.Rect((9*unit,screenHeight-13 *unit),(unit,unit))
    winDoor= pygame.rect.Rect((9.75*unit,screenHeight-13 *unit),(10,unit))

    # draw ladders
    ladders= list()
    ladderParameters= [
        (2/3,2,1,0)
                ]
    
    for p in ladderParameters:
        ladder= Ladder("ladder.png",p[0],p[1],p[2],p[3])
        ladders.append(ladder) 
    ladder= ladders[0]

    # draw machines
    machines= list()
    machineParameters= [
        (0.7,0.75,11,9)
                ]
    for p in machineParameters:
        machine= Machine("machine_inactive.png",p[0],p[1],p[2],p[3])
        machines.append(machine)

    # draw gears
    gears= list()
    gearParameters= [
        (0.35,1,6.3)
                ]
    for p in gearParameters:
        gear= Gear("gear.png",p[0],p[1],p[2])
        gears.append(gear)
    gear= gears[0]


    hero= Hero("hero.png",0.5,2,0)

    # PHYSICS
    jumpHeight= 8
    hero.y_vel= jumpHeight
    gravity= 0.5


    ladderCollide= False
    screenCollide= False
    floorCollide= True

    xHist= list()
    xHist.append(hero.xpos)

    yHist= list()
    yHist.append(hero.ypos)

    start_time= time.time()

            ### TUTORIAL ###
    while tutorialScreen:
        # EVENTS
        screen.fill('white')
        restartBUTTON= Button(size= (3 * unit, unit*0.7),xpos= screenWidth*0.25 - 2*unit,ypos= screenHeight*1.07,colour= 'lightgrey',border= 'grey',text= 'RESTART',textsize= 30,textcolour= 'darkgrey')

        giveupBUTTON= Button(size= (3 * unit, unit*0.7),xpos= screenWidth*0.75 - 2*unit,ypos= screenHeight*1.07,colour= 'lightgrey',border= 'grey',text= 'GIVE UP',textsize= 30,textcolour= 'darkgrey')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                    if restartBUTTON.rect.collidepoint(event.pos):
                        tutorial(tutorialScreen)
                    if giveupBUTTON.rect.collidepoint(event.pos):
                        tutorialScreen= False
                        menuScreen= True
                        menu(menuScreen)

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and ladder.visible:
                    if ladder.picked:
                        ladder.scaleLadder()

                elif event.key == pygame.K_SPACE and not hero.jump:
                    hero.jump= True
                # pick and drop
                elif event.key == pygame.K_p and ladder.active and floorCollide:
                    if not ladder.picked and not gear.picked:
                        # and not ladder.rect.bottom > hero.rect.bottom:    Bug
                        ladder.picked= True
                    else:
                        bottomCollide, bottomIdx, allowDrop= checkLadderDrop(floors,ladder)
                        if bottomCollide and allowDrop:
                            ladder.ypos= screenHeight - floorParameters[bottomIdx][0] * unit - 1
                            ladder.picked= False

                elif event.key == pygame.K_p and gear.active:
                    if not gear.picked and not ladder.picked:
                        gear.picked= True
                    else:
                        if machineActive:
                            gear.visible= False
                            machine.image= pygame.image.load(os.path.join("images","machine_active.png"))
                            machine.image= pygame.transform.scale_by(machine.image,machine.scale)

                            floors[machine.floor].visible= True


                        else:
                            gear.picked= False
                        


        # test conditions
        # LADDERS
        laddersActive= list()
        for ladderIdx, ladder in enumerate(ladders):
            # collide
            if hero.rect.colliderect(ladder.rect):
                ladderCollide= True
            else:
                ladderCollide= False

            if abs(ladder.rect.centerx - hero.rect.centerx) < unit * 2 and ladder.rect.top < hero.rect.bottom and ladder.rect.bottom > hero.rect.top:
                ladder.active= True
                laddersActive.append(ladder.active)
                activeLadder= ladderIdx
            else:
                ladder.active= False
                laddersActive.append(ladder.active)

            ladderActive= any(laddersActive)
            if ladderActive:
                ladder= ladders[activeLadder]

            # update YPOS picked ladder
            if ladder.picked:
                ladder.ypos= hero.ypos + unit * -0.10
                if ladder.xpos <= hero.xpos:
                    ladder.xpos= hero.xpos - unit*0.5

                if ladder.xpos >= hero.xpos:
                    ladder.xpos= hero.xpos + unit*0.5

        # GEARS
        gearsActive= list()
        for gearIdx, gear in enumerate(gears):
            # collide
            if hero.rect.colliderect(gear.rect):
                gearCollide= True
            else:
                gearCollide= False

            if abs(gear.rect.centerx - hero.rect.centerx) < unit * 2 and gear.rect.top < hero.rect.bottom and gear.rect.bottom > hero.rect.top:
                gear.active= True
                gearsActive.append(gear.active)
                activeGear= gearIdx
            else:
                gear.active= False
                gearsActive.append(gear.active)

            gearActive= any(gearsActive)
            if gearActive:
                gear= gears[activeGear]

            # update YPOS picked gear
            if gear.picked:
                gear.ypos= hero.ypos + unit * -0.10
                if gear.xpos <= hero.xpos:
                    gear.xpos= hero.xpos - unit*0.7

                if gear.xpos >= hero.xpos:
                    gear.xpos= hero.xpos + unit*0.7


        # Machines
        machinesActive= list()
        for machineIdx, machine in enumerate(machines):
            # active
            if abs(machine.rect.centerx - gear.rect.centerx) < unit * 2 and machine.rect.top < gear.rect.bottom:
                machine.active= True
                machinesActive.append(machine.active)
                activeMachine= machineIdx
            else:
                machine.active= False
                machinesActive.append(machine.active)

            machineActive= any(machinesActive)
            if machineActive:
                machine= machines[activeMachine]

        # MOVEMENTS
        keys= pygame.key.get_pressed()

        # XY MOVEMENTS
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and hero.rect.left > 0:
            x = -1
            hero.movex(x, heroSpeed)
            if ladder.picked:
                ladder.movex(x, heroSpeed)

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and hero.rect.right < screenWidth:
            x = 1
            hero.movex(x, heroSpeed)
            if ladder.picked:
                ladder.movex(x, heroSpeed)

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and ladderCollide and not ladder.picked:
            y = -1
            hero.movey(y)

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ladderCollide and not ladder.picked and not floorCollide:
            y = 1
            hero.movey(y)

        # JUMPING  
        if hero.jump:
            heroSpeed= 2.5
            jumpCollide,jumpHit= checkFloorJump(floors,hero,jumpHeight,yHist)
            if jumpCollide and any(yHist) < floors[jumpHit].rect.top:
                hero.jump= False
                hero.ypos= screenHeight - floorParameters[jumpHit][0] * unit - 1
                hero.y_vel= jumpHeight
            else:
                hero.ypos-= hero.y_vel
                hero.y_vel -= gravity
                
        else:
            heroSpeed= 4

        # Climbing
        climbCollide,climbHit= checkFloorStand(floors,hero,jumpHeight,yHist)
        if ladderCollide and not climbCollide:
            hero.climb= True

        # FALLING
        if not hero.jump:
            if not hero.fall:
                fallCollide,fallHit= checkFloorStand(floors,hero,jumpHeight,yHist)
            if ladder.picked:
                ladderCollide= False
            if not fallCollide and not ladderCollide: # here is the bug that gravity doesnt work when ladder is picked up
                hero.fall= True
            if hero.fall:
                hero.ypos+= hero.fall_vel
                hero.fall_vel += gravity
                fallCollide,fallHit= checkFloorStand(floors,hero,jumpHeight,yHist)
                if fallCollide:
                    hero.fall= False
                    hero.ypos= screenHeight - floorParameters[fallHit][0] * unit - 1
                    hero.fall_vel= 0
        # track coordinates
        pos= [hero.xpos,hero.ypos]
        ls= [xHist,yHist]
        for l,p in enumerate(pos):
            Coord= p
            if Coord != ls[l][-1]:
                ls[l].append(p)
                if len(ls[l]) > 5:
                    del ls[l][0]

        # WIN
        if hero.rect.colliderect(winDoor):
            end_time= time.time()
            elapsed_time= round(end_time-start_time,2)
            tutResultScreen= True
            tutResult(tutResultScreen,elapsed_time)
            tutorialScreen= False
        # DRAW
        
        
        hero.draw()
        for ladder in ladders:
            ladder.draw()

        for machine in machines:
            machine.draw()

        for gear in gears:
            if gear.visible:
                gear.draw()

        for floor in floors:
            floor.draw()

        pygame.draw.rect(screen, 'black', door)
        pygame.draw.rect(screen, 'black', winDoor)
        clock.tick(FPS)
        pygame.display.flip()



def tutResult(tutResultScreen,elapsed_time):
    while tutResultScreen:
        screen.fill('white')
        image= pygame.image.load(os.path.join("images","result.png"))
        imageRect= image.get_rect()
        imageRect.center= (screenWidth/2,screenHeight/2)
        screen.blit(image,imageRect)

        #it took you
        Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*0.7,colour= 'white',border= 'white',text= 'it took you:',textsize= 32,textcolour= 'black')
        #time
        Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*0.78,colour= 'white',border= 'white',text= str(elapsed_time)+' seconds',textsize= 25,textcolour= 'black')
        #can you be faster?
        Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*0.90,colour= 'white',border= 'white',text= 'can you beat your score?',textsize= 25,textcolour= 'black')

        menuBUTTON= Button(size= (4 * unit, unit),xpos= screenWidth*0.5 - 2*unit,ypos= screenHeight*1,colour= 'grey',border= 'black',text= 'MENU',textsize= 30,textcolour= 'black')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuBUTTON.rect.collidepoint(event.pos):
                    tutResultScreen= False
                    menuScreen= True
                    menu(menuScreen)
        
        pygame.display.update()
            

def checkFloorJump(floors,hero,jumpHeight, yHist):
    # FLOORS
    floorCollideList= list()
    floorHit= 0
    hero.rect.bottom += 1
    for floorIdx, floor in enumerate(floors):
        if floor.visible:
            if hero.y_vel < -jumpHeight*0.8 and floor.rect.collidepoint(hero.rect.midbottom):
                tmp= True
                floorCollideList.append(tmp)
                floorHit= floorIdx
            else:
                tmp= False
                floorCollideList.append(tmp)
    hero.rect.bottom -= 1
    if any(floorCollideList):
        floorCollide= True
    else:
        floorCollide= False
    return floorCollide, floorHit

def checkFloorStand(floors,hero,jumpHeight,yHist):
    # FLOORS
    floorCollideList= list()
    floorHit= 0
    hero.rect.bottom += 1
    for floorIdx, floor in enumerate(floors):
        if floor.visible:
            if floor.rect.collidepoint(hero.rect.midbottom):
                floorHit= floorIdx
                tmp= True
                floorCollideList.append(tmp)
            else:
                tmp= False
                floorCollideList.append(tmp)
        
    hero.rect.bottom -= 1
    if any(floorCollideList):
        floorCollide= True
    else:
        floorCollide= False
    return floorCollide, floorHit
    

def checkLadderDrop(floors,ladder):
    bottomCollide= False
    topCollide= False
    topFit= False
    bottomIdx= None
    topIdx= None
    fitIdx= None
    allowDrop= True
    bottomCollideList= list()
    topCollideList= list()
    topFitList= list()
    for floorIdx, floor in enumerate(floors):
        # check if bottom collides with floor
        # move ladder down to probe floor
        ladder.rect.bottom+= unit*0.2
        if floor.rect.collidepoint(ladder.rect.midbottom):
            tmp= True
            bottomCollideList.append(tmp)
            bottomIdx= floorIdx
        else:
            tmp= False
            bottomCollideList.append(tmp)
        
        ladder.rect.bottom-= unit*0.2
    
        # check if top of ladder goes through floor
        if floor.rect.colliderect(ladder.rect):
            tmp= True
            topCollideList.append(tmp)
            topIdx= floorIdx
        else:
            tmp= False
            topCollideList.append(tmp)
        

        # check if top fits to floor
        ladder.rect.bottom+= unit*0.2
        if floor.rect.collidepoint(ladder.rect.midtop):
            tmp= True
            topFitList.append(tmp)
            fitIdx= floorIdx
        else:
            tmp= False
            topFitList.append(tmp)
        ladder.rect.bottom-= unit*0.2

    
    bottomCollide= any(bottomCollideList)
    topCollide= any(topCollideList)
    topFit= any(topFitList)
    if topCollide and topFit:
        allowDrop=True
    elif not topCollide and not topFit:
        allowDrop=False        
    else:
        allowDrop=False
    return bottomCollide, bottomIdx, allowDrop
        


        
class Hero:
    def __init__(self,image,scale,xpos,ypos):
        self.image= pygame.image.load(os.path.join("images",image))
        self.scale= scale
        self.xpos= xpos * unit
        self.ypos= screenHeight - ypos * unit - 1
        self.image= pygame.transform.scale_by(self.image,self.scale)
        self.rect= self.image.get_rect()
        self.jump= False
        self.fall= False
        self.climb= False
        self.y_vel= 0
        self.fall_vel= 0
        self.storage= list()

    def draw(self):
        self.rect.centerx= self.xpos
        self.rect.bottom= self.ypos
        screen.blit(self.image,self.rect)

    def movex(self,x, heroSpeed):
        self.xpos += heroSpeed * x

    def movey(self,y):
        self.ypos += heroSpeed * y


class Ladder:
    def __init__(self,image,scaleInit,scale,xpos,ypos):
        self.image= pygame.image.load(os.path.join("images",image))
        self.scaleInit= scaleInit
        self.scale= scale
        self.scaled= False
        self.xpos= xpos * unit
        self.ypos= screenHeight - ypos * unit - 1
        self.image= pygame.transform.scale_by(self.image,self.scaleInit)
        self.rect= self.image.get_rect()
        self.visible= True
        self.active= False
        self.picked= False

    def draw(self):
        self.rect= self.image.get_rect()
        self.rect.centerx= self.xpos
        self.rect.bottom= self.ypos
        screen.blit(self.image,self.rect)

    def movex(self,x, heroSpeed):
        self.xpos += x * heroSpeed

    def movey(self,y):
        self.ypos += y  * heroSpeed

    # scale
    def scaleLadder(self):
        if not self.scaled:
            self.image= pygame.transform.scale_by(self.image,self.scale)
            self.scaled= True
        else:
            self.image= pygame.transform.scale_by(self.image,1/self.scale)
            self.scaled= False

class Machine:
    def __init__(self, image, scale, xpos, ypos, floor):
        self.image= pygame.image.load(os.path.join("images",image))
        self.scale= scale
        self.image= pygame.transform.scale_by(self.image,self.scale)
        self.xpos= xpos * unit
        self.ypos= screenHeight - ypos * unit - 1
        self.floor= floor
        self.rect= self.image.get_rect()
    
    def draw(self):
        self.rect.centerx= self.xpos
        self.rect.bottom= self.ypos
        screen.blit(self.image,self.rect)

class Gear(Ladder):
    def __init__(self,image,scaleInit,xpos,ypos):
        self.image= pygame.image.load(os.path.join("images",image))
        self.scaleInit= scaleInit
        self.xpos= xpos * unit
        self.ypos= screenHeight - ypos * unit - 1
        self.image= pygame.transform.scale_by(self.image,self.scaleInit)
        self.rect= self.image.get_rect()
        self.visible= True
        self.active= False
        self.picked= False

    def place(self):
        self.visible= False

class Button:
    def __init__(self,size,xpos,ypos,colour,border,text,textsize,textcolour):
        self.size= size
        self.xpos= xpos
        self.ypos= ypos
        self.colour= colour
        self.border= border
        self.text= text
        self.textsize= textsize
        self.textcolour= textcolour
        self.rect= pygame.rect.Rect((self.xpos,self.ypos),self.size)
        self.draw()

    def draw(self):
        # draw rect
        pygame.draw.rect(screen,self.colour,self.rect,0,5)
        pygame.draw.rect(screen,self.border,self.rect,3,5)
        # define text
        font= pygame.font.Font("freesansbold.ttf",size=self.textsize)
        text= font.render(self.text,True,self.textcolour)
        textRect= text.get_rect()
        textRect.center= self.rect.center
        screen.blit(text, textRect)

class Floor:
    def __init__(self,ypos,xpos,length,visible):
        self.ypos= screenHeight - ypos * unit
        self.xpos= xpos * unit
        self.length= length
        self.visible= visible
        self.rect= pygame.rect.Rect((0,0),(length * unit, unit * 0.5))

    def draw(self):
        if self.visible:
            self.rect.left= self.xpos
            self.rect.top= self.ypos

            pygame.draw.rect(screen, 'darkgrey', self.rect)

main()

