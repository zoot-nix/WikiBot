# Modules
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
import sys
import time

answer_A = ["A", "a", "A.", "a."]
answer_B = ["B", "b", "B.", "b."]
answer_C = ["C", "c", "C.", "c."]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]


# Return Name
def returnname():
    print("What's your name? (Enter your name only)")
    global name
    name = input(">>> ")
    if name == "exit":
        print("Goodbye!")
        sys.exit()
    elif name == "help":
        instructions()
    elif name == "return":
        mainmenu()
    else:
        print("\nWow! Cool name,", name, "!\n")


# Instructions
def instructions():
    """Prints instructions on how to operate the chatbot."""
    print(
        "\nI am a robot powered by wikipedia i.e. WikiBot !\n\nFirst off, I returned your name at the beginning of the program!\nFurthermore, I can give you a summary about any topic.\n"
    )
    print(
        'Operating me is very simple, from the main menu, you can follow the on-screen prompts to tell me what to do.\nIf you want to return to the main menu from any action, all you have to say is "return" at any time.\nAfter you finish your action, I will automatically prompt you to return to the main menu as well.\nIf you want me to stop running, then just type "exit" from anywhere in the program.\nDon\'t worry if you can\'t memorize all of this.\nJust type "help" if you can\'t remember, and I will give you these instructions again.'
    )


# Main Menu 
def main_menu_validate(x):
    """Input validation for mainmenu() function"""
    if x == "y":
        wikichat()
    elif x == "n":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
        time.sleep(1)
        mainmenu()
    elif x == "return":
        mainmenu()
    else:
        return False

def mainmenu():  # Main Function
    """Asks the user what they want to do and redirects accordingly"""
    print(
        "\nWould you like to learn about new stuffs? (y/n)"
    )
    time.sleep(1)
    x = input(">>> ")
    main_menu_result = main_menu_validate(x)
    if main_menu_result == False:
        while main_menu_result == False:
            print("Please enter a valid input:")
            x = input(">>> ")
            main_menu_result = main_menu_validate(x)



# Return to Main Menu
def wiki_return_validate(x):
    """Validates input for wiki_return() function."""
    if x in yes:
        mainmenu()
    elif x in no:
        wikichat()
    else:
        return False


def wiki_return():
    """Returns to the mainmenu() function from the wikichat() function"""
    print("Do you want to return to the main menu?")
    x = input(">>> ")
    if x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_return_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input (yes or no):")
                x = input(">>> ")
                wiki_validation_result = wiki_return_validate(x)

# Retrieve Summary of Wikipedia Article
def wiki_article_validate(articlename):
    """Validates the input for the wikichat() function"""
    page_py = wiki_wiki.page(articlename)
    if page_py.exists() == True:
        print("Here you go,", name, ":")
        print(
            "Page - Title: %s" % page_py.title
        ) 
        print(
            "Page - Summary: %s" % page_py.summary
        )  
    else:
        return False
    return page_py


def wikichat():  # Main Function
    """Prompts the user to enter the name of a Wikipedia article to retrieve the summary of said article."""
    print("\nWhat do you want to learn about? (Powered by Wikipedia)")
    x = input(">>> ")
    if x == "exit":
        print("\nThank you! Goodbye!\n")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_article_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input:")
                x = input(">>> ")
                wiki_validation_result = wiki_article_validate(x)
        wiki_return()



# Main Code

print(
    "Hello, my name is WikiBot!\n\nI was created by github@zoot-nix.\n"
)
time.sleep(1)
returnname()
instructions()
print("Now, let's get started!")
mainmenu()
