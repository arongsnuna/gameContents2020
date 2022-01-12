import turtle
import time
import random
import winsound

# Create a window
wn = turtle.Screen()
wn.title("Don't Panic")
wn.bgcolor("white")
wn.setup(width=1500,height=800)

# 전역변수
life = 1
Keys = [0, 0, 0, 0]
keys_n = turtle.Turtle()
player = turtle.Turtle()
Mplayer = turtle.Turtle()
Mplayer.hideturtle()
door0 = turtle.Turtle()
door1 = turtle.Turtle()
door2 = turtle.Turtle()
door3 = turtle.Turtle()

# Make pictures can be used
def Register_shape(file_name_list) :
    for file in file_name_list :
        wn.register_shape(file)
Register_shape(["person.gif", "person_left.gif", "person_right.gif", "person_back.gif", 
"door.gif", "num0.gif", "num1.gif", "num2.gif", "num3.gif", "gameover.gif", "mm.gif", 
"mperson.gif", "mperson_left.gif", "mperson_right.gif", "mperson_back.gif"])


# Represent the text "Found keys: "
def KeysFound() :
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color("red")
    pen.goto(400,350)
    pen.write("Found keys: ", move=False, align="left", font=("Arial",24,"normal"))

# Represent the number of keys found
def CompletedKeys(key_num) :
    if key_num == 0 :
        Put_pics(keys_n, "num0.gif", 600, 365)
    if key_num == 1 :
        Put_pics(keys_n, "num1.gif", 600, 365)
    if key_num == 2 :
        Put_pics(keys_n, "num2.gif", 600, 365)
    if key_num == 3 :
        Put_pics(keys_n, "num3.gif", 600, 365)

# Character's dialog
def Lines(dialog, colour, times) :
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.penup()
    pen.color(colour)
    pen.goto(-300, -100)
    pen.write(dialog, move = False, align = "left", font = ("HancomEQN 보통", 18, "normal"))
    time.sleep(times) # Continue the code after 3 sec
    pen.clear()

# Player's movement
def right():
    player.shape("person_right.gif")
    player.setheading(0)
    player.forward(20)

def left():
    player.shape("person_left.gif")
    player.setheading(180)
    player.forward(20)

def up():
    player.shape("person_back.gif")
    player.setheading(90)
    player.forward(20)

def down():
    player.shape("person.gif")
    player.setheading(270)
    player.forward(20)
        
turtle.listen()
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")


# Represent pictures on window
def Put_pics(Object, pic_name, x_cor, y_cor) :
    Object.speed(0)
    Object.penup()
    Object.shape(pic_name)
    Object.goto(x_cor, y_cor)

# Represent doors on map
def Put_doors() :
    Put_pics(door0, "door.gif", -300, 250)
    Put_pics(door1, "door.gif", -400, 170)
    Put_pics(door2, "door.gif", 0, 170)
    Put_pics(door3, "door.gif", 400, 170)

# Hide doors in door_list
def Hide_doors(door_list) :
    for d in door_list :
        d.hideturtle()

def Show_doors(door_list) :
    for d in door_list :
        d.showturtle()

# Represent background
def Background(color, pic) :
    wn.bgcolor(color)
    wn.bgpic(pic)

# Block player from getting out of window
def Player_in_window(character) :
    if (character.xcor() > 750) or (character.xcor()<-750) or (character.ycor()>400) or (character.ycor()<-400):
            character.backward(50)

# Make a player to be on the floor
def Player_in_map(character, room_num) :
    if room_num == 0 :
        if (character.xcor() > 700) or (character.xcor() < -700) or (character.ycor() > 300) or (character.ycor() < -400):
            character.backward(50)
    elif room_num == 1 :
        if (character.xcor() > 650) or (character.xcor() < -650) or (character.ycor() > 180) or (character.ycor() < -400):
            character.backward(50)
        if (character.xcor() > 420) and (character.ycor() < -120) :
            character.backward(50)
    elif room_num == 2 :
        if (character.xcor() > 330) or (character.xcor() < -390) or (character.ycor() > 270) or (character.ycor()<-400):
            character.backward(50)
    elif room_num == 3 :
        if (character.xcor() > 550) or (character.xcor() < -550) or (character.ycor() > 250) or (character.ycor()<-400):
            character.backward(50)
        if (character.xcor() < -300) and (character.ycor() < 50) :
            character.backward(50)
    else :
        if (character.xcor() > 700) or (character.xcor() < -700) or (character.ycor() > 200) or (character.ycor()<-400):
            character.backward(50)
        if (character.xcor() < -40) and (character.ycor() < -170) :
            character.backward(50)


# 소리재생
def play_sound(file):
    winsound.PlaySound(file, winsound.SND_ASYNC)
    
