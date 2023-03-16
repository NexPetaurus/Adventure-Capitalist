
# Recreating Adventure Capitalist But In Python
# imports
import pygame
import math
import time
from Colours import *
from GameVar import *

pygame.init()

# General Prints

print("\nBe Aware Of Cheats And Read The README.md file to know how to use them!\n")
pygame.font.get_fonts()

# General Var

GameName = 'Adventure Capitalist'
screen = pygame.display.set_mode([340, 450])
pygame.display.set_caption(GameName)
icon = pygame.image.load('money.png')
pygame.display.set_icon(icon)
Backround = black
FrameRate = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# ScreenOpen

ScreenOpen = False
MoreButtonExpand = False
NextClicked = False

# Game Start Commands

running = True
Game_Started = False

# Start Screen
while (Game_Started ==  False):
    screen.fill(black)

    OpeningFont = pygame.font.Font('freesansbold.ttf', 40)
    start_lable = OpeningFont.render(str("Click To Start"), True, purewhite)
    undertext = font.render(str("Your Adventure Awaits"), True, gray)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Started = True
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            Game_Started = True
    
    start_lableY = 180
    undertextY = 220


    screen.blit(start_lable,(40, start_lableY))
    screen.blit(undertext,(75, undertextY))

    

    pygame.display.flip()

# Main Def Functions

def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(round(value, 2)), True, white)
    screen.blit(value_text, (16, y_coord - 10))
    return task, length, draw


def draw_button(color, x_coord, cost, owned, manager_cost):
    color_button = pygame.draw.rect(screen, color, [x_coord, 340, 50, 30])
    color_cost = font.render(str(round(cost, 2)), True, black)
    screen.blit(color_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, black)
        screen.blit(manager_text, (x_coord + 2, 410))

    else:

        manager_button = pygame.draw.rect(screen, black, [x_coord, 405, 50, 30])

    return color_button, manager_button

    #Cheats

def draw_cheat_button(color, x_coord, y_coord):
    CheatTask = pygame.draw.rect(screen, color, [x_coord, y_coord, 60, 30])
    cheat_txt = font.render(str("Cheats"), True, white)
    screen.blit(cheat_txt, (x_coord, y_coord + 9))
    return CheatTask

def AddMoney(color, x_coord, y_coord, Mval): 
    TaskAddMoney = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    AddMoney_txt = font.render(str("+" + Mval), True, white)
    screen.blit(AddMoney_txt, (x_coord +10, y_coord + 9))
    return TaskAddMoney

def RebirthAdder(color, x_coord, y_coord, Rval):
    TaskAddRebirth = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    AddRebirth_txt = font.render(str("+ " + Rval +("rb")), True, white)
    screen.blit(AddRebirth_txt, (x_coord + 10, y_coord + 9))
    return TaskAddRebirth

def AllManagers(color, x_coord, y_coord):
    TaskAllManagers = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    AllManagers_txt = font.render(str("Manager"), True, white)
    screen.blit(AllManagers_txt, (x_coord, y_coord + 9))
    return TaskAllManagers

def RESET(color, x_coord, y_coord):
    TaskReset = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    reset_txt = font.render(str("Reset"), True, white)
    screen.blit(reset_txt, (x_coord + 7, y_coord + 9))
    return TaskReset

def IncSpeed(color, x_coord, y_coord, value):
    TaskIncSpeed = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    IncSpeed_txt = font.render(str("+ " + value + "sd"), True, white)
    screen.blit(IncSpeed_txt, (x_coord + 5, y_coord + 9))
    return TaskIncSpeed

def ClearCash(color, x_coord, y_coord):
    TaskClearCash = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    ClearCash_txt = font.render(str("Clear $"), True, white)
    screen.blit(ClearCash_txt, (x_coord + 5, y_coord + 9))
    return TaskClearCash

# Rebirth (Prev was gonna be more game)

def MoreGame(color, x_coord,y_coord):
    TaskMoreGame = pygame.draw.rect(screen, color, [x_coord, y_coord, 70, 30])
    More_txt = font.render(str("ReBirth"), True, white)
    screen.blit(More_txt, (x_coord + 3, y_coord +9))
    return TaskMoreGame


# Main Window

