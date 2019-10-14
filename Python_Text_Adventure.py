#Danimal's Text Adventure Game

#Player Name

name = raw_input("What is your name? ")

#Player Class

print "Pick a class: Warrior, Rouge, or Mage"
role = raw_input()

#Confirmation

print "Your name is %s and your role is that of a %s, correct?" % (name, role)

Continue = raw_input("Y/N? ")

if Continue == "Y":
	print "Then let us begin..."
elif Continue == "N":
	print "Then let us start from the beginning once more..."
else:
	print "You puzzle me..."
#Class Stats
class Warrior:
	HP = 250
	Mana = 50
	Speed = 1
	Attack = 25
	S_Attack = 5
	Defense = 25
	S_Defense = 5
	Starting_Gold = 200
class Rouge:
	HP = 200
	Mana = 75
	Speed = 2
	Attack = 15
	Defense = 15
	S_Attack = 10
	S_Defense = 10	
	Starting_Gold = 500
class Mage:
	HP = 150
	Mana = 100
	Speed = 1.25
	Attack = 5
	S_Attack = 25
	Defense = 5
	S_Defense = 25
	Starting_Gold = 300
#Status Menu
print "Current Status"
if role == "Warrior":
	print "HP: %d Mana: %d Gold: %d\n" % (Warrior.HP, Warrior.Mana, Warrior.Starting_Gold)
elif role == "Rouge":
	print "HP: %d Mana: %d Gold: %d\n" % (Rouge.HP, Rouge.Mana, Rouge.Starting_Gold)
elif role == "Mage":
	print "HP: %d Mana: %d Gold: %d\n" % (Mage.HP, Mage.Mana, Mage.Starting_Gold)
#ADVENTURE START
print "You begin your adventure in the town of Greenwich, a town renown for their watches and clocks."
raw_input("")
print "You were sent here on an errand for the mayor of your hometown."
raw_input("")
print "I do believe I've forgotten where you come from...\n"
#Hometown
hometown = raw_input("What was your hometown called again? ")
print "Ahhh yes... The town of %s... Twas an interesting place..." % (hometown)
if hometown == "Bruhl":
	print "Had a huge windmill and a strange tank driver and his baker girlfriend... Good times..."
elif hometown == "Atlantis":
	print "Atlantis is under the sea... Are you a ocean dweller?"
else: 
	print "I can't remember anything that interesting about it though..."
raw_input("")
#Quest 1
print "Now where were we? Right. Your story."
raw_input("")
print "You are on a mission to retreive the mayor's finished clockpiece. Now go. Get outta here.\n"
raw_input("")
choice = raw_input("Go to clocksmith to retreive the mayor's clock? ")
if choice == "yes" or "Y":
	print "Alright."
else: 
	print "What do you think you're doing, eh?"
print "The clockpiece was interesting...."
raw_input("")
print "It had an intricate design to it"
raw_input("")
print "The clockpiece had a winding swirl circling to the center as its vertex. The face and arms were revolving along the swirls as well. "
raw_input("")
print "Other than the swirls of the clockpiece there was something odd about it"
raw_input("")
print "The more you inspect you noticed there is a blue-ish aura emminating from it"
raw_input("")
print "Suddenly the arms of the clock spin rapidly and looking at it everything is starting to look blurry"
raw_input("")
print "A sudden surge of energy engulfs you..."
raw_input("")
print "Everything goes black..."
raw_input("")
print " You wake up to a dim lit forest. With a few floating lights around you and a slow growl behind you."
raw_input("")
print "Looking behind you see a humanoid tiger growling and slowly approaching you..."
choice = raw_input("Do you fight or do you flee?")
if choice == "Fight":
	print ("You stand up bravely and get ready to attack ")
elif choice == "Flee":
	print ("You get up and run as far as your legs can take you")
else:
	print ("You mind is still in a confused state, but you must choose before its too late!")
#Inventory WIP
"""print "Inventory:"
Inventory = { "knapsack": ["sword", 'dagger', 'rocks']}
for item in Inventory:
	for x in item:
		print item["x"]"""


