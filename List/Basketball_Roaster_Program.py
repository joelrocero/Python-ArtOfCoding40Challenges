#Lists Challenge 9: Basketball Roaster Program

print("Welcome to the Basketball Roaster Program.")

#Get user input and define our roaster
roaster = []
player = input("Who is your point guard: ").title()
roaster.append(player)
player = input("Who is your shooting guard: ").title()
roaster.append(player)
player = input("Who is your small forward: ").title()
roaster.append(player)
player = input("Who is your power forward: ").title()
roaster.append(player)
player = input("Who is your center: ").title()
roaster.append(player)

#Display roaster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t" + roaster[0])
print("\t\tShooting Guard:\t\t" + roaster[1])
print("\t\tSmall Forward:\t\t" + roaster[2])
print("\t\tPower Forward:\t\t" + roaster[3])
print("\t\tCenter:\t\t\t" + roaster[4])

#Remove a injured player
injured_player = roaster.pop(2)
print("\nOh no, " + injured_player + " is injured.")

roaster_length = len(roaster)
print("Your roaster only has " + str(roaster_length) + " players.")

#Add a new player
added_player = input("Who will take " + injured_player + "'s spot: ").title()
roaster.insert(2, added_player)

#Display roaster
print("\n\tYour starting 5 for the upcoming basketball season")
print("\t\tPoint Guard:\t\t" + roaster[0])
print("\t\tShooting Guard:\t\t" + roaster[1])
print("\t\tSmall Forward:\t\t" + roaster[2])
print("\t\tPower Forward:\t\t" + roaster[3])
print("\t\tCenter:\t\t\t" + roaster[4])

print("\nGood luck " + roaster[2] + " you will be great!")
roaster_length = len(roaster)
print("Your roaster now has " + str(roaster_length) + " player.")










