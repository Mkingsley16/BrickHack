#Other than your name, all inputs should be numbers. All paths lead to the same outcome but each have their own benefits.

import random
#Start Global Variables
weapon = "."
health= 20
ammo = 7
mana = 100
name = "."
buff = 0
dmgBuff = 0
surrender = 0
totalDamage = 0
lootList=["health potion", "mana potion", "bundle of arrows", "mysterious rock", "damage potion","blade enchantment" ]
itemList=[]
 #End Global Variables

def start():
    global name
    global weapon
    global itemList
    global health
    print("You wake up in a clearing inside a dark forest. Your memory is blurry.")
    name = input("What is your name? ")
    weapon = int(input("You look down, and see a 1: sword, 2: a bow, and 3: a wand, laying on the ground. Which do you pick up? "))
    if weapon == 1:
        health += 5
        weapon = "sword"
    elif weapon == 2:
        weapon = "bow"
    elif weapon == 3:
        weapon = "wand"
    bagList =[]
    for i in range(3):
        loot = random.choice(lootList)
        bagList.append(loot)
    print("Next to you is a torn bag, with a 1:", bagList[0], "a 2:", bagList[1],"a 3:",bagList[2], "in it. You can only carry one.")
    item = int(input("Which do you choose? "))
    item -=1
    itemList.append(bagList[item])
    print("You sense danger, and feel a sort of urgency creep over you.")
    direction = int(input("You see two sets of tracks leaving the clearing, to your right and to your left. Which do you follow? 1: The right tracks. 2: the left tracks "))
    if direction == 1:
        rightPath()
    elif direction == 2:
        leftPath()
#rightPath go to line 51, left path go to line 77

def rightPath():
    global weapon
    global itemList
    global health
    print("You follow the tracks until you reach a section of tall trees. On one tree you see a man with a bow begin to climb.")
    print("He spots you, drops to the ground and draw his bow.")
    combat(11,"Archer","an arrow",2,"an iron tipped arrow",4,0,1,0)
    if health > 0:
        bagList = ["health potion","damage poition"]
        print("You recognize the insignia on the Archers cape. It's the crest of the demon king. You remember now that you and your comrads were sent to kill this demon. You were injured in battle, and so they went on without you.")
        print("You begin to search the body of the Archer for any more clues.")
        bag = int(input("You find a 1: mana potion, a 2: bundle of arrows, and a 3: blade enchantment sigil. Which do you choose? "))
        if bag == 1:
            itemList.append("mana potion")
        elif bag == 2:
            itemList.append("bundle of arrows")
        elif bag == 3:
            itemList.append("blade enchantment")
        print("You continue following the tracks when you hear a gutteral roar near you. Whatever beast made it is close, and sounds angry")
        choice = int(input("Do you 1: continue foward or 2: find somewhere to hide? "))
        if choice == 1:
            beast()
        elif choice == 2:
            hide()
#beast go to line 288, hide go to line 107

def leftPath():
    global itemList
    global health
    print("You follow the tracks until they reach a river. The tracks seem to go into it, and continue on the other side. But it seems risky to cross...?")
    direction = int(input("Do you 1: turn around to follow the other set of tracks, or 2: attempt to cross the river? "))
    if direction == 1:
        wolf()
    elif direction == 2:
        print("You wade slowly into the river...")
        chanceList = [1,1,1,1,1,1,1,1,2,2,2,3,3,4]
        chance = random.choice(chanceList)
        if chance == 1:
            print("The river is flowing quickly, but you manage to cross uninjured.")
        elif chance ==2:
            print("As you cross, you feel a sharp pain in your foot. You stepped on a sharp rock and cut your toe. You take 2 damage.")
            health -= 2
            if health <=0:
                death()
            print("Your health is", health)
        elif chance ==3:
            print("The river flows too quickly for you, and it sweeps you off your feet. You manage to right yourself and get to the other side, but you dropped your",itemList[-1])
            itemList.remove(itemList[-1])
        elif chance ==4:
            print("You begin to cross, but the force of the river is too much for you. You are forced underwater, and are thrashed around until you hit the other shore.")
            health -=2
            print("You have lost 2 health and your",itemList[-1])
            itemList.remove(itemList[-1])
        scout()
#wolf go to line 219, scout go to line 227

