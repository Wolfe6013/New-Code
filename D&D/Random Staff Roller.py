import random
import time

d4 = random.randint(1,4)
d100 = random.randint(1,100)
#d4 = 3
#d100 = 5

answerd3 = random.randint(1,3)
answerd4 = random.randint(1,4)
answerd6 = random.randint(1,6)
answerd8 = random.randint(1,8)
answerd9 = random.randint(1,9)
answerd10 = random.randint(1,10)
answerd12 = random.randint(1,12)

if d4 == 4:
    print('You got a 4, and nothing happens...')
else:
    print("You got",d4,"and",d100,)   
if d4 == 1:
    if d100 == 1:
        print("Every creature within 10ft loses their legs for 10 minutes.")
    if d100 == 2:
        print("A giant snail appears in the nearest unoccupied space.")
    if d100 == 3:
        print("Every creature within 15ft loses 5ft of move speed but gets advantage on all charisma checks for an hour, as a fancy suit/dress (their choosing) appears on their body.")
    if d100 == 4:
        print("The target turns invisible to everyone except the caster/attacker.")
    if d100 == 5:
        print("Every creature within 10ft must make a DC25 wisdom save or turn into a giant panda.")
    if d100 == 6:
        print("The target and the caster/attacker must make a DC20 dexterity save or be trapped in a painting depicting their fight until the end of their next turn. In the painting, you are considered restrained and have a movement speed of zero.")
    if d100 == 7:
        print("A portal appears, sucking every creature within 20ft into it for an hour. Inside the portal is an infinite 5ft deep pool.")
    if d100 == 8:
        print("A portal appears, sucking every creature within 20ft into it for an hour. Inside the portal is an infinite maze.")
    if d100 == 9:
        print("A portal appears, sucking every creature within 20ft into it for an hour. Inside the portal is an infinite swamp.")
    if d100 == 10:
        print("A portal appears, sucking every creature within 20ft into it for an hour. Inside the portal is an infinite 2d parkour game.")
    if d100 == 11:
        print("A Blue, Red, Green and White Dragon Wyrmling appear and play with each other, and with whoever else wants to.")
        if answerd4 == 1:
            print("The Blue Dragon Wyrmling is evil, and is plotting to kill everyone")
        if answerd4 == 2:
            print("The Red Dragon Wyrmling is evil, and is plotting to kill everyone")
        if answerd4 == 3:
            print("The Green Dragon Wyrmling is evil, and is plotting to kill everyone")
        if answerd4 == 4:
            print("The White Dragon Wyrmling is evil, and is plotting to kill everyone")
    if d100 == 12:
        print("A platform pushes everyone within melee range 10ft up into the air.")
    if d100 == 13:
        print("For one minute, any flammable objects you touch burst up into flames (dealing",answerd4,"fire damage).")
    if d100 == 14:
        print("Your mouth disappears, so you cannot speak or use verbal components for one minute.")
    if d100 == 15:
        print("A ghost follows you around, saying insults to you and everyone you pass.")
    if d100 == 16:
        print("Your eyes permanently become either red, yellow, purple, black, white, or invisible (wish spell or remove curse removes this effect).")
    if d100 == 17:
        print(answerd4*2,"Birds land on your shoulders and head and chirp. You have a -5 to your stealth for 10 minutes, or until all the birds die. The birds have an AC of 12 and 10 hit points. All damage dealt to them deals damage to the attacker as well.")
    if d100 == 18:
        print("You have a vision of you dying (may not actually happen).")
    if d100 == 19:
        print("All plants within 20ft shoot up and grow 100x the speed they usually would, and 30 seconds later, wilt and die.")
    if d100 == 20:
        print("The target turns into a marble statue for one minute. The creature gets a +5 to its AC and immunity to all damage except physcic for this time.")
    if d100 == 21:
        print("For the next 10 minutes, you and the target must speak like a snake.")
    if d100 == 22:
        print("The target must make a DC15 save or turn into a cat for one minute.")
    if d100 == 23:
        print("A magic mouth appears on the nearest wall/tree for the next hour and whenever you speak, the mouth says those words too.")
    if d100 == 24:
        print("Everything your target says is 10x louder.")
    if d100 == 25:
        print("The target turns into a potted plant for one minute. Breaking the pot (AC 10,",answerd4*5,"hp) stops this effect early.")
    if d100 == 26:
        print("A giant, floating eye appears, which you can see through for one minute. The eye has a flying speed of 60ft. While this effect is active, you cannot see through your own eyes.")
    if d100 == 27:
        print("A anti-magic field appears, centred on you for an hour.")
    if d100 == 28:
        print("Mushrooms appear at your feet. Make a DC 15 constitution save or take 10 necrotic damage, healing 10 hp on a success.")
    if d100 == 29:
        print("Flashing, colourful lights appear in a 10ft diameter circle, centred on you for a minute. Every creature starting their turn in this area must make a DC 15 constitution save or be blinded until the start of their next turn.")
    if d100 == 30:
        print("You are illiterate for the next hour.")
    if d100 == 31:
        print("Everyone within 10ft including you must make a DC 15 wisdom save or fall asleep (a creature that cannot be put to sleep takes",answerd4,"psychic damage on a fail).")
    if d100 == 32:
        print("Exactly 100 gallons of milk drop from the sky, dealing",answerd4+2,"magical bludgeoning damage and making everyone's hair reach toward the nearest light source.")
    if d100 == 33:
        print("If the caster/attacker dies within the next minute, they wake up on their next turn, with 1 hit point.")
    if d100 == 34:
        print("A skeleton horse appears as the mount for the caster/attacker for one week.")
    if d100 == 35:
        print("The caster/attacker has their alignment change for",answerd4,"days.")
        if answerd9 == 1:
            print("Your alignment becomes Lawful Good.")
        if answerd9 == 2:
            print("Your alignment becomes Neutral Good.")
        if answerd9 == 3:
            print("Your alignment becomes Chaotic Good.")
        if answerd9 == 4:
            print("Your alignment becomes Lawful Neutral.")
        if answerd9 == 5:
            print("Your alignment becomes True Neutral.")
        if answerd9 == 6:
            print("Your alignment becomes Chaotic Neutral.")
        if answerd9 == 7:
            print("Your alignment becomes Lawful Evil.")
        if answerd9 == 8:
            print("Your alignment becomes Neutral Evil.")
        if answerd9 == 9:
            print("Your alignment becomes Chaotic Evil.")
    if d100 == 36:
        print("The next time need to use this table, roll",answerd4,"times.")
    if d100 == 37:
        print("It starts to rain your urine.")
    if d100 == 38:
        print("The target transforms into a chest mimic for one minute, or until slain.")
    if d100 == 39:
        print("The staff turns into a snake and attacks the caster/attacker.")
    if d100 == 40:
        print("A pack of 5 dire wolves appear and are:")
        time.sleep(0.5)
        if answerd4 <= 2:
            print("hostile to the target!")
        if answerd4 >= 3:
            print("hostile to the attacker/caster!")
    if d100 == 41:
        print("A 20ft sphere of fog appears centred on you. Everything in this area is heavily obscured.")
    if d100 == 42:
        print("A cloud follows, 5ft above you, and rains on you. The rain goes through objects, but still soaks your clothes and you.")
    if d100 == 43:
        print("5 illusionary duplicates of the target appear. When attacking the target, roll a d6. on a 6 they hit the correct target. When a false target is hit, it disappears.")
    if d100 == 44:
        print("Any nearby plants attack the target (awakened bush/tree).")
    if d100 == 45:
        print("A random creature within 20ft gains a fly speed of 50 for the next 10 minutes. The caster/attacker and the target of the attack can't get this fly speed. If a creature already has a fly speed, it is increased by 30ft instead.")
    if d100 == 46:
        print("A lake appears, roughly 100ft by 100ft centred on you with",answerd9+answerd4,"small islands on it (explorable) for an hour.")
    if d100 == 47:
        print("A small Japanese pond (10ft by 10ft) appears permanently below you and your target.")
    if d100 == 48:
        print("A coil of rope appears and ties you to your target (DC15 to escape) and you are now both restrained. Escaping frees the other person too.")
    if d100 == 49:
        print("You and the target switch bodies. You are now in their body. As soon as one person gets reduced to 0 hit points then you swap bodies back, and regain",answerd4,"/4 of the damage your body took.")
    if d100 == 50:
        print("An Almiraj appears in the nearest unoccupied space for a week (unless you cast find familiar on it)")
        if answerd4 <= 2:
            print("It is loyal to the target")
        if answerd4 >= 3:
            print("It is loyal to you")
    if d100 == 51:
        print("Everything you eat for the next 48 hours tastes like soap")
    if d100 == 52:
        print("Everyone you have killed in the past minute comes back to life as a zombie")
    if d100 == 53:
        print("All your hair falls out. In 5 minutes it will grow back exactly how it was before")
    if d100 == 54:
        print("A demon (level appropriate) appears.")
        if answerd4 <= 2:
            print("It wants to kill you")
        if answerd4 >= 3:
            print("It wants to kill your target")
    if d100 == 55:
        print("You get sent to the astral plane for one minute. If you are already in the astral plane, nothing happens")
    if d100 == 56:
        print("Your target and the furthest creature away from you within 100ft swap places")
    if d100 == 57:
        print("Next time you speak a burst of fire shoots out of your mouth. It has the stats of a Adult Red Dragon's fire breath, only it deals",answerd6^2+answerd4,"fire damage")
    if d100 == 58:
        print("You get trapped in a cocoon. You are restrained, you are considered to be in total cover and can't attack. You get freed if the cocoon takes more than 15 damage (AC 10)")
    if d100 == 59:
        print("Cabbages sprout out the ground in a 15ft radius centred on you. This area is considered difficult terrain")
    if d100 == 60:
        print("Everyone within 10ft of you (including you) must make a DC 15 constitution save or takes 4 fire damage, taking half on a success, as the area heats up dramatically")
    if d100 == 61:
        print(answerd4+4,"doors appear, 10ft away from you, scattered apart for an hour. Heading through one door leads to another. When opening the door, roll a d6 to decide which door it goes to (it can lead to itself)")
    if d100 == 62:
        print(answerd6*2,"zombies pull themselves out of the ground, prone and are aggressive to every creature around them (except each other)")
    if d100 == 63:
        print(answerd4+1,"spectres appear, and are aggressive to every creature around them (except each other)")
    if d100 == 64:
        print("The target must make a DC 15 wisdom saving throw or turn into a lion for 10 minutes. It can retry the save every turn after the first")
    if d100 == 65:
        print("A banquet appears on a huge banquet table fit for a king for 24 hours. Eating food from the table gives you",answerd4*2,"temporary hit points")
    if d100 == 66:
        print("The target becomes magnetic until the end of their next turn. Every metal object within 10ft gets sucked toward them, dealing",answerd4*2,"bludgeoning damage per object. Anyone can make a DC 15 strength check to try and hold on to their objects. Any attack made with a metal weapon against the target during this time has advantage and deals an extra",answerd4,"damage, as the weapon naturally goes toward them")
    if d100 == 67:
        print("A glass case (10ft by 10ft) rises from the ground. Inside is",answerd4*3,"skeletons. The glass needs to take 10 damage to shatter (AC 12) and when it does, whoever is within 5ft takes",answerd4+1,"piercing damage, as the glass pierces their flesh. The skeletons are immune to this damage.")
    if d100 == 68:
        print("Next time the attacker/caster goes within 20ft of water, a large Viking longboat appears, devoid of crew but with loot")
    if d100 == 69:
        print("A grandfather clock appears and starts donging loudly and can be heard from 50ft away (if it has a path there). The clock has 25 hit points and every 5 hit points delt to it reduces the distance heard by 10ft (AC 14)")
    if d100 == 70:
        print("Every creature within 50ft of the attacker/caster must make a DC 20 wisdom save or forget every interaction they have ever had with them for 10 minutes")
    if d100 == 71:
        print("A bush appears in the closest unoccupied space near you. Roll a d4 for each person to decide one of these effects; either they are afraid of the bush, suspicious of the bush, fine with the bush or believe that they have been friends with the bush for many years. The effects wear off slowly over 10 minutes")
    if d100 == 72:
        print("You can only speak in gibberish for the next 10 minutes")
    if d100 == 73:
        print("In",answerd4,"hours, roll on this table again and again until something happens, with the attacker/caster also being the target")
    if d100 == 74:
        print("The air around you becomes super thick and you cannot breath for",answerd4*2,"minutes")
    if d100 == 75:
        print("A giant tree appears in the nearest unoccupied space (15ft by 15ft) and grows up 100ft. In 30 seconds or on your next turn (whichever is first) it will start to rain giant acorns. At the start of everyone's turns, they must make a DC 17 dexterity save or get hit by one, taking",answerd4,"bludgeoning damage. Failing by 5 makes you get hit by two and failing by 10 makes you get hit by 3. Failing by 15 makes you take",answerd4*8,"bludgeoning damage")
    if d100 == 76:
        print("Next time the attacker/caster walks through a door,",answerd4*3,"cats will follow them for the next",answerd4,"hours.")
    if d100 == 77:
        print("Next time the attacker/caster walks through the door, the door will slam them in the face, dealing 1 bludgeoning damage and 1 embarrassing damage.")
    if d100 == 78:
        print("An illusion makes it appear as though the ceiling/sky is collapsing on you. DC 20 investigation check to discern the ruse. If you touch it the illusion ends.")
    if d100 == 79:
        print("Everyone within 20ft have an irresistible urge to either, if they are outside, get inside, or if they are inside, get outside.")
    if d100 == 80:
        print("For the next",answerd4*2,"weeks your reflection doesn't follow you, but acts upon its own free will. Roll a d4. On a 1-2 the reflection is actually a Night Hag. She will work to slowly get you to free her. You can free her by splashing your reflection with holy water and saying, 'I unbind thee from my service!' The hag knows this. She will reveal her true form and attack the moment you save her. On a 3-4 it is a Celestial. The Celestial will help you but if you do an evil act then they will mislead you. It can hear you but cannot speak. If can write to you by fogging up the reflection, as if it is a reflection in a mirror. The reflections both know what you have done since they existed and know the best way to help you, although the Celestial will say it all cryptically and the Night Hag will mislead you.")
    if d100 == 81:
        print("Every tree within 50ft starts to grow different fruit. Picking the fruit off the tree will result in the fruit vanishing after 1d4 minutes. If the fruit are eaten, the eater heals 2d4 and next time they attack, have them roll on this table.")
    if d100 == 82:
        print("A magic, glass elevator appears. Going into it and pressing the button will have you go straight up, passing through solid objects. When you have gone up 200ft, the elevator will stop and stay there. If you press the button again, the elevator will disappear and you will fall back down super-fast and just before you hit the ground, it will re-appear below you, land and make a ding sound.")
    if d100 == 83:
        print("The nearest wall appears to have disappeared. When you try to walk through it, you will bump into it and you will hear a cackling noise. Everyone else will not hear the noise and see you go through the wall. After bumping into the wall you can see everyone else that has as well, and see through the illusion.")
    if d100 == 84:
        print("Any dirt in a 20ft circle, centred on you turns to dirt for 1d4 minutes.")
    if d100 == 85:
        print("A 10ft wide, 20ft tall tower appears with a spiral staircase inside it. At the top of the staircase is a painting. The person in the painting moves, and says, 'haha, you just wasted your time!' Taking the painting off the wall reveals a chest. In the chest is",answerd4+1,"poisonous snakes and 4d10 silver pieces.")
    if d100 == 86:
        print("A random nearby object turns into a mimic.")
    if d100 == 87:
        print("A glass pane appears 10ft above you and falls down. Everyone within 10ft must make a Dexterity save or take 3d8 piercing damage, taking half on a success as it shatters everywhere.")
    if d100 == 88:
        print(answerd4,"chain devils appear and attack you, disappearing in",14-answerd4*3,"rounds (not their rounds, just rounds total).")
    if d100 == 89:
        print(answerd4,"chain devils appear and attack your target, disappearing in",14-answerd4*3,"rounds (not their rounds, just rounds total).")
    if d100 == 90:
        print("A trapdoor appears in the nearest unoccupied space near you. Going into the trapdoor brings you to a demiplane, but all that is there is a plain concrete room, 50ft by 50ft and 10ft tall.")
    if d100 == 91:
        print("A random person within 20ft becomes hostile to the target (the target can be that person)")
    if d100 == 92:
        print("A random person within 20ft becomes charmed by the target.")
    if d100 == 93:
        print("A random person within 20ft becomes hostile to you (you can be that person).")
    if d100 == 94:
        print("A random person within 20ft becomes charmed to you.")
    if d100 == 95:
        print("Next time you attack, the target heals instead of taking damage.")
    if d100 == 96:
        print("Next attack you make, you heal the amount of damage you dealt.")
    if d100 == 97:
        print("Next attack you make, you take half the damage you deal.")
    if d100 == 98:
        print("A table falls from the sky and everyone, one their turn, must use their action and their move speed to stand on the table. Once they have stood on the table they heal 1 hit point.")
    if d100 == 99:
        print("A potion appears. There is enough liquid in it for 1d4+2 drinks. Every time you drink this potion, roll on this table again. If it requires a target, it triggers as soon as you make an attack..")
    if d100 == 100:
        print("You deal an extra 4d4 necrotic damage.")

