


# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes
import random


jokes = [
    {"category": "robbers",
     "setup": "Knock Knock",
     "who": "Calder",
     "punchline": "Calder police — I've been robbed!"},

    {"category": "tanks",
     "setup": "Knock Knock",
     "who": "Tank",
     "punchline": "You're welcome!"},

    {"category": "pencils",
     "setup": "Knock Knock",
     "who": "Broken pencil",
     "punchline": "Nevermind… it's pointless!"}
]


def tell_joke(category):

    matching = [j for j in jokes if j["category"] == category]

    if not matching:
        print("That’s not a valid category.")
        return

    
    joke = random.choice(matching)

    input(joke["setup"])
    input(joke["who"])
    print(joke["punchline"])



joke = input("Do you want to hear a joke? (yes/no) ")

if joke == "no":
    print("Okay, suit yourself!")
else:
    while joke == "yes":
        print("Great, let's play!")
        category = input("Choose a joke: robbers, tanks, or pencils: ")

        tell_joke(category)

        joke = input("Do you want to hear another joke or are you finished? (yes/finished) ")


if joke == "finished":
    rate = int(input("Please rate our game 1–10: "))
    final_score = rate * 10
    print(str(final_score) + "% satisfaction rate!")

    friend = input("Would you recommend this game to a friend? (yes/no/maybe) ")

    if friend == "yes" or friend == "maybe":
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")
