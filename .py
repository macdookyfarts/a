import random
#This is spaggehti code
#YOU HAVE BEEN WARNED 

PlayerDict = {"PlayerHp": 30}
enemydict1 = {"name": "other worldly being", "monsterhp": 20} #No damage here because that means it gets picked once
enemydict2 = {"name": "reanimated solider", "monsterhp": 25}
def inv():
    print("This is the inventory.") #THIS
    invList=['apple', 'health potion']
    print(invList)
    prompt()
def prompt():
    prompt = input("Enter a one of the following: interact, pick up, check inventory.\npick one: ")
    if prompt == "interact":
        interact = input("What would you like to interact with?")#

    elif prompt == "pick up":
        if SecondCha==True:
            ListItems2 = ["loose stones"]
        elif ThirdCha==True:
            ListItems3 = ["bow"]
        
            
            
        pickup = input("What would you like to pick up?")#same here
        if SecondCha==True:
            print("ur mom")
            
    elif prompt == "check inventory":
        print("test inv")
        inv()
   	 
def combat():
    
    print("You have engaged combat with a", (enemydict1["name"]), ".")
    print("How will you fight this creature?")
    Turn1=0
    while (enemydict1["monsterhp"]) > 0: #THIS IS THE LOOP THAT WORKS
        if Turn1==1: #Bug with block that it does normal attack after
             print("The monster pounces on you, dealing ", SpecialDam)
             (PlayerDict["PlayerHp"]) -= SpecialDam #Special Damage
             Turn1=2
            
        MonsterDam1 = (random.randint(1, 3))
        SpecialRoll = (random.randint(1, 10)) # Special Attack 10% chance
        if SpecialRoll == 1:
            print("The creature jolts back, preparing to jump onto you.")
            SpecialDam = (random.randint(3, 6))
            
            Turn1=1
        if Turn1==0: #After Blocking Cant deal damage
            (PlayerDict["PlayerHp"]) -= MonsterDam1 #Monster Damage
            print ("The creature has attacked you for", MonsterDam1, "\nYour total hitpoints are", (PlayerDict["PlayerHp"])) #add various phrases eg "the monster slashed you" "the monster stabbed you"
        
        if (PlayerDict["PlayerHp"]) < 0:
            print("You have died, no one can stop the king's rule.")
            exit() #implement this better? perhasps checkpoints?
            
        combat = input("Your options are: attack, heal, block.\nYou choose: ")
        if combat == "attack":
            roll = (random.randint(0, 6))
            if roll == 0:
                print("You missed lol.")
            else:
                enemydict1["monsterhp"] -= roll
                print("You got a hit of", roll)
                print("The Monster's health is",(enemydict1["monsterhp"]))
                if (enemydict1["monsterhp"]) <= 0: #above zero keep doing combat  
                    print("You have slain the creature, your victory is great!\n")
                    (PlayerDict["PlayerHp"]) = 30 # Resets health after battle
                    
        elif combat == "heal": #Add player hp cap, you can heal infinitely atm
            rollheal = (random.randint(3, 8))
            (PlayerDict["PlayerHp"]) += rollheal
            print("You have healed", rollheal, "\nYour current health is", (PlayerDict["PlayerHp"]))
            
        elif combat == "block":
            if Turn1==1:
                print("You successfully block the monster's attack, you deflect the damage.")
                Turn1=2
            if Turn1==0:
                MonsterDam1 / 2 #only gonna be useful if it winds up for a big attack
        else:
            print("Invalid option, check for mistakes.")
            r = (random.randint(1,20))
            if r == 1:
                print("\nType correctly ya oaf.\n")
