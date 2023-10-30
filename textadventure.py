import sys
import time
import os
from enum import Enum

# To keep track of user's choices
class Choice(Enum):
    LOCKET = 1
    SHOE = 2
    READ_NOTE = 3
    IGNORE_NOTE = 4
    DISGUSTED = 5
    APPALLED = 6
    READY = 7
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Obtains user's choice for scene_0
def scene_0_choice():
    choices = {
        "1": Choice.LOCKET,
        "2": Choice.SHOE,
    }
    prompt = "Choose [1] for locket or [2] for shoe: "
    return choices[get_user_input(prompt, choices.keys())]

# Error checking for user input   
def get_user_input(prompt, valid_inputs):
    while True:
        try:
            user_input = input(prompt)
            if user_input not in valid_inputs:
                raise ValueError("Input must be 1 or 2. Please try again.")
            return user_input
        except ValueError as ve:
            print(ve)

# Enables text scroll output animation
def scrollout(input_string):
    for char in input_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # You can adjust the delay here
    print()

# Player chooses to read or ignore the note on the laptop
def scene_1_choice():
    choices = {
        "1": Choice.READ_NOTE,
        "2": Choice.IGNORE_NOTE,
    }
    prompt = "Read the note? [1] for yes or [2] for no: "
    return choices[get_user_input(prompt, choices.keys())]

# Player chooses their emotion in response to reading the note
def scene_2_choice():
    choices = {
        "1": Choice.DISGUSTED,
        "2": Choice.APPALLED,
    }
    prompt = "Choose [1] for disgusted or [2] for appalled: "
    return choices[get_user_input(prompt, choices.keys())]

# Player chooses to start the game
def scene_3_choice():
    choices = {
        "1": Choice.READY,
    }
    prompt = "Ready to hack? Press [1] when you're ready: "
    return choices[get_user_input(prompt, choices.keys())]

# Begins game
def scene_0():
    display_scene_0()
    return scene_0_choice()

# Displays intro scene to player
def display_scene_0():
    scrollout("In this game, you play a master hacker, who is capable of doing anything.")
    scrollout("Tell me, where do you keep your secret tools for emergencies? [1||2]: ")
    print()
    scrollout("1. In the old silver locket tucked under your shirt; there is a microSD card nestled behind a photo of someone.")
    print()
    scrollout("2. In an imperceptively carved slot in the sole of your shoe, where it's safe and completely out of sight.")

# Displays scene 1 to user
def scene_1(start):
    emergencytools = start
    print()
    scrollout("You wake up on the cold floor of an empty, windowless cell.")
    scrollout("Your head hurts. Bad.")
    scrollout("In the corner, there's an ancient-looking laptop. It's about an inch thick, and whirring violently.")
    scrollout("There's a note on it.")
    choice = scene_1_choice()

    if choice == Choice.READ_NOTE:
        read_note()
    else:
        scrollout("You don't have to listen to the POS who decided to kidnap you.")
        scrollout("You crumple the note up and toss it aside.")

    scene_2(emergencytools)

# Optional scene
# Displas read note scene to player
def read_note():
    print()
    scrollout("Note:")
    scrollout("\"No wifi access, obviously. I put some movies on here")
    scrollout("so you'd have something to do. Behave - you don't")
    scrollout("want to mess up what you've got going here. Trust me. ")
    scrollout("-The Good Cop\"")
    print()
    scrollout("As you read the note, you are [1||2]:")
    scrollout("1. Disgusted.")
    scrollout("2. Appalled.")
    choice = scene_2_choice()
    print()

    if choice == Choice.DISGUSTED:
        scrollout("What kind of person could *kidnap* someone and still think they're good?")
    else:
        scrollout("How could they leave a *human being* with nothing but *Nicolas Cage* movies??")
    scrollout("You realize you're dealing with true monsters.")

# Displays scene 2 to player
def scene_2(emergencytools):
    print()
    scrollout("It's time to get the fuck out of here.")
    print()
    scrollout("A grin breaks out over your face.")

    if emergencytools == Choice.LOCKET:
        scrollout("\"Good thing they let me keep my locket,\"")
        print()
        scrollout("You reach to your heart, your fist wrapping around the locket there for a moment before you open it, and pull out a microSD card.")
    else:
        scrollout("\"Good thing they let me keep my shoes,\"")
        print()
        scrollout("You reach down, your fingers deftly fishing through your shoe, and pull out your microSD card.")
    scrollout("With this and the computer, you have everything you need.")
    print()
    scrollout("When you're ready, press 1 to load in the microSD card and start hacking.")
    scene_3_choice()
    scene_3()
    
def scene_3():
	clear()
	print("it worked!")

# Main function, starts program
if __name__ == "__main__":
    start = scene_0()
    if start:
        scene_1(start)