def hide():
    global surrender
    print("You dash through the forest as quickly as you can looking for somewhere to hide. You find some form of encampment and decide to hide in there")
    print("As you enter the encapment, you see a group of soldiers with the the Demon Insignia around a fire. They haven't noticed you yet.")
    choice = int(input("Do you 1: turn around and face the wrath of the beast, or 2: take your chances fighting the enemy soldiers? "))
    if choice == 1:
        beast()
    elif choice == 2:
        surrender = 1
        infFight()
#beast go to line 288, infFight go to line 271

def castle():
    global health
    global itemList
    global buff
    print("You approach the castle cautiously. Uppon arriving, you see a gated entrance, with one guard. You think you can sneak around the side of the castle, but it'll risk certain death over the moat.")
    choice = int(input("You could 1: Fight the Guard at the door, or 2: find a way to sneak in. "))
    if choice == 1:
        castleFight()
    elif choice == 2:
        print("You slowly approach the side of the castle, and prepare to climb.")
        print("You have a 75% chance of death. You can choose to sacrifice your health, buffs or items to increase your chance of survival by 25%")
        chance = 75
        chanceList = [0,0,0,1]
        while chance >0:
            print("Current health is", str(health)+", current damage buff is", str(buff) +", and your items are", itemList)
            choice = int(input("1: to lose 5 health, 2: to -2 from your current buff, or 3: to sacrfice your held item, or 4: to take the risk"))
            if choice == 1:
                    if health - 5 <= 0:
                        print("You don't have enough health to do this!")
                    else:
                        print("You lose 5 health, and increase your chance.")
                        health -= 5
                        chance -= 25
                        chanceList.remove(0)
                        chanceList.append(1)
                    print("Chance of death is", str(chance) +"%")
            elif choice == 2:
                buff -= 2
                chance -= 25
                chanceList.remove(0)
                chanceList.append(1)
                print("You sacrifice 2 damage, and decreased your chance of death to",str(chance) +"%")
            elif choice ==3:
                if len(itemList)<0:
                    print("You have no items.")
                else:
                    print("You have the following items in on you:", itemList)
                    use = int(input("Which item would you like to sacrifice? (Press 1 for the first item, 2 for the second...) "))
                    chance -= 25
                    print("You sacrifice your", itemList[use-1], "and decrease your chance of death to", str(chance) +"%")
                    itemList.remove(itemList[use-1])
                    chanceList.remove(0)
                    chanceList.append(1)
            elif choice == 4:
                print("Your chance is", str(chance) +"%")
                print("Good luck...")
                break
        deathChance = random.choice(chanceList)
        if deathChance == 0:
            print("You werent as lucky as you thought...")
            print("You attempt to climb the side of the tower, but one of the bricks gives way. You fall down into the darkness.")
            death()
        elif deathChance == 1:
            print("Your luck and sacrifce pay off.")
            print("You climb the side of the castle tower, and are able to sneak your way into its hallways.")
            print("Down the hall, you see two large doors, the throne room. You makem your way towards them...")
            throne()
#castleFight line 249, throne line 328, death line 513

def hideout():
    print("After ten minutes of walking, you find the area of the hideout.")
    print("As soon as you enter the area, you hear a noise behind you. You turn to see a group of people all wearing the Demon Kings banner")
    print('"Surrender or die!" they shout')
    print("Fighting them would be incredible difficult, but surrendering might be just as dangerous.")
    fight = int(input("Do you 1: Fight against the onslaught or 2: Surrender yourself "))
    if fight == 1:
        infFight()
    elif fight == 2:
        print("You drop your weapon, and raise your hands to your head. They tie you up and knock you unconcious.")
        cell()
# infFight go to line 271, cell go to line 190

def cell():
    global surrender
    global health
    global weapon
    surrender = 2
    if weapon == "sword":
        health = 25
    else:
        health = 20
    print("You wake up in a small dark room. Its clearly some type of cell.")
    print("Your", weapon, " and items are on a table just within reach outside the cell door")
    print("However, the lock on the door looks rusty, and you think you can break it with a good hit. Although that would hurt.")
    choice = int(input("Do you 1: risk reaching for your weapons, or 2: Use your elbow to break the lock? "))
    if choice == 1:
        print("You reach for your", weapon, "and grab it was quickly as you can.")
        if weapon == "sword":
            print("You hit the lock with the hilt of you sword, snapping it with a loud bang.")
        elif weapon == "bow":
            print("You take the sharp edge of one of your arrows, and pry open the rusty lock.")
        elif weapon == "wand":
            print("You cast a blasting spell and blow the cell door off its hinges")
    elif choice == 2:
        print("You hit the lock with as much force as you can muster, snapping it off with a loud bang.")
        health -= 5
        print("You have", health, "health")
    mage()
