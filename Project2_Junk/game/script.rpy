# The script of the game goes in this file.

define j = Character("Jasmine", color="#c8ffc8")

image Jasmine Neutral= "sprite_smile_open.png"
image Jasmine Blinking = "sprite_blink.png"

image bg room = "basic_background_gradient.png"

image jasmine: 
    "sprite_smile_open.png"
    3.0
    "sprite_blink.png"
    0.15
    repeat

transform zoom_in:
    zoom 1.5

transform center: 
    xalign 0.5
    yalign 0.5

# The game starts here.

label start:
    show bg room at zoom_in

    show jasmine at center
    show jasmine at zoom_in
    j "Hey! I don't think we've met before. I'm Jasmine."

    j "What's your name?"

    j "Nice to meet you! Say, would you like to go on an adventure with me?"

    # This ends the game.

    return