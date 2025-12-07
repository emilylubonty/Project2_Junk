# The script of the game goes in this file

# Jasmine's character definition
define j = Character("Jasmine", color="#6f1a91", image = "jasmine")
define jside = Character ("Jasmine", image = "jasmine")
image side j = "blink"


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
        action Return("mystic")

    # Middle third - Froggie
    imagebutton:
        idle Null(640, 1080)
        hover Null(640, 1080)
        xpos 640
        ypos 0
        hovered SetScreenVariable("h", "froggie")
        unhovered SetScreenVariable("h", None)
        action Return("froggie")

    # Right third - Chaos
    imagebutton:
        idle Null(640, 1080)
        hover Null(640, 1080)
        xpos 1280
        ypos 0
        hovered SetScreenVariable("h", "chaos")
        unhovered SetScreenVariable("h", None)
        action Return("chaos")

# Journal entry display screen
screen journal_entry_display(entry_text, pov_name):
    if entry_text == " ": 
        text " " at canvas_pos ysize 800 size 64
    else: 
        text "[entry_text]" xpos 1100 ypos 400 size 40
    

# Journal interior images
image Chaos Pages room = "Chaos Page.png"
image Mystic Pages room = "Mystic Page.png"
image Froggie Pages room = "Frog Page.png"

# Additional junk journal element images
image tape = "Tape.png"
image Music Note = "Music Note 1.png"
image second music note = "Music Note 2.png"
image drawing space = "Drawing Canvas.png"


# Jasmine's blinking transition
image jasmine: 
    "Jasmine.png"
    3.0
    "Jasmine Blink.png"
    0.15
    repeat

# Transforms
transform zoom_in:
    zoom 1.5


transform center: 
    xalign 0.9
    yalign 0.5

transform slide_right:
    xalign 0.9
    linear 1.0 xalign 1.4

transform left: 
    xalign 0.1
    yalign 0.5

transform music_pos:
    xpos 200
    ypos 100
    zoom 0.6

transform second_music: 
    xpos 600
    ypos 200
    zoom 0.5

transform canvas_pos:
    xpos 1000
    ypos 300
    zoom 0.7

transform tape_pos:
    xpos 1070
    ypos 250
    zoom 0.5

transform cat_pos:
    xpos 1000
    ypos 300
    zoom 1.0


# POV character definition
default povname = ""
define pov = Character("[povname]")


# The game starts here.
label start:
    show bg room at zoom_in

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

# Game begins here
label begin_adventure:

    show bg room empty at zoom_in
    j "Glad to see you've made it. You're probably wondering why I brought you here."
    j "Well... I'll explain soon. Let me show you something important."

    show Journal Choices at zoom_in
    j "[povname], I'm assigning you a task."
    j "You need to choose one journal to document your time spent here, as you'll have no recollection of this ever happening later."
    j "Choose wisely!"

    scene black
    $journal_choice = renpy.call_screen("journal_selection")
    
    if journal_choice == "mystic":
        jump mystic_path
    elif journal_choice == "froggie":
        jump froggie_path
    elif journal_choice == "chaos":
        jump chaos_path

# Mystic Journal Path
label mystic_path:
    show mystic room at zoom_in
    jside "Here we are!"
    j "So, you've chosen the Mystic Journal. Interesting choice!"
    j "This journal is elegant and radiates an ethereal aura. It looks like it was crafted with care."
    j "Let's see what's inside!"

    show Mystic Pages room at zoom_in
    j "Wow! Look at how crisp and clean these pages are."
    j "The pages are completely blank, as if it was untouched."

    j "You're probably still wondering why I brought you here, huh? Well, its to teach you about junk journals!"
    j "A junk journal is a type of journaling that typically uses everyday 'junk' to create a unique and personalized journal."
    j "This can include items like old tickets, fabric scraps, magazine clippings, and more."
    j "As we move into a more digital world, junk journaling can be amplified with digital elements, such as music, photos, and even videos!"
    j "Let me show you a few examples of what you can do with a junk journal."

    show Music Note at music_pos 
    show second music note at second_music
    j "In the digital realm, you can easily add music to your journal."
    j "This can be a song stuck in your head, or just one of your favorites!"

    show drawing space at canvas_pos
    show tape at tape_pos
    j "You can also doodle and draw anything you want right onto the pages!"
    j "Alternatively, you can upload images."

    j "With analog journals, you're unable to add music, images, or videos. But with digital journals, there are endless possibilities!"
    j "Another benefit to digital junk journaling is that you can type out your entries instead of handwriting them."
    j "How about you give it a try right now? Let's try writing a short entry about your experience so far. Or, you can write about anything you like!"
    j "*please do NOT write anything inappropriate or else Jasmine will be sad :(*"

    $entry = renpy.input("Write your journal entry here:", length = 500)
    $entry = entry.strip()

    call screen journal_entry_display(entry, povname)
    if entry == " ":
        j "You didn't write anything? That's okay, junk journals don't have to be filled with words."
        j "It's your journal, you can put whatever you want in it!"
    else:
    j "Great job, [povname]! You've completed your first junk journal entry!"
    j "Junk journaling is all about creativity and self-expression. There's no right or wrong way to do it."
    j "If you don't feel like writing anything, that's A-OK!"
    j "The most important thing is to make it your own. You can add anything you want to your journal, there are no rules!"
    j "It seems our time together is coming to an end. I hope you documented our adventure well." 
    j "If you didn't well... That's okay. I had fun, [povname], and I hope you did too. See you around!"