# Draw a line
def Draw(x_cor1, y_cor1, x_cor2, y_cor2) :
    PEN = turtle.Turtle()
    PEN.speed(0)
    PEN.pensize(10)
    wn.colormode(255)
    PEN.pencolor(153, 153, 153)
    PEN.pencolor(153, 153, 153)
    PEN.penup()
    PEN.goto(x_cor1, y_cor1)
    PEN.pendown()
    PEN.goto(x_cor2, y_cor2)


if __name__ == "__main__" :
    Background("black", "room0.gif")

    Put_pics(player, "person.gif", 250, -300)
    Put_pics(Mplayer, "mperson.gif", -350, 330)
    Mplayer.hideturtle()

    KeysFound()
    CompletedKeys(sum(Keys))
    Put_doors() 
    Hide_doors([door1, door2, door3])

    play_sound("bgm.wav")
    Lines("나: 여긴 어디지??","black", 1.5)
    Lines("나: 일단 여기서 나가야겠어", "black", 1.5)
    player_location = "room0"
    

    while life == 1 :
        wn.update()
        Player_in_window(player)
        
        while player_location == "room0" :
            Hide_doors([door1, door2, door3])
            Background("black", "room0.gif")

            if ((door0.xcor() - 40) < player.xcor() < (door0.xcor() + 40)) and (player.ycor() >= door0.ycor()) : # Player goes corridor
                player_location = "corridor"
                player.goto(-400, -100)
                door0.goto(-400, -170)
            
        # corridor
        while player_location == "corridor" :
            Show_doors([door0, door1, door2, door3])
            Background("black", "corridor.gif")
            Player_in_map(player, -1)

            if ((door1.xcor() - 40.0) < player.xcor() < (door1.xcor() + 40.0)) and (player.ycor() > door1.ycor()) : # 복도에서의 door1의 위치
                player_location = "room1"
                player.goto(0, -280)
                break

            elif ((door2.xcor() - 40.0) < player.xcor() < (door2.xcor() + 40.0)) and (player.ycor() > door2.ycor()) : # 복도에서의 door2의 위치
                player_location = "room2"
                player.goto(0, -280)
                break

            elif ((door3.xcor() - 40.0) < player.xcor() < (door3.xcor() + 40.0)) and (player.ycor() > door3.ycor()) : # 복도에서의 door3의 위치
                player_location = "room3"
                player.goto(0, -280)
                break

            elif ((350-100) < player.xcor() < (350 + 100)) and (player.ycor() < -330) : # 탈출구
                if (sum(Keys) == 3) :
                    player_location = "outside"
                    play_sound("END.wav")
                    player.goto(350, 330)
                    Draw(0,400,0,-400)
                    door0.goto(350, -350)
                    door1.goto(-350, -350)
                    Hide_doors([door2, door3])
                    Mplayer.showturtle()
                    Background("white", "escaped.gif")
                    Mplayer.goto(-player.xcor(), player.ycor())
                    Lines("세상이 미쳤다고 생각해서 탈출했는데 그냥 내가 미친거였어....", "black", 3)
                else :
                    Lines("보라색, 초록색, 검은색 자물쇠가 걸려있다.", "black", 2)

        # room 1
        while player_location == "room1" :
    
            Put_pics(door1, "door.gif", 0, -360)
            Hide_doors([door0, door2, door3])
            Background("black", "room1.gif")

            Player_in_map(player, 1)
            if (380 < player.xcor() < 420) and (-350 < player.ycor() < -250) : # Speak ramdom words
                Lines("?? : ..%d.....%d...%d......." %(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)), "black", 2)
            
            if (434 - 50 < player.xcor() < 434 + 50) and (108 < player.ycor()) : # 금고
                if Keys[1] < 1 :
                    password1 = turtle.textinput("금고", "64 @ 120 = ?\n암호를 입력하세요")

                    if password1 == str(64*8) :
                        Keys[1] += 1
                        Lines("검은색 열쇠를 얻었다.","black", 1)
                        CompletedKeys(sum(Keys))
                    else :
                        Lines("잘못된 입력입니다.", "black",1)

                turtle.listen()
            
            if ((door1.xcor() - 40.0) < player.xcor() < (door1.xcor() + 40.0)) and (player.ycor() < door1.ycor()) : # Player go back to corridor
                player_location = "corridor"
                door1.goto(-400, 170)
                player.goto(-400, 150)
                break

        # room 2
        while player_location == "room2" :

            Put_pics(door2, "door.gif", 0, -360)
            Hide_doors([door0, door1, door3])
            Background("black", "room2.gif")
            Player_in_map(player, 2)

            if (-200 - 50 < player.xcor() < -200 + 50) and (220 < player.ycor()) : # 금고
                if Keys[2] < 1 :
                    password2 = turtle.textinput("금고", "\n암호를 입력하세요\n")

                    if password2 == "9168" :
                        Keys[2] += 1
                        Lines("보라색 열쇠를 얻었다.","black", 1)
                        CompletedKeys(sum(Keys))
                        mm.hideturtle()
                    else :
                        Lines("잘못된 입력입니다.", "black",1)

                turtle.listen()
            
            if (150 - 50 < player.xcor() < 150 + 50) and (220 < player.ycor()) : # 감금실 제어기
                if life > 0 :
                    ctrl_input = turtle.textinput("감금실 제어기", "UNLOCK\tA  C\nLOCK  \tB  D\n\n명령어와 감금실 이름을 입력하세요\n")

                    if "UNLOCK" in ctrl_input :
                        if "B" in ctrl_input :
                            Lines("감금실 B가 열렸습니다.", "black",1.5)
                            Lines("B: 고마워.. 보답으로 비밀번호가 적힌 쪽지를 줄게", "black",2)
                            # 쪽지
                            mm=turtle.Turtle()
                            Put_pics(mm, "mm.gif", -500, 250)
                            turtle.listen()
                        
                        else :
                            play_sound("여자비명.wav")
                            life -= 1
                            if "A" in ctrl_input :                                
                                Lines("감금실 A가 열렸습니다.","black", 1.5)
                                play_sound("웃음소리.wav")
                                Lines("환자 A: 이 손맛 그리웠어. 드디어 죽였어.", "red",2)
                                break

                            elif "C" in ctrl_input :
                                Lines("감금실 C가 열렸습니다.","black", 1.5)
                                play_sound("웃음소리.wav")
                                Lines("환자 C: 왜 태어났니. 어차피 죽을꺼. 왜 태어났니.","red", 2)
                                break

                            elif "D" in ctrl_input :
                                Lines("감금실 D가 열렸습니다.","black", 1.5)
                                play_sound("웃음소리.wav")
                                Lines("환자 D: 아갈머리를 찢어부릴라.","red", 2)
                                break
                        
                    elif "LOCK" in ctrl_input :
                        Lines("이미 잠겨있습니다.", "black",1.5)
                    else :
                        Lines("잘못된 입력입니다.","black", 1)

                turtle.listen()
            
            if ((door2.xcor() - 40.0) < player.xcor() < (door2.xcor() + 40.0)) and (player.ycor() < door2.ycor()) : # Player go back to corridor
                player_location = "corridor"
                door2.goto(0, 170)
                player.goto(0, 150)
                break

        
        # room 3
        while player_location == "room3" :

            Put_pics(door3, "door.gif", 0, -360)
            Hide_doors([door0, door1, door2])
            Background("black", "room3.gif")
            Player_in_map(player, 3)

            if ((400 - 50) < player.xcor() < (400 + 50)) and (player.ycor() > 180) :
                if Keys[3] < 1 :
                    password3 = turtle.textinput("금고", "\n암호를 입력하세요\n")

                    if password3 == "나가" :
                        Keys[3] += 1
                        Lines("초록색 열쇠를 얻었다.", "black",1)
                        CompletedKeys(sum(Keys))
                    else :
                        Lines("잘못된 입력입니다.", "black",1)

                turtle.listen()

            if ((door3.xcor() - 40.0) < player.xcor() < (door3.xcor() + 40.0)) and (player.ycor() < door3.ycor()) : # Player go back to corridor
                player_location = "corridor"
                door3.goto(400, 170)
                player.goto(400, 150)
                break
            
        while player_location == "outside" :
            Hide_doors([door2, door3])
            Background("white", "escaped.gif")
            Player_in_window(player)
            Mplayer.goto(-player.xcor(), player.ycor())            

            if player.shape() == "person.gif" :
                Mplayer.shape("mperson.gif")
            elif player.shape() == "person_right.gif" :
                Mplayer.shape("mperson_left.gif")
            elif player.shape() == "person_left.gif" :
                Mplayer.shape("mperson_right.gif")
            elif player.shape() == "person_back.gif" :
                Mplayer.shape("mperson_back.gif")
            
            if ((door0.xcor() - 40.0) < player.xcor() < (door0.xcor() + 40.0)) and (player.ycor() < door0.ycor()) : 
                exit()
            if ((door1.xcor() - 40.0) < player.xcor() < (door1.xcor() + 40.0)) and (player.ycor() < door1.ycor()) : 
                exit()

    # Game over
    play_sound("gameover.wav")
    dead = turtle.Turtle()
    Put_pics(dead, "gameover.gif", 0, 0)
    time.sleep(7)
    exit()  
            