# go to line 311

#All Enemies
def wolf():
    global health
    print("You walk back into the clearing where you awoke, to see a wolf snarling at you.")
    combat(10,"wolf","bite",2,"lunge",4,0,0,1)
    if health > 0:
        rightPath()
# go to line 51

def scout():
    global health
    print("You continue following the tracks away from the river until they suddenly disappear. You walk carefully.")
    print("Through the trees you see a person, and when he spots you he draws his sword")
    combat(9,"Scout","slash of his sword",3,"overhead swing of his blade",5,1,0,0)
    if health > 0:
        bagList = ["health potion","damage poition"]
        print("You recognize the insignia on the Scouts armor. It's the crest of the demon king. You remember now that you and your comrads were sent to kill this demon. You were injured in battle, and so they went on without you.")
        print("You begin to search the body of the Scout for any more clues.")
        bag = int(input("You find a 1: health potion, and a 2: damage potion. Which do you choose? "))
        if bag == 1:
            itemList.append("health potion")
        elif bag == 2:
            itemList.append("damage potion")
        print("You start towards the where you know the demon king will be, but you remember something. Your allies were going to meet not far from here. There's a good chance they've already gone to the castle of the demon king, but it might be worth it to check anyway")
        choice = int(input("Do you 1: Go straight for the castle or 2: go to your allies hideout? "))
        if choice == 1:
            castle()
        elif choice == 2:
            hideout()

# if castle go to line 119, hideout go to line 177

def castleFight():
    global health
    global itemList
    global buff
    rock = 0
    if "mysterious rock" in itemList:
        rock = 3
    print("You get as close as you can while staying hidden, then you charge into attack range!")
    combat(15,"Castle Gaurd","swing of his axe",4,"swing of his axe",5,0,1,0)
    if health >0:
        print("You rush into the castle, you make our way towards the center where you think the throne room might be.")
        print("You find two large doors, and just before you can enter, you get grabbed by a demonic beast wearing armor")
        health += 3
        combat(17-rock,"Demon Guard","a fire-infused sword",5-rock,"breath of fire",6-rock,1,0,1)
        if health >0:
            print("You search the Demon Guard as quiuckly as you can before moving deeper into the castle. He has a health potion which you quickly drink.")
            health += 10
            print("Current health is", health)
            print("The throne room is just ahead... You steel your nerves, and charge foward")
            throne()
#Go to line 328

def infFight():
    global health
    global surrender
    if surrender == 0:
        print("You turn to run through the forest, dashing through as quickly as you can")
        print("You run as far as you can, until you find yourself cornered between the river and the soldiers")
        print("You raise your weapon and prepare to face certain death")
    else:
        print("You charge at the soldiers and prepare yourself for a gruesome battle")
    while True:
        combat(random.randint(9,15),"Soldier","a slash", random.randint(2,4),"a stab",random.randint(4,6),random.randint(0,2),random.randint(0,2),random.randint(0,2))
        if surrender ==2:
            break
        else:
            print("The next soldier approaches")
#if surrender is 1, cell line 190, if 0, line 514

def beast():
    global health
    global buff
    print("You turn away from the camp, and back towards where you here the roar. You know its close. You decide its better to fight it now than get jumped by it later.")
    print("You walk to where you heard the roar, and see a hideous fourlegged animal, as large as a bear standing over a body.")
    combat(25,"Beast","slash of its claws",6,"ferocious bite",9,0,0,1)
    if health >0:
        print("You stand over the corpse of the Beast.")
        print("Fighting such a difficult foe seems to of brought back some of your skills and memory. You now remember where the Demons castle is")
        buff += 2
        health +=10
        bagList =[]
        for i in range(2):
            loot = random.choice(lootList)
            bagList.append(loot)
        print("The body of person killed by the beast has a 1:", bagList[0], "and a 2:", bagList[1] + ". You can only carry one.")
        item = int(input("Which do you choose? "))
        item -=1
        itemList.append(bagList[item])
        print("You begin your walk to the castle...")
        castle()
#go to castle line 119