if d4 == 2:
    if d100 == 1:
        print("Gravity reverts in a 10ft sphere, centred on you, for everyone except you")
    if d100 == 2:
        print("A small red ball appears and bounces, trying to hit every creature with 50ft of you in the face, healing 1 hit point. After doing so on all creatures, the ball disappears. Any creature hit by the ball becomes super happy, and can't get a grin off their face for an hour")
    if d100 == 3:
        print("You gain resistance to a random type of damage for one minute. The damage type is...")
        if answerd12 == 1:
            print("Acid!")
        if answerd12 == 2:
            print("Cold!")
        if answerd12 == 3:
            print("Fire!")
        if answerd12 == 4:
            print("Psychic!")
        if answerd12 == 5:
            print("Lightning!")
        if answerd12 == 6:
            print("Necrotic!")
        if answerd12 == 7:
            print("Poison!")
        if answerd12 == 8:
            print("Radiant!")
        if answerd12 == 9:
            print("Thunder!")
        if answerd12 == 10:
            print("Bludgeoning!")
        if answerd12 == 11:
            print("Slashing!")
        if answerd12 == 12:
            print("Piercing!")
    if d100 == 4:
        print("Your target gains resistance to a random type of damage for one minute. The damage type is...")
        if answerd12 == 1:
            print("Acid!")
        if answerd12 == 2:
            print("Cold!")
        if answerd12 == 3:
            print("Fire!")
        if answerd12 == 4:
            print("Psychic!")
        if answerd12 == 5:
            print("Lightning!")
        if answerd12 == 6:
            print("Necrotic!")
        if answerd12 == 7:
            print("Poison!")
        if answerd12 == 8:
            print("Radiant!")
        if answerd12 == 9:
            print("Thunder!")
        if answerd12 == 10:
            print("Bludgeoning!")
        if answerd12 == 11:
            print("Slashing!")
        if answerd12 == 12:
            print("Piercing!")
    if d100 == 5:
        print("You gain vunrability to a random type of damage for one minute. The damage type is...")
        if answerd12 == 1:
            print("Acid!")
        if answerd12 == 2:
            print("Cold!")
        if answerd12 == 3:
            print("Fire!")
        if answerd12 == 4:
            print("Psychic!")
        if answerd12 == 5:
            print("Lightning!")
        if answerd12 == 6:
            print("Necrotic!")
        if answerd12 == 7:
            print("Poison!")
        if answerd12 == 8:
            print("Radiant!")
        if answerd12 == 9:
            print("Thunder!")
        if answerd12 == 10:
            print("Bludgeoning!")
        if answerd12 == 11:
            print("Slashing!")
        if answerd12 == 12:
            print("Piercing!")
    if d100 == 6:
        print("Your target gains vunrability to a random type of damage for one minute. The damage type is...")
        if answerd12 == 1:
            print("Acid!")
        if answerd12 == 2:
            print("Cold!")
        if answerd12 == 3:
            print("Fire!")
        if answerd12 == 4:
            print("Psychic!")
        if answerd12 == 5:
            print("Lightning!")
        if answerd12 == 6:
            print("Necrotic!")
        if answerd12 == 7:
            print("Poison!")
        if answerd12 == 8:
            print("Radiant!")
        if answerd12 == 9:
            print("Thunder!")
        if answerd12 == 10:
            print("Bludgeoning!")
        if answerd12 == 11:
            print("Slashing!")
        if answerd12 == 12:
            print("Piercing!")
    if d100 == 7:
        print("One mile by one mile centred on you, it will start to snow, and it will keep snowing for a week. It is a light snow, not heavy and it doesn't make the area super cold")
    if d100 == 8:
        print("One mile by one mile centred on you, it starts to rain bowls of soup that doesn't burn you. It stops raining the soup after 10 minutes")
    if d100 == 9:
        print("A 20ft long, 20ft high, picket fence appears between you and your target")
    if d100 == 10:
        print("You cast shockwave at first level without using a spell slot.")
    if d100 == 11:
        print("Your target cast shockwave at first level without using a spell slot.")
    if d100 == 12:
        print("You have to commentate what is happening around you for one minute or take",answerd4,"psychic damage.")
    if d100 == 13:
        print("You have the sudden realisation that all of this might just be a game to entertain people. After an hour you realise the flaw in your thought, that nobody would every want to play as someone like you.")
    if d100 == 14:
        print("Your shadow stops following you and attacks the target every turn for 1 minute.")
    if d100 == 15:
        print("Your targets shadow stops following them and attacks whatever they attack every turn for 1 minute.")
    if d100 == 16:
        print("You highest stat and your lowest stat swap for an hour.")
    if d100 == 17:
        print("In one minute,",answerd4*2+1,"orcs and an orc chieftain will charge through the bushes, attacking everyone hostile to your target")
    if d100 == 18:
        print("You are cursed with Lycanthrope. During the next full moon you will turn into a werewolf with half the usual hit points. Being reduced to zero hit points as a werewolf, you will wake up as if you just long rested. After you have been killed as a werewolf, you will never become one again.")
    if d100 == 19:
        print("Classical music starts playing from where you are.")
    if d100 == 20:
        print("Everyone within 30ft turns invisible for a minute or until they attack or cast a spell.")
    if d100 == 21:
        print("Everything but your head turns invisible for",answerd4*2+answerd6+1,"minutes.")
    if d100 == 22:
        print("You lose control of your arm and it becomes sentient, doing whatever it likes for the next hour.")
    if d100 == 23:
        print("A sassy Lich follows you around and wants you to become a warlock using its power and won't leave until you say yes, and upon doing so, it will say, 'haha, jk!' and teleport away. If they attack the Lich it will not fight back")
    if d100 == 24:
        print("The attacker/casters thinks they are a frog, and acts like a frog for 10 minutes.")
    if d100 == 25:
        print("Your mind gets taken over by a god for 3 days.")
    if d100 == 26:
        print("Your mind gets taken over by an old dragon for 3 days")
    if d100 == 27:
        print("You believe that a random one of your party members are conspiring against you.")
    if d100 == 28:
        print("You and the target get teleported to an underground room and suffer from horrible hallucinations for one hour. After the hour, you are teleported back to your exact position. If something else is there,  both things take 5d12 bludgeoning damage and get moved to the nearest unoccupied space.")
    if d100 == 29:
        print("A swarm of",answerd4*5,"bats appear and attack you.")
    if d100 == 30:
        print("A swarm of",answerd4*5,"bats appear and attack your target.")
    if d100 == 31:
        print("A peasant shows up and challenges the party to a friendly battle (not to the death). The 'peasant' is a level 20 paladin with the sword of zariel.")
    if d100 == 32:
        print("Next time you long rest, everyone within 30ft of you (including yourself) will wake up to 3d6 silver pieces on their stomach.")
    if d100 == 33:
        print("The target doesn't need to breath for the next",answerd4*2,"hours.")
    if d100 == 34:
        print("You don't need to breath for the next",answerd4*2,"hours.")
    if d100 == 35:
        print("Extreme wind pushes everyone within 20ft of you 10ft in a random direction (d4 - 1 North - 2 South - 3 East - 4 West). The direction can be different for everyone.")
    if d100 == 36:
        print("A little boy in a red cap with a baseball bat attempts to kill you. He has an armour class of 13 but 500 hp. Every hit deals one damage, and his movement speed is 20ft.")
    if d100 == 37:
        print("Everyone within 10ft of you is shrunk down to the size tiny.")
    if d100 == 38:
        print("All your clothes appear to catch on fire. They don't.")
    if d100 == 39:
        print("120 people appear and start to sing in a choir. Each has an AC of 8 and 5 hit points. If left for too long, their voices will go hoarse and they will start bleeding from their eyes and they will eventually starve to death.")
    if d100 == 40:
        print("One of your items appears 100ft in the air and falls back down at the end of your next turn.")
    if d100 == 41:
        print("You hear a voice in your head. 'slap someone in the next 30 seconds or face the consequences!' slapping someone means that next time you check your gold pouch, there will be an extra 20 gold pieces. Not slapping someone means you are encased in rock for a minute.")
    if d100 == 42:
        print("A darkness spell, centred on you, appears for one minute.")
    if d100 == 43:
        print("Everything within 20ft of you is darkness. While inside this darkness, anyone with darkvision no longer has it but someone who doesn't have darkvision will gain it.")
    if d100 == 44:
        print(answerd4*2,"Chiminimera appear for an hour. They are violent until you reduce them to half health, where they just sit there and whimper sadly. Killing them will result in every NPC they see will have their eyes glow green and immediately say, 'I am very disappointed in you,' and then return to normal and proceed to not know they said that for the entire rest of the game.")
    if d100 == 45:
        print("All vulnerabilities, resistances and immunities you and the target have get swapped for one minute. You have theirs and they have yours.")
    if d100 == 46:
        print("All vulnerabilities and resistances you and the target have get swapped for one minute. All your resistances turn to vulnerabilities and vice versa. The same happens to the target.")
    if d100 == 47:
        print("Any dirt within 20ft of you becomes mud and difficult terrain.")
    if d100 == 48:
        print("The nearest plant is set ablaze.")
    if d100 == 49:
        print("A sentient clockwork dog follows you around. It has an AC of 12 and 1 hit point. It will continue to follow you until you try to sell it, kill it or do anything else, in an attempt to get rid of it, upon which it whimpers and slowly melts itself, as you hear whispers saying, 'you monster, you horrible, evil, vile creature.' It will do nothing but follow.")
    if d100 == 50:
        print("A small portal appears. Only creatures you allow can go in. Inside the portal is house where there is anything that you could ever want. If it is taken outside the portal, it disappears. The portal disappears after 10 minutes, although people inside the house can still leave through the portal, just no-one can go back in.")
    if d100 == 51:
        print("Next time someone within 30ft of you casts a spell,",answerd4,"skeletons rise from the ground and use the help help action for that creature for",6-answerd4,"minutes.")
    if d100 == 52:
        print("A book falls from the sky. Inside the book is a 1000 word essay on how to make a sandwich. If you make the sandwich, it tastes horrible. Only then do you notice all the 1-star reviews and grading of F on it. Every meal you have will taste like this sandwich until you give the book to someone who doesn't know about the bad sandwich.")
    if d100 == 53:
        print("A book falls from the sky. Inside is 101 ways to make a book fall from the sky. No. 1 is: 'by using that staff that you just used.' All the rest are scratched out. Next to it is a marking saying '-for the dm's sanity. This is just for a once-off gag.' You don't know who the dm is, but you assume that he is the greatest thing of all time.")
    if d100 == 54:
        print("When the target dies, they will turn into a bunch of origami cranes and fly off.")
    if d100 == 55:
        print("The nearest body of water turns into ice for a minute.")
    if d100 == 56:
        print("You and the target get trapped in a giant snow globe. The snow globe must take 5 damage to break (AC 10).")
    if d100 == 57:
        print("You receive a newspaper talking about you as a horrible, murderous villain, labelled to be in one year. Wait… huh… whats a new spaper? A spaper that is new? Whats a spaper…? I guess it is going to be invented soon… Kind of a dumb name.")
    if d100 == 58:
        print("You are suddenly wearing a very fancy top hat, as tall as you are")
    if d100 == 59:
        print("A floating disco ball appears above your head. Everyone that can see or hear the disco ball starts dancing. The disco ball disappears in an hour.")
    if d100 == 60:
        print("The target flops around as if it is made of jelly for an hour.")
    if d100 == 61:
        print("You flop around as if you are made of jelly for an hour.")
    if d100 == 62:
        print("A giant bridge appears, going over your head and disappears when someone is in the middle of it.")
    if d100 == 63:
        print("The nearest body of water has over 1000 fish corpses float to the surface, dead.")
    if d100 == 64:
        print("The postman show up and gives you a really powerful weapon, which shatters as soon as you go to use it, dealing",answerd6*2,"piercing damage to everyone within 5ft.")
    if d100 == 65:
        print("A penguin, wearing a monocle and a top hat, waddles past you in",answerd4,"rounds and pecks you a bunch of times. If attacked, the penguin retaliates. He is a level 20 monk with 200 hp, an AC of 25, a walking speed of 100ft, a flying speed of 30ft, a swim speed of 200ft and will slap you 10 times a round, dealing 4d4 bludgeoning damage on a hit (+10). After 3 rounds, the penguin will introduce itself as Jesus (who?) and will sing, 'and he waddles away, waddle away, waddle waddle, till the very next day, bupbupbupbupbupbup.' He will never return. You are sad now.")
    if d100 == 66:
        print("Everyone within 30ft can't see anything except things on the ethereal plane.")
    if d100 == 67:
        print("A key appears in your pocket. Inserting it into a door opens up to a demiplane where",answerd6*3,"skeletons run out and attack you.")
    if d100 == 68:
        print("For one hour you believe that you can walk through walls even though you can't.")
    if d100 == 69:
        print("A floating longbow appears and shoots you with arrows. Each arrow has a cork on the end so it deals half the usual damage and it deals bludgeoning damage. If it reduces you to 0 hit points, you are pathetic. It lasts a minute, or until someone is knocked unconscious.")
    if d100 == 70:
        print("Three bottles appear in your backpack. Drinking one with heal 1d4 health, one is normal wine and the last deals 1d4 necrotic damage.")
    if d100 == 71:
        print("Water spills out of your shoes for 10 minutes, and next time you go to bed you will have sand in your sheets (IRL, not in game!).")
    if d100 == 72:
        print("An army of bugs crawls up your leg.")
    if d100 == 73:
        print("An army of bugs crawls up your targets leg.")
    if d100 == 74:
        print("You get trapped in a sarcophagus for 10 minutes. To unlock it is a DC 20 sleight of hand check with thieves tools from the outside. Or just smash it. AC 20, 20 it points. Immune to everything but force and bludgeoning damage.")
    if d100 == 75:
        print("Roll a d4. On a 1-2 you shrink",answerd4+1,"feet in height. On a 3-4 you grow",answerd4+1,"feet in height for a week")
    if d100 == 76:
        print("You get teleported to the top of a really tall mountain for 2d6 minutes before getting teleported back.")
    if d100 == 77:
        print("A woman appears, grabbing your arm and tries to pull you away from the party, saying, 'they've got my baby! Help me get my baby!' All attempts to reason with her fail. When she has you all alone, she turns into a succubus and attacks you.")
    if d100 == 78:
        print("An illusion makes it appear as though the ceiling/sky is collapsing on you. DC 20 investigation check to discern the ruse. If you touch it the illusion ends.")
    if d100 == 79:
        print("Everyone within 20ft have an irresistible urge to either, if they are outside, get inside, or if they are inside, get outside.")
    if d100 == 80:
        print("For the next",answerd4*2,"weeks your reflection doesn't follow you, but acts upon its own free will. Roll a d4. On a 1-2 the reflection is actually a Night Hag. She will work to slowly get you to free her. You can free her by splashing your reflection with holy water and saying, 'I unbind thee from my service!' The hag knows this. She will reveal her true form and attack the moment you save her. On a 3-4 it is a Celestial. The Celestial will help you but if you do an evil act then they will mislead you. It can hear you but cannot speak. If can write to you by fogging up the reflection, as if it is a reflection in a mirror. The reflections both know what you have done since they existed and know the best way to help you, although the Celestial will say it all cryptically and the Night Hag will mislead you.")
    if d100 == 81:
        print("Every tree within 50ft starts to grow different fruit. Picking the fruit off the tree will result in the fruit vanishing after",answerd4*2,"minutes. If the fruit are eaten, the eater heals",answerd4*2,"and next time they attack, have them roll on this table.")
    if d100 == 82:
        print("A magic, glass elevator appears. Going into it and pressing the button will have you go straight up, passing through solid objects. When you have gone up 200ft, the elevator will stop and stay there. If you press the button again, the elevator will disappear and you will fall back down super-fast and just before you hit the ground, it will re-appear below you, land and make a ding sound.")
    if d100 == 83:
        print("The nearest wall appears to have disappeared. When you try to walk through it, you will bump into it and you will hear a cackling noise. Everyone else will not hear the noise and see you go through the wall. After bumping into the wall you can see everyone else that has as well, and see through the illusion.")
    if d100 == 84:
        print("Any creatures in a 20ft circle, centred on you turns to dirt for",answerd4,"minutes, including you.")
    if d100 == 85:
        print("A 10ft wide, 20ft tall tower appears with a spiral staircase inside it. At the top of the staircase is a painting. The person in the painting moves, and says, 'haha, you just wasted your time!' Taking the painting off the wall reveals a chest. In the chest is",answerd4+1,"poisonous snakes and",answerd10*4,"silver pieces.")
    if d100 == 86:
        print("A random nearby object turns into a mimic.")
    if d100 == 87:
        print("A glass pane appears 10ft above you and falls down. Everyone within 10ft must make a Dexterity save or take",answerd8*3,"piercing damage, taking half on a success as it shatters everywhere.")
    if d100 == 88:
        print(5-answerd4,"chain devils appear and attack you, disappearing in",answerd4,"rounds (their rounds)")
    if d100 == 89:
        print(5-answerd4,"chain devils appear and attack your target, disappearing in",answerd4,"rounds (their rounds)")
    if d100 == 90:
        print("A trapdoor appears in the nearest unoccupied space near you. Going into the trapdoor brings you to a demiplane, but all that is there is a plain concrete room, 15ft by 15ft and 10ft tall. You can take the trapdoor with you, but it takes 10 minutes to open, as it is very stiff, and the room has to load in. When the trapdoor is closed, the room runs out of oxygen.")
    if d100 == 91:
        print("A random person within 20ft becomes hostile to the target (the target can be that person).")
    if d100 == 92:
        print("A random person within 20ft becomes charmed by the target.")
    if d100 == 93:
        print("A two-way portal appears, leading to a random spot on Gehenna. It closes after 24 hours.")
    if d100 == 94:
        print("A two-way portal appears, leading to a random spot on the Nine Hells. It closes after 24 hours.")
    if d100 == 95:
        print("Next time you attack, the target heals instead of taking damage.")
    if d100 == 96:
        print("Next attack you make, you heal the amount of damage you dealt.")
    if d100 == 97:
        print("Next attack you make, you take half the damage you deal.")
    if d100 == 98:
        print("A table falls from the sky and everyone, one their turn, must use their action and their move speed to stand on the table. Once they have stood on the table they heal 1 hit point.")
    if d100 == 99:
        print("A potion appears. There is enough liquid in it for",answerd4+2,"drinks. Every time you drink this potion, you regain 5 hit points, and you roll on this table again. If it requires a target, it triggers as soon as you make an attack. If you get this option again, reroll.")
    if d100 == 100:
        print("You deal",answerd4*4+(17-answerd4*4),"necrotic damage to the target.")

