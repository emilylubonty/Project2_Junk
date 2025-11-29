# The script of the game goes in this file.

# Jasmine's character definition
define j = Character("Jasmine", color="#6f1a91")

image Jasmine Neutral= "Jasmine.png"
image Jasmine Blinking = "Jasmine Blink.png"

image bg room = "Bookshelf Filled.png"
image bg room empty = "Bookshelf Empty.png"

image jasmine: 
    "Jasmine.png"
    3.0
    "Jasmine Blink.png"
    0.15
    repeat

# Jasmine's transforms
transform zoom_in:
    zoom 1.5

transform center: 
    xalign 0.9
    yalign 0.5

transform fade_out:
    linear 2.0 


# POV character definition
default povname = ""
define pov = Character("[povname]")

# The game starts here.

label start:
    show bg room at zoom_in

    show jasmine at center
    show jasmine at zoom_in
    j "Hey! I don't think we've met before. I'm Jasmine."

    j "What's your name?"

    $povname = renpy.input("What is your name?", length = 32)
    $povname = povname.strip()

    if not povname:
        $povname = "Nameless One"
    
    j "Nice to meet you, [povname]!"

    j "Say, [povname] would you like to go on an adventure with me?"

    $povname = renpy.input("Do you want to go on an adventure with Jasmine? (yes/no)", length = 3)
    $povname = povname.strip().lower()

    if povname == "yes":
        j "Yipee! Let's go!"
        jump begin_adventure
    else:
        j "Oh... Okay..."
        j "You can deal with this entire scene again then."
        jump start

label begin_adventure:

    show bg room empty at zoom_in

    show jasmine at center
    show jasmine at zoom_in
    j "Glad to see you've made it. You're probably wondering where I'm taking you."
    j "Well... It's difficult to explain. But I promise you'll like it!"

    

    return