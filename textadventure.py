import sys
import time
    
def get_user_input(prompt, valid_inputs):
    user_input = input(prompt)
    while user_input not in valid_inputs:
        user_input = input("Input must be 1 or 2: ")
    return user_input
    
def scrollout(input_string):
    for char in input_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)  # You can adjust the delay here
    print()
    
def introScene():
    scrollout("In this game, you play a master hacker, who is capable of doing anything.")
    scrollout("Tell me, where do you keep your secret tools for emergencies? [1||2]: ")
    print()
    scrollout("1. In the old silver locket tucked under your shirt; there is a microSD card nestled behind a photo of someone.")
    print()
    scrollout("2. In an imperceptively carved slot in the sole of your shoe, where it's safe and completely out of sight.")
    user_input = get_user_input("[1||2]: ", ["1", "2"])
    return user_input
    
def scene_1(start):
    emergencytools = start
    print()
    scrollout("You wake up on the cold floor of an empty, windowless cell.")
    scrollout("Your head hurts. Bad.")
    scrollout("In the corner, there's an ancient-looking laptop. It's about an inch thick, and whirring violently.")
    scrollout("There's a note on it.")
    read = get_user_input("Read it? [1||2]: ", ["1", "2"])
    
    if (read == "1"):
        readNote()
    else:
        scrollout("You don't have to listen to the POS who decided to kidnap you.")
        scrollout("You crumple the note up and toss it aside.")
    scene_2(emergencytools)
    
def readNote():
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
    disgust = get_user_input("[1||2]: ", ["1", "2"])
    print()

    if (disgust == "1"):
        scrollout("What kind of person could *kidnap* someone and still think they're good?")
    else:
        scrollout("How could they leave a *human being* with nothing but *Nicolas Cage* movies??")
    scrollout("You realize you're dealing with true monsters.")
    
def scene_2(emergencytools):
    print()
    scrollout("It's time to get the fuck out of here.")
    print()
    scrollout("A grin breaks out over your face.")

    if (emergencytools == "1"):
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
    user_input = get_user_input("Ready? [1]: ", ["1"])
    
if __name__ == "__main__":
    start = introScene()
    if (start):
        scene_1(start)