def mage():
    global health
    global buff
    print("After escaping your cell, you grab the rest of your loot as quickly as possible.")
    print("You leave the cell block and make your way through what you can tell is the Demons Castle.")
    print("You find a two large doors, but before you can enter a bolt of lighting flies past your head.")
    print("You turn to see a mage with his staff raised at you.")
    combat(8,"Mage","blast of of energy",6,"wave of electricity",8,0,0,0)
    if health > 0:
        print("You quickly search the mages body, grabbing any artifact that might help you.")
        buff += 1
        health += 5
        print("You turn towards the two doors, and prepare yourself to face the Demon King")
        throne()
# go to throne line 328

#final scenario. All paths lead to this point
def throne():
    global itemList
    global health
    rock = 0
    print("You enter a large room filled with orante decorations, and crimson colored banners.")
    print("In the center stands a 7 foot tall demon, with large black horns and blood red skin.")
    print('"You will die mortal" he screams')
    if "mysterious rock" in itemList:
        rock = 3
    combat(30 - rock,"Demon King","a hell-fire sword",6 - rock,"a blast of hellish magic",9 - rock,0,1,2)
    if health >0:
        print("The King falls slowly to the ground. The castle itself seems to shake as he does. You turn to leave and put this whole ordeal behind you.")
        win()
#death or win line 532

#fighting functions
def combat(enemyHealth,enemyType,damageName1,damage1,damageName2,damage2,swordDebuff,arrowDebuff,mageDebuff):
    global weapon
    global itemList
    global health
    global ammo
    global mana
    global buff
    global dmgBuff
    global totalDamage
    print("Prepare for combat!")
    mana += 50
    if mana > 100:
        mana = 100
    tempBuff = 0
    #looped combat starts
    while health != "no" and enemyHealth != "no":
        damage = 0
        block = 0
        action = int(input("Do you want to 1: attack, 2: block, or 3: use an item? "))
        #if player attacked
        if action == 1:
            #sword
            if weapon == "sword":
                swordList = [3,4,4,4,5,5]
                if tempBuff > 0:
                    tempBuff +=1
                damage = random.choice(swordList) + buff+ tempBuff +dmgBuff -swordDebuff
                print("You swipe at the",enemyType,"with your sword. It deals", damage, "damage.")
                enemyHealth -= damage
            #bow
            elif weapon == "bow":
                if ammo > 0:
                    print("You have",ammo, " arrows left.")
                    arrowChoice = int(input("Do you use your 1: bow or 2: your knife? "))
                    if arrowChoice == 1:
                        arrowList= [6,6,7,7,8,8,8]
                        damage = random.choice(arrowList) + buff + tempBuff +dmgBuff - arrowDebuff
                        print("You aim your bow, and fire an arrow! it hits the",enemyType,"for",damage,"damage.")
                        enemyHealth -= damage
                        ammo -=1
                    elif arrowChoice ==2:
                        damage = 2+buff +tempBuff +dmgBuff
                        print("You draw your knife and stab the", enemyType, "it deals", damage, "damage")
                        enemyHealth -= damage
                else:
                    damage = 2+buff +tempBuff + dmgBuff
                    print("You draw your knife and stab the", enemyType, "it deals", damage, "damage")
                    enemyHealth -= damage
            #wand
            elif weapon == "wand":
                print("You have ", mana, "mana remaining.")
                if tempBuff >0:
                    tempBuff -=1
                if mana >=50:
                    attackChoice = int(input("Do you cast 1: Fireball for 50 mana, 2: Eldritch blast for 20 mana, or 3: a cantrip for no mana cost? "))
                elif mana >=20:
                    attackChoice = int(input("Do you cast 1: Eldritch blast for 20 mana, or 2: a cantrip for no mana cost? "))
                    attackChoice +=1
                elif mana <20:
                    attackChoice = 3
                if attackChoice ==1 and mana >= 50:
                    fireballDamage = [4,4,6,6,6,6,7,7,7,7,7,7,8,8,8,9]
                    damage = random.choice(fireballDamage) + buff +tempBuff +dmgBuff -mageDebuff
                    mana -= 50
                    print("You summon a fireball to scoarch the",enemyType +".","It deals", damage, "damage.")
                    enemyHealth -= damage
                elif attackChoice ==2 and mana >=20:
                    eldritchDamage =[2,2,4,4,4,4,4,5,5,5,7]
                    damage = random.choice(eldritchDamage) + buff +tempBuff +dmgBuff - mageDebuff
                    mana -=20
                    print("You cast eldritch lightning towards the",enemyType + ".","It deals",damage,"damage.")
                    enemyHealth-= damage
                else:
                    mana +=10
                    cantripList = ["a collum of fire.","a bolt of lightning.","a volley of icicles.", "a mote of light.", "a slash of darkness"]
                    cantrip = random.choice(cantripList)
                    damage = 2 + buff +tempBuff+ dmgBuff- mageDebuff
                    if damage <=0:
                        damage = 1
                    print("You attack the", enemyType, "with", cantrip, "It deals",damage, "damage.")
                    enemyHealth -= damage
            tempBuff = 0
        #block
        elif action == 2:
            tempBuff =3
            block = random.randint(damage1-1,damage2-1)
            print("You block", block, "damage from the",enemyType +"'s attack, and are prepped for more damage.")
        #item
        elif action == 3:
            itemUse()
            block = damage2
        elif action != 1 or action != 2 or action != 3:
            print("Please choose a valid input. Enemy Attack will be blocked.")
            block = damage2
        totalDamage+=damage
        #Now the enemy attacks
        if enemyHealth > 0:
            enemyAttack = random.randint(0,6)
            if enemyAttack <=4:
                damage = damage1 - block
                if damage <0:
                    damage = 0
                print("The", enemyType,"attacks you with a", damageName1 +". It deals", damage,"damage to you.")
                health -= damage
            elif enemyAttack >4:
                damage =damage2 -block
                if damage <0:
                    damage = 0
                print("The", enemyType,"attacks you with a", damageName2 +". It deals", damage,"damage to you.")
                health -= damage
        if health <= 0:
            health = "no"
        if enemyHealth <= 0:
            enemyHealth = "no"
        print("You have",health,"health remaining.")
        print("The",enemyType,"has",enemyHealth, "health remaining.")
    if health <=0:
        death()              
    else:
        dmgBuff =0
        print("You have slain the",enemyType+ "!")
        input("Enter any key to continue: ")