return

# Froggie Journal Path
label froggie_path:
    show froggie room at zoom_in
    jside "Classic choice!"
    j "The Froggie Journal is always a fun one."
    j "This journal contains tales and adventures of a little frog."
    j "Let's see what's inside!"

    show Froggie Pages room at zoom_in
    j "Oh cool, there are illustrations of lilypads on the inside!"
    j "Oh, the pages are blank? That's toad-tally odd..."
    j "...No? Okay." 

    j "You're probably still wondering why I brought you here, huh? Well, its to teach you about junk journals!"
    j "A junk journal is a type of journaling that typically uses everyday 'junk' to create a unique and personalized journal."
    j "This can include items like old tickets, fabric scraps, magazine clippings, and more."
    j "As we move into a more digital world, junk journaling can be amplified with digital elements, such as music, photos, and even videos!"
    j "Let me show you a few examples of what you can do with a junk journal."

    show Music Note at music_pos 
    show second music note at second_music
    j "In the digital realm, you can easily add music to your journal."
    j "This can be a song stuck in your head, or just one of your favorites!"

    show drawing space at canvas_pos
    show tape at tape_pos
    j "You can also doodle and draw anything you want right onto the pages!"
    j "Alternatively, you can upload images."

    j "With analog journals, you're unable to add music, images, or videos. But with digital journals, there are endless possibilities!"
    j "Another benefit to digital junk journaling is that you can type out your entries instead of handwriting them."
    j "How about you give it a try right now? Let's try writing a short entry about your experience so far. Or, you can write about anything you like!"
    j "*please do NOT write anything inappropriate or else Jasmine will be sad :(*"

    $entry = renpy.input("Write your journal entry here:", length = 500)
    $entry = entry.strip()
    call screen journal_entry_display(entry, povname)
    if entry == " ":
        j "You didn't write anything? That's okay, junk journals don't have to be filled with words."
        j "It's your journal, you can put whatever you want in it!"
    else:
    j "Great job, [povname]! You've completed your first junk journal entry!"
    j "Junk journaling is all about creativity and self-expression. There's no right or wrong way to do it."
    j "If you don't feel like writing anything, that's A-OK!"
    j "The most important thing is to make it your own. You can add anything you want to your journal, there are no rules!"
    j "It seems our time together is coming to an end. I hope you documented our adventure well." 
    j "If you didn't well... That's okay. I had fun, [povname], and I hope you did too. See you around!"
return

# Chaos Journal Path
label chaos_path:
    show chaos room at zoom_in
    jside "Oh... The Chaos Journal..."
    j "Well, whatever floats your boat, [povname]..."
    j "The pages are a bit messy from the puddle it seems to have fallen in, but you can work around it."
    j "Let's see what's inside!"

    show Chaos Pages room at zoom_in 
    j "It looks like someone, or something, has taken a bite out of these pages..."
    j "The pages are also stained with watermarks, but I suppose that adds to its charm."

    j "You're probably still wondering why I brought you here, huh? Well, its to teach you about junk journals!"
    j "A junk journal is a type of journaling that typically uses everyday 'junk' to create a unique and personalized journal."
    j "This can include items like old tickets, fabric scraps, magazine clippings, and more."
    j "As we move into a more digital world, junk journaling can be amplified with digital elements, such as music, photos, and even videos!"
    j "Let me show you a few examples of what you can do with a junk journal."

    show Music Note at music_pos 
    show second music note at second_music
    j "In the digital realm, you can easily add music to your journal."
    j "This can be a song stuck in your head, or just one of your favorites!"

    show drawing space at canvas_pos
    show tape at tape_pos
    j "You can also doodle and draw anything you want right onto the pages!"
    j "Alternatively, you can upload images and alter them digitally. Or, you could add in animations like GIFs!"
    j "With analog journals, you're unable to add music, images, or videos. But with digital journals, there are endless possibilities."

    j "Another benefit to digital junk journaling is that you can type out your entries instead of handwriting them."
    j "How about you give it a try right now? Let's try writing a short entry about your experience so far. Or, you can write about anything you like!"
    j "*please do NOT write anything inappropriate or else Jasmine will be sad :(*"

    $entry = renpy.input("Write your journal entry here:", length = 500)
    $entry = entry.strip()
    call screen journal_entry_display(entry, povname)
    if entry == " ":
        j "You didn't write anything? That's okay, junk journals don't have to be filled with words."
        j "It's your journal, you can put whatever you want in it!"
    else:
    j "Great job, [povname]! You've completed your first junk journal entry!"
    j "Junk journaling is all about creativity and self-expression. There's no right or wrong way to do it."
    j "If you don't feel like writing anything, that's A-OK!"
    j "The most important thing is to make it your own. You can add anything you want to your journal, there are no rules!"
    j "It seems our time together is coming to an end. I hope you documented our adventure well." 
    j "If you didn't well... That's okay. I had fun, [povname], and I hope you did too. See you around!"
return