if d4 == 3:
    if d100 == 1:
        print("Have the player choose an ability score. Nothing happens.")
    if d100 == 2:
        print("The current map is replaced by the target's character sheet or statblock.  If this proves to be inconvenient, display the character sheet or statblock nearby in a visible location if possible. If stats do not exist for the target, create them specifically so they can be used as the map.")
    if d100 == 3:
        print("Instead of rolling damage, the caster's attacks always deal 5 damage for the next",answerd4,"encounters.")
    if d100 == 4:
        print("The caster loses a body part of choice, then has all their missing body parts replaced with metal. Replaced parts work as intended. The metal turns back to flesh in 1 week.")
    if d100 == 5:
        print("The caster's favourite NPC appears adjacent to the target.")
    if d100 == 6:
        print("The caster's least favourite NPC appears adjacent to the target.")
    if d100 == 7:
        print("The caster and target are restored to max hp.")
    if d100 == 8:
        print("All attacks the caster and target deal double damage until the end of their next turn.")
    if d100 == 9:
        print("The caster and target have no maximum health for",answerd4,"days. After a long rest, they will regain their max amount of hit points, but there is no limit to the amount of healing they can recieve.")
    if d100 == 10:
        print("For the next",answerd3,"campaign sessions, all advantage turns into disadvantage and vice-versa.")
    if d100 == 11:
        print("For the rest of the session, caster becomes an animated skeleton that cannot speak.")
    if d100 == 12:
        print("The caster now share a health pool with the last person they got into an argument with for an hour. Both parties become aware of this immediately.")
    if d100 == 13:
        print("The target now reflects all magical effects directed at them for 24 hours, as if they were the ones who cast it.")
    if d100 == 14:
        print("All combatants lose 4 years of age for 4 years, after which the effect ends and they return to their original age.")
    if d100 == 15:
        print("The nearest magical orb is now a magical cube. It has the original effects, but can now be rolled as a 1d6 to determine the level of intensity.")
    if d100 == 16:
        print("The caster is teleported to their current place of residence and is teleported back after",answerd4,"hours.")
    if d100 == 17:
        print("All ongoing effects on the caster are applied to all creatures within 60 feet of the target, with the exclusion of the target.")
    if d100 == 18:
        print("Any ongoing effects on the target triple in intensity and duration.")
    if d100 == 19:
        print("Any ongoing effects on the target triple in intensity and duration.")
    if d100 == 20:
        print("The caster thinks that they are immune to all mind-altering effects permanently, including their own. Really, they are only immune to the next time that happens, but never again. And yet, they still think they are immune.")
    if d100 == 21:
        print("The caster is permanently immune to a random damage type, but vulnerable to a different random damage type for 1d4+1 days (of the dm's choosing).")
    if d100 == 22:
        print("You lose control of your arm and it becomes sentient, doing whatever it likes for the next hour.")
    if d100 == 23:
        print("A sassy Lich follows you around and wants you to become a warlock using its power and won't leave until you say yes, and upon doing so, it will say, 'haha, jk!' and teleport away. If they attack the Lich it will not fight back")
    if d100 == 24:
        print("The attacker/casters thinks they are a frog, and acts like a frog for 10 minutes.")
    if d100 == 25:
        print("Your mind gets taken over by a god for 3 days.")
    if d100 == 26:
        print("Your mind gets taken over by an old dragon for 3 days")
    if d100 == 27:
        print("You believe that a random one of your party members are conspiring against you.")
    if d100 == 28:
        print("You and the target get teleported to an underground room and suffer from horrible hallucinations for one hour. After the hour, you are teleported back to your exact position. If something else is there,  both things take 5d12 bludgeoning damage and get moved to the nearest unoccupied space.")
    if d100 == 29:
        print("A swarm of",answerd4*5,"bats appear and attack you.")
    if d100 == 30:
        print("A swarm of",answerd4*5,"bats appear and attack your target.")
    if d100 == 31:
        print("A peasant shows up and challenges the party to a friendly battle (not to the death). The 'peasant' is a level 20 paladin with the sword of zariel.")
    if d100 == 32:
        print("Next time you long rest, everyone within 30ft of you (including yourself) will wake up to 3d6 silver pieces on their stomach.")
    if d100 == 33:
        print("The target doesn't need to breath for the next",answerd4*2,"hours.")
    if d100 == 34:
        print("You don't need to breath for the next",answerd4*2,"hours.")
    if d100 == 35:
        print("Extreme wind pushes everyone within 20ft of you 10ft in a random direction (d4 - 1 North - 2 South - 3 East - 4 West). The direction can be different for everyone.")
    if d100 == 36:
        print("A little boy in a red cap with a baseball bat attempts to kill you. He has an armour class of 13 but 500 hp. Every hit deals one damage, and his movement speed is 20ft.")
    if d100 == 37:
        print("Everyone within 10ft of you is shrunk down to the size tiny.")
    if d100 == 38:
        print("All your clothes appear to catch on fire. They don't.")
    if d100 == 39:
        print("120 people appear and start to sing in a choir. Each has an AC of 8 and 5 hit points. If left for too long, their voices will go hoarse and they will start bleeding from their eyes and they will eventually starve to death.")
    if d100 == 40:
        print("One of your items appears 100ft in the air and falls back down at the end of your next turn.")
    if d100 == 41:
        print("You hear a voice in your head. 'slap someone in the next 30 seconds or face the consequences!' slapping someone means that next time you check your gold pouch, there will be an extra 20 gold pieces. Not slapping someone means you are encased in rock for a minute.")
    if d100 == 42:
        print("A darkness spell, centred on you, appears for one minute.")
    if d100 == 43:
        print("Everything within 20ft of you is darkness. While inside this darkness, anyone with darkvision no longer has it but someone who doesn't have darkvision will gain it.")
    if d100 == 44:
        print(answerd4*2,"Chiminimera appear for an hour. They are violent until you reduce them to half health, where they just sit there and whimper sadly. Killing them will result in every NPC they see will have their eyes glow green and immediately say, 'I am very disappointed in you,' and then return to normal and proceed to not know they said that for the entire rest of the game.")
    if d100 == 45:
        print("All vulnerabilities, resistances and immunities you and the target have get swapped for one minute. You have theirs and they have yours.")
    if d100 == 46:
        print("All vulnerabilities and resistances you and the target have get swapped for one minute. All your resistances turn to vulnerabilities and vice versa. The same happens to the target.")
    if d100 == 47:
        print("Any dirt within 20ft of you becomes mud and difficult terrain.")
    if d100 == 48:
        print("The nearest plant is set ablaze.")
    if d100 == 49:
        print("A sentient clockwork dog follows you around. It has an AC of 12 and 1 hit point. It will continue to follow you until you try to sell it, kill it or do anything else, in an attempt to get rid of it, upon which it whimpers and slowly melts itself, as you hear whispers saying, 'you monster, you horrible, evil, vile creature.' It will do nothing but follow.")
    if d100 == 50:
        print("A small portal appears. Only creatures you allow can go in. Inside the portal is house where there is anything that you could ever want. If it is taken outside the portal, it disappears. The portal disappears after 10 minutes, although people inside the house can still leave through the portal, just no-one can go back in.")
    if d100 == 51:
        print("Next time someone within 30ft of you casts a spell,",answerd4,"skeletons rise from the ground and use the help help action for that creature for",6-answerd4,"minutes.")
    if d100 == 52:
        print("A book falls from the sky. Inside the book is a 1000 word essay on how to make a sandwich. If you make the sandwich, it tastes horrible. Only then do you notice all the 1-star reviews and grading of F on it. Every meal you have will taste like this sandwich until you give the book to someone who doesn't know about the bad sandwich.")
    if d100 == 53:
        print("A book falls from the sky. Inside is 101 ways to make a book fall from the sky. No. 1 is: 'by using that staff that you just used.' All the rest are scratched out. Next to it is a marking saying '-for the dm's sanity. This is just for a once-off gag.' You don't know who the dm is, but you assume that he is the greatest thing of all time.")
    if d100 == 54:
        print("When the target dies, they will turn into a bunch of origami cranes and fly off.")
    if d100 == 55:
        print("The nearest body of water turns into ice for a minute.")
    if d100 == 56:
        print("You and the target get trapped in a giant snow globe. The snow globe must take 5 damage to break (AC 10).")
    if d100 == 57:
        print("You receive a newspaper talking about you as a horrible, murderous villain, labelled to be in one year. Wait… huh… whats a new spaper? A spaper that is new? Whats a spaper…? I guess it is going to be invented soon… Kind of a dumb name.")
    if d100 == 58:
        print("You are suddenly wearing a very fancy top hat, as tall as you are")
    if d100 == 59:
        print("A floating disco ball appears above your head. Everyone that can see or hear the disco ball starts dancing. The disco ball disappears in an hour.")
    if d100 == 60:
        print("The target flops around as if it is made of jelly for an hour.")
    if d100 == 61:
        print("You flop around as if you are made of jelly for an hour.")
    if d100 == 62:
        print("A giant bridge appears, going over your head and disappears when someone is in the middle of it.")
    if d100 == 63:
        print("The nearest body of water has over 1000 fish corpses float to the surface, dead.")
    if d100 == 64:
        print("The postman show up and gives you a really powerful weapon, which shatters as soon as you go to use it, dealing",answerd6*2,"piercing damage to everyone within 5ft.")
    if d100 == 65:
        print("A penguin, wearing a monocle and a top hat, waddles past you in",answerd4,"rounds and pecks you a bunch of times. If attacked, the penguin retaliates. He is a level 20 monk with 200 hp, an AC of 25, a walking speed of 100ft, a flying speed of 30ft, a swim speed of 200ft and will slap you 10 times a round, dealing 4d4 bludgeoning damage on a hit (+10). After 3 rounds, the penguin will introduce itself as Jesus (who?) and will sing, 'and he waddles away, waddle away, waddle waddle, till the very next day, bupbupbupbupbupbup.' He will never return. You are sad now.")
    if d100 == 66:
        print("Everyone within 30ft can't see anything except things on the ethereal plane.")
    if d100 == 67:
        print("A key appears in your pocket. Inserting it into a door opens up to a demiplane where",answerd6*3,"skeletons run out and attack you.")
    if d100 == 68:
        print("For one hour you believe that you can walk through walls even though you can't.")
    if d100 == 69:
        print("A floating longbow appears and shoots you with arrows. Each arrow has a cork on the end so it deals half the usual damage and it deals bludgeoning damage. If it reduces you to 0 hit points, you are pathetic. It lasts a minute, or until someone is knocked unconscious.")
    if d100 == 70:
        print("Three bottles appear in your backpack. Drinking one with heal 1d4 health, one is normal wine and the last deals 1d4 necrotic damage.")
    if d100 == 71:
        print("Water spills out of your shoes for 10 minutes, and next time you go to bed you will have sand in your sheets (IRL, not in game!).")
    if d100 == 72:
        print("An army of bugs crawls up your leg.")
    if d100 == 73:
        print("An army of bugs crawls up your targets leg.")
    if d100 == 74:
        print("You get trapped in a sarcophagus for 10 minutes. To unlock it is a DC 20 sleight of hand check with thieves tools from the outside. Or just smash it. AC 20, 20 it points. Immune to everything but force and bludgeoning damage.")
    if d100 == 75:
        print("Roll a d4. On a 1-2 you shrink 1d4+1 feet in height. On a 3-4 you grow 1d4+1 feet in height for a week")
    if d100 == 76:
        print("You get teleported to the top of a really tall mountain for 2d6 minutes before getting teleported back.")
    if d100 == 77:
        print("A woman appears, grabbing your arm and tries to pull you away from the party, saying, 'they've got my baby! Help me get my baby!' All attempts to reason with her fail. When she has you all alone, she turns into a succubus and attacks you.")
    if d100 == 78:
        print("A magic wooden box appears. When you open the box, a loaf of bread is in there. It is enough bread for 10 days of rations although the bread disappears 24 hours after it leaves the box. When the bread disapears, the box also dissapears.")
    if d100 == 79:
        print("A box of water appears around the target. They can't breathe air while inside of this box. While in this box, they walk half their normal speed but have resistance to bludgeoning damage, as the water slows the attack down. It lasts for",answerd6*6,"rounds")
    if d100 == 80:
        print("Every 10 minutes the attacker/caster switches between their personality, one of an energetic child, and one of a grumpy old man without realising for",answerd4,"hours")
    if d100 == 81:
        print("A two-way portal appears, leading to a random spot on the Material Plane. It closes after 24 hours.")
    if d100 == 82:
        print("A two-way portal appears, leading to a random spot on the Feywild. It closes after 24 hours.")
    if d100 == 83:
        print("A two-way portal appears, leading to a random spot on the Shadowfell. It closes after 24 hours.")
    if d100 == 84:
        print("A two-way portal appears, leading to a random spot on Elysium. It closes after 24 hours.")
    if d100 == 85:
        print("A two-way portal appears, leading to a random spot on the Beastlands. It closes after 24 hours.")
    if d100 == 86:
        print("A two-way portal appears, leading to a random spot on Arborea. It closes after 24 hours.")
    if d100 == 87:
        print("A two-way portal appears, leading to a random spot on Ysgard. It closes after 24 hours.")
    if d100 == 88:
        print("A two-way portal appears, leading to a random spot on Limbo. It closes after 24 hours.")
    if d100 == 89:
        print("A two-way portal appears, leading to a random spot on Pandemonium. It closes after 24 hours.")
    if d100 == 90:
        print("A two-way portal appears, leading to a random spot on the Abyss. It closes after 24 hours.")
    if d100 == 91:
        print("A two-way portal appears, leading to a random spot on Carceri. It closes after 24 hours.")
    if d100 == 92:
        print("A two-way portal appears, leading to a random spot on Hades. It closes after 24 hours.")
    if d100 == 93:
        print("A two-way portal appears, leading to a random spot on Gehenna. It closes after 24 hours.")
    if d100 == 94:
        print("A two-way portal appears, leading to a random spot on the Nine Hells. It closes after 24 hours.")
    if d100 == 95:
        print("A two-way portal appears, leading to a random spot on Achereon. It closes after 24 hours.")
    if d100 == 96:
        print("A two-way portal appears, leading to a random spot on Mechanus. It closes after 24 hours.")
    if d100 == 97:
        print("A two-way portal appears, leading to a random spot on Arcadia. It closes after 24 hours.")
    if d100 == 98:
        print("A two-way portal appears, leading to a random spot on Mount Celestia. It closes after 24 hours.")
    if d100 == 99:
        print("A two-way portal appears, leading to a random spot on Bytopia. It closes after 24 hours.")
    if d100 == 100:
        print("A two-way portal appears, leading to a random spot on the Ethereal Plane. It closes after 24 hours.")
    