def combat2():
    print("You have engaged combat with a ", (enemydict2["name"]), ".")
    print("How will you fight this creature?")
    Turn1=0
    while (enemydict2["monsterhp"]) > 0: #THIS IS THE LOOP THAT WORKS
        if Turn1==1:
             print("The monster slashes you, dealing ", SpecialDam)
             (PlayerDict["PlayerHp"]) -= SpecialDam #Special Damage
             Turn1=2
            
        MonsterDam2 = (random.randint(2, 5))
        SpecialRoll = (random.randint(1, 10)) # Special Attack 10% chance
        if SpecialRoll == 1:
            print("The creature jolts back, winding up for a big swing.")
            SpecialDam = (random.randint(3, 6))
            
            Turn1=1
        if Turn1==0: #After Blocking Cant deal damage Because it like never = 0.
            (PlayerDict["PlayerHp"]) -= MonsterDam2 #Monster Damage
            print ("The creature has attacked you for", MonsterDam2, "\nYour total hitpoints are", (PlayerDict["PlayerHp"])) #add various phrases eg "the monster slashed you" "the monster stabbed you"
        
        
        if (PlayerDict["PlayerHp"]) < 0:
            print("You have died, no one can stop the king's rule.")
            exit() #implement this better? perhasps checkpoints?
            
        combat = input("Your options are: attack, heal, block.\nYou choose: ")
        if combat == "attack":
            roll = (random.randint(0, 7))
            if roll == 0:
                print("You missed lol.")
            else:
                enemydict2["monsterhp"] -= roll
                print("You got a hit of", roll)
                print("The Monster's health is",(enemydict2["monsterhp"]))
                if (enemydict2["monsterhp"]) <= 0: #above zero keep doing combat  
                    print("You have slain the creature, your victory is great!\n")
                    (PlayerDict["PlayerHp"]) = 30 # Resets health after battle
                    
        elif combat == "heal": #Add player hp cap, you can heal infinitely atm
            rollheal = (random.randint(3, 8))
            (PlayerDict["PlayerHp"]) += rollheal
            print("You have healed", rollheal, "\nYour current health is", (PlayerDict["PlayerHp"]))
            
        elif combat == "block":
            if Turn1==1:
                print("You successfully parry the monster's sword, you deflect the damage.")
                Turn1=0
            if Turn1==0:
                MonsterDam2 / 2 #only gonna be useful if it winds up for a big attack
        else:
            print("Invalid option, check for mistakes.")
            r = (random.randint(1,20))
            if r == 1:
                print("\nType correctly ya oaf.\n")


print("Welcome to the land of adventure.\nYou will go through a range of trials and tribulations.")
UserInp = 0
while UserInp != "Y" and UserInp != "N":
    UserInp = input("Would you like a tutorial? Enter Y or N: ")
    if UserInp == "Y":
        print("You have selected the tutorial! The basic interactions are: interact, pick up, inventory check\nThe combat interactions are: attack, heal and block.\nAttacks are your main way of delievering damage.\nHeal heals your character.\nBlock halves the incoming damage, and completely negates special attacks.\n")
    elif UserInp == "N":
        print("Alright, you'll skip straight to the adventure then.\n")
    else:
        print("Invalid option.")

print("-------------------\n The First Chapter \n-------------------\n")
FirstCha=True #can only interact with things available in that chapter
print("A towering castle looms in the distance, the air is full of fumes and the ashes of battle.\nBefore you stands a forest, the only way through to the tyranical king.\nYou are alone, your comrades injured or dead by those beasts.\nThose beasts are no match for your might, and the forest is plentyful of them.\nYou must fight!\n")
print("A four legged beast reveals itself, you've seen this monster before in battle but, it is not of this world.")
combat()
FirstCha=False
print("--------------------\n The Second Chapter \n--------------------\n") #Work In Progress
SecondCha=True
print("You have made it through the forest, the beasts were no match for you.")
print("Before you stands the castle, fires and loose stones torn about the wall.") #Commit your entire life to picking up loose stones as a joke ending
print("With no way through you must figure out a way to get inside.")
prompt() 

WayThrough = "A" # DO stuff with this
SecondCha=False
print("-------------------\n The Third Chapter \n-------------------\n")
ThirdCha=True
#depending on how you get through writing changes
if WayThrough == "A":
	print("You made it through by climbing the wall.\nLongbowmen litter the wall, corpses are littered about the courtyard.\nSome guards are still loyal to their king, even with this current devastation.\nA few become reanimated, devoid of emotion and soul.")
	combat2() #attacking reanimated soliders
elif WayThrough == "B":
    print("You made it through by crawling through the sewer.\nYou suffer from the foul stench.\n")
ThirdCha=False
print("----------------\n The Great Hall \n----------------\n") #add story idk
FourthCha=True
print("The Great Hall stands before you, surely the king has made some pact with some devil.\nAll these supernatural creatures, there is no logical way these are natural.\n")

combat()
print("The King slouches on the grand throne posed cocky and arrogant.\nHis face is obscured by a hood.\nWithout heisitation you charge onward, your sword plunges into the kings chest.\nBlood seeps out, his lifeless body goes limp.\n")
#Ok i could do twist final boss fight or hes just actually dead
#with the way this is going i'll add a boss fight last
print("-----------\n The End \n-----------\n")
FourthCha=False
