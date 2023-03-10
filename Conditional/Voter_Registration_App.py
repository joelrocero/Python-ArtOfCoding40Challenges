#Conditionals CHallenge 18: Voter Registration App

print("Welcome to the Voter Registration App")

#Get user input
name = input("\nPlease enter you name: ").title().strip()
age = int(input("Please enter your age: "))

#Define our list of political parties
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

#if the user is 18 or older, They can register to vote
if age>17:
    print("\nCongratulations " + name + "! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")

    #Display our political parties
    for party in parties:
        print("\t- " + party)

    #Get user input for the party they with to join
    chosen_party = input("\nWhat party would you like to join: ").title().strip()

    #Print a message specific to the party chosen
    if chosen_party in parties:
        print("\nCongratulation " + name + "! You have joined the " + chosen_party + " party!")
        if chosen_party == "Republican" or chosen_party == "Democratic":
            print("That is a major party!")
        elif chosen_party == "Independent":
            print("You are an indenpendent person!")
        else:
            print("That is not a major party.")
    else:
        print("That is not a given party.")
        
#Else the user is younger that 18 yearsold
else:
    print("\nYou are not old enough to register to vote.")






        