while running:

    timer.tick(FrameRate)

    if green_owned and not draw_green:
        draw_green = True
    if red_owned and not draw_red:
        draw_red = True
    if orange_owned and not draw_orange:
        draw_orange = True
    if white_owned and not draw_white:
        draw_white = True
    if purple_owned and not draw_purple:
        draw_purple = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            TruScore = math.trunc(score)
            ScoreSTR = str(TruScore)
            print("\nYou Ended With: $" + ScoreSTR)
            print("You Had A Total Of " + str(Rebirths) + " rebirths") #16400 to rebirth
            print("This Brings Your Final Score To A Total Of: " + str(TruScore + (16400 * Rebirths))+"\n")
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if Task1AddMoney.collidepoint(event.pos):
                score += H1
            if Task2AddMoney.collidepoint(event.pos):
                score += Th1
            if Task3AddMoney.collidepoint(event.pos):
                score += M1
            if Task4AddMoney.collidepoint(event.pos):
                score += B1
            if Task5AddMoney.collidepoint(event.pos):
                score += T1

            if Task1AddRebirth.collidepoint(event.pos):
                Rebirths += R1
                print(Rebirths)
            if Task2AddRebirth.collidepoint(event.pos):
                Rebirths += R10
                print(Rebirths)
            if Task3AddRebirth.collidepoint(event.pos):
                Rebirths += R50
                print(Rebirths)
            if Task4AddRebirth.collidepoint(event.pos):
                Rebirths += R100
                print(Rebirths)
            if Task5AddRebirth.collidepoint(event.pos):
                Rebirths += R500
                print(Rebirths)

            if TaskClearCash1.collidepoint(event.pos):
                score = 0

            if TaskMoreGame.collidepoint(event.pos):
                Rebirths += 1
                if Rebirths == 1:
                    print("Your Have Achived Your: " + str(Rebirths), "Rebirth")
                else:
                    print("Your Have Achived Your: " + str(Rebirths), "Rebirth")
                score = 100
                green_value = 2 + Rebirths
                red_value = 3 + Rebirths
                orange_value = 5 + Rebirths
                white_value = 6 + Rebirths
                purple_value = 7 + Rebirths
                draw_green = False
                draw_red = False
                draw_orange = False
                draw_white = False
                draw_purple = False
                green_length = 0
                red_length = 0
                orange_length = 0
                white_length = 0
                purple_length = 0 
                green_speed = 5 + Rebirths
                red_speed = 4 + Rebirths
                orange_speed = 3 + Rebirths
                white_speed = 2 + Rebirths
                purple_speed = 1 + Rebirths
                green_cost = 0.1
                green_owned = False
                green_manager_cost = 100 - round(Rebirths/2)
                red_cost = 4
                red_owned = False
                red_manager_cost = 500 - round(Rebirths/2)
                orange_cost = 7
                orange_owned = False
                orange_manager_cost = 1800 - round(Rebirths/2)
                white_cost = 24
                white_owned = False
                white_manager_cost = 4000 - round(Rebirths/2)
                purple_cost = 230
                purple_owned = False
                purple_manager_cost = 10000 - round(Rebirths/2)
                screen = pygame.display.set_mode([340, 450])
                ScreenOpen = False
                MoreButtonExpand = False
                
            if Task1IncSpeed.collidepoint(event.pos):
                green_speed += Speed1
                red_speed += Speed1
                orange_speed += Speed1
                white_speed += Speed1
                purple_speed += Speed1
            if Task2IncSpeed.collidepoint(event.pos):
                green_speed += Speed2
                red_speed += Speed2
                orange_speed += Speed2
                white_speed += Speed2
                purple_speed += Speed2
            if Task3IncSpeed.collidepoint(event.pos):
                green_speed += Speed3
                red_speed += Speed3
                orange_speed += Speed3
                white_speed += Speed3
                purple_speed += Speed3
            if Task4IncSpeed.collidepoint(event.pos):
                green_speed += Speed4
                red_speed += Speed4
                orange_speed += Speed4
                white_speed += Speed4
                purple_speed += Speed4
            if Task5IncSpeed.collidepoint(event.pos):
                green_speed += Speed5
                red_speed += Speed5
                orange_speed += Speed5
                white_speed += Speed5
                purple_speed += Speed5

            if TaskAllManagers.collidepoint(event.pos):
                green_owned = True
                red_owned = True
                orange_owned = True
                purple_owned = True
                white_owned = True
                MoreButtonExpand = True
                screen = pygame.display.set_mode([600, 500])
                print("Showing ReBirth Button")
                
            if TaskReset.collidepoint(event.pos):
                Rebirths = 0
                score = 0
                green_value = 1
                red_value = 2
                orange_value = 3
                white_value = 4
                purple_value = 5
                draw_green = False
                draw_red = False
                draw_orange = False
                draw_white = False
                draw_purple = False
                green_length = 0
                red_length = 0
                orange_length = 0
                white_length = 0
                purple_length = 0
                green_speed = 5
                red_speed = 4
                orange_speed = 3
                white_speed = 2
                purple_speed = 1
                green_cost = 0.1
                green_owned = False
                green_manager_cost = 100
                red_cost = 3
                red_owned = False
                red_manager_cost = 500
                orange_cost = 9
                orange_owned = False
                orange_manager_cost = 1800
                white_cost = 30
                white_owned = False
                white_manager_cost = 4000
                purple_cost = 200
                purple_owned = False
                purple_manager_cost = 10000
                screen = pygame.display.set_mode([340, 450])
                ScreenOpen = False
                MoreButtonExpand = False
            
            if CheatTask1.collidepoint(event.pos):
                
                if MoreButtonExpand == True and ScreenOpen == True and NextClicked == False:
                    screen = pygame.display.set_mode([340, 500])
                    ScreenOpen = False
                    print("CHEATS TOGGLED")
                elif MoreButtonExpand == True and ScreenOpen == False and NextClicked == False:
                    screen = pygame.display.set_mode([600, 500])
                    ScreenOpen = True
                    print("CHEATS TOGGLED")
                elif MoreButtonExpand == False and ScreenOpen == False and NextClicked == False:
                    screen = pygame.display.set_mode([600, 450])
                    ScreenOpen = True
                    print("CHEATS TOGGLED")
                elif MoreButtonExpand == False and ScreenOpen == True and NextClicked == False:
                    screen = pygame.display.set_mode([340, 450])
                    ScreenOpen = False
                    print("CHEATS TOGGLED")
            
                    # 340 500 - MoreButtonExpand = True and ScreenOpen = True 
                    # 600 500 - MoreButtonExpand = True and ScreenOpen = False
                    # 600 450 - MoreButtonExpand = False and ScreenOpen = False
                    # 340 450 - MoreButtonExpand = False and ScreenOpen = True

                elif MoreButtonExpand == True and ScreenOpen == True and NextClicked == True:
                    screen = pygame.display.set_mode([340, 900])
                    ScreenOpen = False
                    print("CHEATS TOGGLED")
                elif MoreButtonExpand == True and ScreenOpen == False and NextClicked == True:
                    screen = pygame.display.set_mode([600, 900])
                    ScreenOpen = True
                    print("CHEATS TOGGLED")
                elif MoreButtonExpand == False and ScreenOpen == False and NextClicked == True:
                    screen = pygame.display.set_mode([600, 900])
                    ScreenOpen = True
                    print("CHEATS TOGGLED")
                elif MoreButtonExpand == False and ScreenOpen == True and NextClicked == True:
                    screen = pygame.display.set_mode([340, 900])
                    ScreenOpen = False
                    print("CHEATS TOGGLED")

                    
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_red = True
            if task3.collidepoint(event.pos):
                draw_orange = True
            if task4.collidepoint(event.pos):
                draw_white = True
            if task5.collidepoint(event.pos):
                draw_purple = True

            if green_manager_buy.collidepoint(event.pos) and score >= green_manager_cost and not green_owned:
                green_owned = True
                score -= green_manager_cost
                if purple_owned and white_owned and orange_owned and red_owned and green_owned:
                    screen = pygame.display.set_mode([340, 500])
                    MoreButtonExpand = True
                    ScreenOpen = False
            if red_manager_buy.collidepoint(event.pos) and score >= red_manager_cost and not red_owned:
                red_owned = True
                score -= red_manager_cost
                if purple_owned and white_owned and orange_owned and red_owned and green_owned:
                    screen = pygame.display.set_mode([340, 500])
                    MoreButtonExpand = True
                    ScreenOpen = False
            if orange_manager_buy.collidepoint(event.pos) and score >= orange_manager_cost and not orange_owned:
                orange_owned = True
                score -= orange_manager_cost
                if purple_owned and white_owned and orange_owned and red_owned and green_owned:
                    screen = pygame.display.set_mode([340, 500])
                    MoreButtonExpand = True
                    ScreenOpen = False
            if white_manager_buy.collidepoint(event.pos) and score >= white_manager_cost and not white_owned:
                white_owned = True
                score -= white_manager_cost
                if purple_owned and white_owned and orange_owned and red_owned and green_owned:
                    screen = pygame.display.set_mode([340, 500])
                    MoreButtonExpand = True
                    ScreenOpen = False
            if purple_manager_buy.collidepoint(event.pos) and score >= purple_manager_cost and not purple_owned:
                purple_owned = True
                score -= purple_manager_cost
                if purple_owned and white_owned and orange_owned and red_owned and green_owned:
                    screen = pygame.display.set_mode([340, 500])
                    MoreButtonExpand = True
                    ScreenOpen = False

            if green_buy.collidepoint(event.pos) and score >= green_cost:
                green_value += .15 + green_value/50
                score -= green_cost
                green_cost += .1 + green_cost/10
                if green_speed > 500:
                    green_speed = 500
                if green_speed <= 500:
                    green_speed += 0.1
            if red_buy.collidepoint(event.pos) and score >= red_cost:
                red_value += 1 + red_value/50
                score -= red_cost
                red_cost += 3 + red_cost/10
                if red_speed > 500:
                    red_speed = 500
                if red_speed <= 500:
                    red_speed += 0.1
            if orange_buy.collidepoint(event.pos) and score >= orange_cost:
                orange_value += 7 + orange_value/50
                score -= orange_cost
                orange_cost += 9 + orange_cost/10
                if orange_speed > 500:
                    orange_speed = 500
                if orange_speed <= 500:
                    orange_speed += 0.1
            if white_buy.collidepoint(event.pos) and score >= white_cost:
                white_value += 15 + white_value/50
                score -= white_cost
                white_cost += 30 + white_cost/10
                if white_speed > 1000:
                    white_speed = 500
                if white_speed <= 500:
                    white_speed += 0.1

            if purple_buy.collidepoint(event.pos) and score >= purple_cost:
                purple_value += 100 + purple_value/50
                score -= purple_cost
                purple_cost += 200 + purple_cost/10
                if purple_speed > 500:
                    purple_speed = 500
                if purple_speed <= 500:
                    purple_speed += 0.1

    screen.fill(Backround)

    task1, green_length, draw_green = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
    task2, red_length, draw_red = draw_task(red, 110, red_value, draw_red, red_length, red_speed)
    task3, orange_length, draw_orange = draw_task(orange, 170, orange_value, draw_orange, orange_length, orange_speed)
    task4, white_length, draw_white = draw_task(white, 230, white_value, draw_white, white_length, white_speed)
    task5, purple_length, draw_purple = draw_task(purple, 290, purple_value, draw_purple, purple_length, purple_speed)

    green_buy, green_manager_buy = draw_button(green, 10, green_cost, green_owned, green_manager_cost)
    red_buy, red_manager_buy = draw_button(red, 70, red_cost, red_owned, red_manager_cost)
    orange_buy, orange_manager_buy = draw_button(orange, 130, orange_cost, orange_owned, orange_manager_cost)
    white_buy, white_manager_buy = draw_button(white, 190, white_cost, white_owned, white_manager_cost)
    purple_buy, purple_manager_buy = draw_button(purple, 250, purple_cost, purple_owned, purple_manager_cost)

    CheatTask1 = draw_cheat_button(deepred, 275, 5)
    TaskAllManagers = AllManagers(deepred, 440, 5)
    TaskReset = RESET(deepred, 525, 5)
    TaskClearCash1 = ClearCash(deepred, 355, 5)

    Task1IncSpeed = IncSpeed(deepred, 440, 50, Speed1str)
    Task2IncSpeed = IncSpeed(deepred, 440, 100, Speed2str)
    Task3IncSpeed = IncSpeed(deepred, 440, 150, Speed3str)
    Task4IncSpeed = IncSpeed(deepred, 440, 200, Speed4str)
    Task5IncSpeed = IncSpeed(deepred, 440, 250, Speed5str)

    Task1AddMoney = AddMoney(deepred, 355, 50, H1str)
    Task2AddMoney = AddMoney(deepred, 355, 100, Th1str)
    Task3AddMoney = AddMoney(deepred, 355, 150, M1str)
    Task4AddMoney = AddMoney(deepred, 355, 200, B1str)
    Task5AddMoney = AddMoney(deepred, 355, 250, T1str)

    Task1AddRebirth = RebirthAdder(deepred, 525, 50, R1str)
    Task2AddRebirth = RebirthAdder(deepred, 525, 100, R10str)
    Task3AddRebirth = RebirthAdder(deepred, 525, 150, R50str)
    Task4AddRebirth = RebirthAdder(deepred, 525, 200, R100str)
    Task5AddRebirth = RebirthAdder(deepred, 525, 250, R500str)

    TaskMoreGame = MoreGame(deepred, 250, 455)

    display_score = font.render('Cash: $' + str(round(score, 2)), True, white, black)
    screen.blit(display_score, (10, 5))

    buy_more = font.render('Buy More: ', True, white)
    screen.blit(buy_more, (10, 315))

    buy_managers = font.render('Buy Managers: ', True, white)
    screen.blit(buy_managers, (10, 380))

    pygame.display.flip()

pygame.quit()
