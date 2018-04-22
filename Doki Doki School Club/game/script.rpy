﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define n = Character("Natsuki")
define m = Character("Monika")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Natsuki happy

    # These display lines of dialogue.
    play music "/bgm/m1.ogg"
    "whats your name"
    $ y =  renpy.input ("whats's my name?")
    "Hello your in jail"

    "Where do you what to go"
    
    menu:
        "Jail":
            jump Jail
            
        "Home":
            jump  Home
     
    label Jail:
      
      scene jail
      show  jail
    "you are in jail for 100 years"
    "Oh where are you"
    show Natuki happy
    "Natsuki go to your room right now"
    "hello"
    "hello"
    "hello"
    "hello"
    "hello"
    "hello"
    "WAKE UP"
    "I hate Monika"
    "pick one"
    
    menu:
        "kill Monika":
            jump kill_Monika
            
        "go":
            jump  go
            
    label kill_Monika:
    
    scene kill_Monika
    show school
    
    "sorry but i will die"
    
    pause
    
    
    show  stab
    
    pause
    
    "Kill me"
    
    scene dead
    hide Natsuki
    "frghjebghejgegbejgengjegne"
    "FEHBWFIUWFHBIUWFBWYFBVWQ"
    "FHRYHUWBUWFW"
    "FJWEFUIWHBFUIWHFUIWFGWY"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DELETE"
    "DDSKJNJK"
    $ renpy.movie_cutscene("/video/stabing.mp4")
    scene black
    show black
    "Oh no "
    "The ligths"
    "are gone"
    m "Were is monika"
    n "She is gone"
    n "but where"
    menu:
        "Delete":
            jump Delete
            
            label Delete:
            
            m "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            m "im puting the lights back"
            m "3"
            m "2"
            m "1"
            m "lights are back"
            scene school 2
            show school2
            m "cool the light is back"
            m "cool"
            m "i love you Monika"
            n "Monika look at me"
            show  fr
            m "im very sorry for killing you"
            n "Monika your grounded for 14411"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            m "all the new games are sold out"
            m "im very sorry for killing you"
            n "Monika your grounded for 14411"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "4534343"
            n "hi bhbh"
            m "i love you"
            n "Will you kill me"
            voice  "/vocies/scam.wav"
            n"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            hide fr
            hide school2
            show school
            show hrhr
            voice "/vocies/hey.wav"
            n "hey"
            n "hey pick one"
            
            menu:
             "love":
              jump love
              
              label love:
                 
                 show love
                 scene love
                 show vrefeg
                 n "wow i love you"
                 n "your the best Girl in the world"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 n "love"
                 scene city
                 play music "/bgm/space.ogg"
                 show city
                 show Natsukiscreaming
                 n "hi"
                 n "I just love this music"
                 show frfr
                 "do you want to fight"
                 define slideawayright = CropMove(1.0, "slideawayright")
                 
            

    return
