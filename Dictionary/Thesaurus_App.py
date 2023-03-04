#Dictionaries Challenge 21: Thesaurus App
import random


#Defime the thesaurus
thesaurus = {
        "hot": ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
        "cold": ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
        "happy": ['content', 'cheery', 'merry', 'jovial', 'jocular'],
        "sad": ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
    }

#Print welcome information
print("Welcome to the Thesaurus App!")
print("\nChoose a word from the thesaurus and I will give you the synonym.")
print("\nHere are the words in the thesaurus: ")
for key in thesaurus.keys():
    print("\t-" + key)

#Get user input
choice = input("\nWhat world would you like a synonym for: ").lower().strip()
if choice in thesaurus.keys():
    index = random.randint(0, 4)
    print("A synonym for " + choice + " is " + thesaurus[choice][index] + ".")
else:
    print("I'm sorry that word is not currently in the thesaurus")

#Get user input to see the whole thesaurus
choice = input("\nWould you like to see the whole thesaurus (yes/no): ").lower().strip()

#Show all values on the thesaurus
if choice == 'yes':
    for key, values in thesaurus.items():
        print("\n" + key.title() + "synonym are: ")
        for value in values:
            print("\t-" + value)
else:
    print("\nI hope you enjoyed the program. Thank you!")




















    
    