#If combat won, continue inside the calling function

def itemUse():
    global weapon
    global itemList
    global health
    global ammo
    global mana
    global buff
    global dmgBuff
    if len(itemList)<=0:
        print("You have no items.")
    else:
        print("You have the following items in on you:", itemList)
        use = int(input("Which item would you like to use? (Press 0 to exit, Press 1 for the first item, 2 for the second...) "))
        if use == 0:
            print("You return to combat")
        else:
            if use <= len(itemList):
                itemUsed = itemList[use -1]
                itemList.remove(itemList[use-1])
                if itemUsed == "health potion":
                    print("You drink the potion, and instantly feel restored.")
                    health += 10
                    print("You now have", health, "health.")
                elif itemUsed == "mana potion":
                    if weapon == "wand":
                        print("You drink the potion, and instantly feel invigorated.")
                        mana += 100
                        print("You now have",mana,"mana.")
                    else:
                        print("You drink the potion, but nothing seems to happen. Perhaps it wasnt meant for you...")
                elif itemUsed == "bundle of arrows":
                    if weapon == "bow":
                        print("You unwrap the arrows and place them into your quiver.")
                        ammo += 5
                        print("You now have", ammo,"arrows.")
                    else:
                        print("Arrows are useless to you without a bow.")
                elif itemUsed == "mysterious rock":
                    print("The rock tingles strangley in the palm of your hand. You feel that it's aura empowers you against demons")
                    itemList.append("mysterious rock")
                elif itemUsed == "damage potion":
                    print("You drink the potion, and instantly feel empowered.")
                    dmgBuff +=4
                    buff +=1
                    print("You now deal a bonus 5 damage on each attack")
                elif itemUsed =="blade enchantment":
                    if weapon == "sword":
                        print("You empower your sword with magic, causing it to deal more damage")
                        buff +=1
            else:
                print("Invalid input")
                itemUse()
#return to combat function

def death():
    global name
    global weapon
    global surrender
    global totalDamage
    if surrender == 1:
        print("You fought as hard as you could, but couldnt win. You collapse to the ground and lose conciousness.")
        cell()
    else:
        for i in range(10):
            print(".")
        print("You have been killed...")
        print("You used the", weapon+ ", and dealt a toal of",totalDamage,"damage.")
        print("That was a great try", name+". Play again sometime!")
    surrender = 2
#If surrender is 1, go to cell line 190
#if surrender is 0, end of program

def win():
    global name
    global weapon
    global health
    global totalDamage
    global surrender
    surrender = 2
    print("Congratulations", name+ ", You beat the game!")
    print("You used the", weapon + ", dealt a total of", totalDamage,"damage, and ended with", health, "health.")
    print("Feel free to try again and take a different path, or try a different weapon.")
#End of program

start()