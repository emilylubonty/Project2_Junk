# The script of the game goes in this file

# Jasmine's character definition
define j = Character("Jasmine", color="#6f1a91")

image Jasmine Neutral= "Jasmine.png"
image Jasmine Blinking = "Jasmine Blink.png"

# Background images
image bg room = "Bookshelf Filled.png"
image bg room empty = "Bookshelf Empty.png"

# Journal Choices
image mystic room = "Purple Bookshelf.png"
image froggie room = "Frog Bookshelf.png"
image chaos room = "Chaos Bookshelf.png"

image Journal Choices = "Choices.png"

screen journal_selection: 
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "Choices_%s.png" 
        hover "Choices_%s_hover.png" action Jump("mystic_path")

    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "Choices_%s.png" 
        hover "Choices_%s_hover.png" action Jump("froggie_path")

    imagebutton:
        xalign 1.0
        yalign 0.5
        idle "Choices_%s.png" 
        hover "Choices_%s_hover.png" action Jump("chaos_path")

# Journal interior images
image pages room = "Open Journal.png"

# Jasmine's blinking transition
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

transform slide_right:
    xalign 0.9
    linear 1.0 xalign 1.4

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

    $response = renpy.input("Do you want to go on an adventure with Jasmine? (yes/no)", length = 3)
    $response = response.strip().lower()

    if response == "yes":
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
    j "Glad to see you've made it. You're probably wondering why I brought you here."
    j "Well... I'll explain soon. Let me show you something important."

    show jasmine at slide_right
    j "Follow me!"

    show Journal Choices at zoom_in

    j "[povname], I'm assigning you a task."
    j "You need to choose one journal to document your time spent here, as you'll have no recollection of this ever happening later."
    j "Choose wisely!"

    scene black
    call screen journal_selection

label mystic_path:
    show mystic room at zoom_in
    j "So, you've chosen the Mystic Journal. Interesting choice!"
    j "This journal is elegant and full of wisdom. It looks like it was crafted with care."
    j "Let's see what's inside!"

    show pages room at zoom_in

label froggie_path:
    show froggie room at zoom_in
    j "Classic choice! The Froggie Journal is always a fun one."
    j "This journal contains tales and adventures of a little frog."
    j "Let's see what's inside!"

label chaos_path:
    show chaos room at zoom_in
    j "Oh... The Chaos Journal..."
    j "Well, whatever floats your boat, I guess..."
    j "The pages are a bit messy from the puddle it seems to have fallen in, but you can work around it."
    j "Let's see what's inside!"
return