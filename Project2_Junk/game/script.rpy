# The script of the game goes in this file

# Jasmine's character definition
define j = Character("Jasmine", color="#6f1a91", image = "jasmine")
define jside = Character ("Jasmine", image = "jasmine")


# Jasmine's images
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

image mystic hover = "Mystic Hover.png"
image froggie hover = "Frog Hover.png"
image chaos hover = "Chaos Hover.png"

screen journal_selection:
    # Track which journal is hovered
    default h = None

    # Base image with all three journals
    add "Choices.png" at zoom_in align (0.5, 0.5)

    # Show only the hovered highlight, layered above the base
    if h == "mystic":
        add "Mystic Hover.png" at zoom_in align (0.5, 0.5)
    elif h == "froggie":
        add "Frog Hover.png" at zoom_in align (0.5, 0.5)
    elif h == "chaos":
        add "Chaos Hover.png" at zoom_in align (0.5, 0.5)

    # Invisible rectangular hit areas (assuming 1920x1080, split into thirds)
    # Left third - Mystic
    imagebutton:
        idle Null(640, 1080)
        hover Null(640, 1080)
        xpos 0
        ypos 0
        hovered SetScreenVariable("h", "mystic")
        unhovered SetScreenVariable("h", None)
        action Jump("mystic_path")

    # Middle third - Froggie
    imagebutton:
        idle Null(640, 1080)
        hover Null(640, 1080)
        xpos 640
        ypos 0
        hovered SetScreenVariable("h", "froggie")
        unhovered SetScreenVariable("h", None)
        action Jump("froggie_path")

    # Right third - Chaos
    imagebutton:
        idle Null(640, 1080)
        hover Null(640, 1080)
        xpos 1280
        ypos 0
        hovered SetScreenVariable("h", "chaos")
        unhovered SetScreenVariable("h", None)
        action Jump("chaos_path")



# Journal interior images
image Chaos Pages room = "Chaos Page.png"
image Mystic Pages room = "Mystic Page.png"
image Froggie Pages room = "Frog Page.png"

image tape = "Tape.png"
image music note = "Music Note 1.png"
image second music note = "Music Note 2.png"
image drawing space = "Drawing Canvas.png"

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
    jside "Here we are!"
    j "So, you've chosen the Mystic Journal. Interesting choice!"
    j "This journal is elegant and radiates an ethereal aura. It looks like it was crafted with care."
    j "Let's see what's inside!"

    show Mystic Pages room at zoom_in
    j "Wow! Look at how crisp and clean these pages are."
    j "The pages are completely blank, as if it was untouched."
    j "There is plenty of room for you to document your time here, [povname]."

return

label froggie_path:
    show froggie room at zoom_in
    j "Classic choice! The Froggie Journal is always a fun one."
    j "This journal contains tales and adventures of a little frog."
    j "Let's see what's inside!"

    show Froggie Pages room at zoom_in
    j "Oh cool, there are illustrations of lilypads on the inside!"
    j "Oh, the pages are blank? That's toad-tally odd..."
    j "...No? Okay." 
    j "Since I brought you here to document your adventure, I guess you'll have to fill them in yourself!"
    j "Hop to it, [povname]!"

return

label chaos_path:
    show chaos room at zoom_in
    j "Oh... The Chaos Journal..."
    j "Well, whatever floats your boat, I guess..."
    j "The pages are a bit messy from the puddle it seems to have fallen in, but you can work around it."
    j "Let's see what's inside!"

    show Chaos Pages room at zoom_in 
    j "It looks like someone, or something, has taken a bite out of these pages..."
    j "The pages are also stained with watermarks, but I suppose that adds to its charm."
    j "The pages are blank though, which is perfect for the task of documenting your adventure, [povname]!"


return