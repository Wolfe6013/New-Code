import random
import time

def Any():
    VillageNameList = ['Kimber','Carroway','Frozen Head','Tatetown','Jim Town','Big Lick','Grassy Cove','Midway','Ozone','Bone Cave','Cedar Grove','Bon Aire','Doyle','Ravenscroft','Walling','Boma','Brotherton Mountain','Cane Creek','Cedar Hill','Dry Valley','Double Springs','Gentry','Post Oak','Silver Point','West Gate','Winona','Little Crab','Pen Mellin','Shirley','Tinch Town','Wilder','Zenith','Flat Top Mountain','Harrison','Middle Valley','Ooltewah','Sale Creek','Bakewell','George Town','Shady Grove','Hale Town','Winesap','Sequatchie','Running Water','Cordova','Eads','Ellendale','Fishervale','Rosemark','Beech Grove','Bethel','Briceville','Claxton','Fork Mountain','Laurel Grove','Rosedale','Branchville','Bugscuffe',"Cortner's Station",'Bell Tower','Craggie Hope','Joelton','Shaklett','Cold Springs','Armona','Binfield','Clover Hill','Kinzel Springs','Laws Chapel','Mentor','Mint','Sunshine','Meltron','Coal Hill','Misty Ridge','Prospect','Tasso','Bluewing','Brandyville','Gassaway','Iconium','Readyville','Sugar Tree Knob','Hollow Brock','Buema Vista','Lvinia','Leach','Yuma','West Port','Big Spring','Bitter End','Stoney Creek','Fish Springs','Antioch','Ovoca','Crockett Mills','Free Hill',"Butler's Landing",'Lilly Dale','Raven Hill']
    VillageName = random.choice(VillageNameList)
    print(f"The village's name is {VillageName}")
    time.sleep(0.5)
    VillagePopulation = round((random.randint(100,1000))/10)*10
    print(f'It has a population of {VillagePopulation} people')
    time.sleep(0.5)
    WealthLevelList = ['The village is Impoverished. The people of the village have barely enough food to eat. Everything is filthy, and everything stinks. What should be working in this village appears to be broken or worn out. There are very few buildings with a couple small shacks, and no walls. This village is either extremely isolated, or extremely oppressed.',"The village is Poor. The people of the village live in poverty, but most seem content in spite of it. The streets are dirty, but the people make do with what they've got. Most of the buildings are small, and a short wall surrounds the village that looks slapped together using random pieces of scrap. This village is either a little isolated, or a little oppressed.","The village is Wealthy. The people of this village seem busy, yet driven. The streets are clean and optimised for productivity. Most of the buildings are spacious, and there is probably a tall, thick, wooden wall that surrounds this village.","The village is Opulent. The people of this village sound jolly and appear well fed. The streets are flashy, featuring wide, stone roads for easy travel. Most of the buildings are artfully ActivitiesDone, favouring beauty over practicality. There is probably a strong wall made of stone or brick that surrounds the village, and it borders becoming a town. This village is either heavily trafficked, or heavily sponsored."]
    WealthLevel = random.choice(WealthLevelList)
    print(f'{WealthLevel}')
    time.sleep(0.5)
    GreetTypeList = ['Verbal','Greeting']
    GreetType = random.choice(GreetTypeList)
    if GreetType == 'Verbal':
        VerbalGreetingList = ["'Good Morrow!'","'Hail fellow!'","'How ya goin?'","'Howdy-doody?'","'Salutations!'","'Top of the mornin' to ya!'","'Well met!'","'Wesap hala!'","'Whadda you at?'","'What's kickin?'","'Hello!'","'Teehee!'"]
        VerbalGreeting = random.choice(VerbalGreetingList)
        print(f"The people of this village greet people by saying {VerbalGreeting}")
    else:
        PhysicalGreetingList = ["back patting.","bowing.","butterfly kiss.","cheek kissing.","waving.","fist bumps.","handshakes.","hongi.","salute.","spartan handshake.","clicking heels."]
        PhysicalGreeting = random.choice(PhysicalGreetingList)
        print(f"The people of this village greet people by {PhysicalGreeting}")
    time.sleep(0.5)
    HolidayReasonList = ["The holiday is to celebrate and be thankful for a successful harvest.","The holiday is to celebrate and remember a historic figure.","The holiday is to celebrate and remember a historic victory.","The holiday is to celebrate and show gratitude for each other."]
    HolidayWorkList = ["Nobody works.","Some shops stay open/staffed."]
    HolidayReason = random.choice(HolidayReasonList)
    print(f'{HolidayReason}')
    time.sleep(0.5)
    HolidayWork = random.choice(HolidayWorkList)
    print(f'{HolidayWork}')
    time.sleep(0.5)
    NumberOfActivities = random.randint(2,4)
    ActivitiesDone = 0
    while NumberOfActivities > ActivitiesDone:
        ActivitiesDone += 1
        EvilAct = random.randint(1,100)
        if EvilAct >= 98:
            if EvilAct == 98:
                print(f"Activity {ActivitiesDone} is a group orgy")
            if EvilAct == 99:
                SacrificeReasonList = ['the youngest person','the oldest person','the most hated person','the poorest person','the richest person','a random person','ten random people','a random quarter of the population']
                SacrificeReason = random.choice(SacrificeReasonList)
                print(f"Activity {ActivitiesDone} is a sacrifice of {SacrificeReason} in the village.")
            if EvilAct == 100:
                print(f"Activity {ActivitiesDone} is the purge")
        else:
            ActivitiesList = ["dancing around a bonfire.","dancing in the streets.","dressing up in costumes.","excessive drinking.","face painting.","feasting all together oudoors.","feasting at home with family.","floating lanterns.","flying kites.","giving gifts.","going on a date.","lighting firecrackers.","lighting fireworks.","playing games together.","singing all day.","singing all night.","telling jokes.","telling stories.","throwing coloured powder.","throwing flower petals."]
            Activity = random.choice(ActivitiesList)
            print(f"Activity {ActivitiesDone} is {Activity}")
        time.sleep(0.5)
    HolidayTime = random.randint(0,364)
    if HolidayTime == 0:
        print(f'The holiday is today!')
    else:
        if HolidayTime == 1:
            print(f'The holiday is tommorrow!')
        else:
            print(f'The holiday is {HolidayTime} days away.')
    DisasterList = ['There is currently a drought.','An earthquake will happen.','A flood will happen.','A thunderstorm will happen.','A tornado will happen.','A volcanic erruption will happen.','A wildfire will happen.','An earthquake just happen.','A flood just happen.','A thunderstorm just happen.','A tornado just happen.','A volcanic erruption just happen.','A wildfire just happen.']
    InfestationList = ['There is a Giand Centipede infestation','There is a Giant Rat infestation','There is a Giant Wasp infestation','There is a Giant Wolf Spider infestation','There is a Kobold infestation','There is a Poisonous Snake infestation','There is a Bat infestation','There is an Insect infestation']
    RaidList = ['The village is about to be raided by bugbears.','The village is about to be raided by drow.','The village is about to be raided by duergar.','The village is about to be raided by gnolls.','The village is about to be raided by goblins.','The village is about to be raided by hobgoblins.','The village is about to be raided by orcs.','The village is about to be raided by rival village.','The village has just been raided by bugbears.','The village has just been raided by drow.','The village has just been raided by duergar.','The village has just been raided by gnolls.','The village has just been raided by goblins.','The village has just been raided by hobgoblins.','The village has just been raided by orcs.','The village has just been raided by rival village.']
    Issue = random.randint(1,30)
    if Issue == 28:
        Disaster = random.choice(DisasterList)
        print(f'{Disaster}')
        time.sleep(0.5)
    if Issue == 29:
        Infestation = random.choice(InfestationList)
        print(f'{Infestation}')
        time.sleep(0.5)
    if Issue == 30:  
        Raid = random.choice(RaidList)
        print(f'{Raid}')
        time.sleep(0.5)
    CryptidChance = random.randint(1,5)
    if CryptidChance == 5:
        CryptidList = ["the villagers believe there is a Bunyip living nearby.","the villagers believe there is a Chupacabra living nearby.","the villagers believe there is a Death Worm living nearby.","the villagers believe there is a Ferus Devil living nearby.","the villagers believe there is a Nessie living nearby.","the villagers believe there is a Ogopogo living nearby.","the villagers believe there is a Slenderman living nearby.","the villagers believe there is a Thunderbird living nearby.","the villagers believe there is a Wendigo living nearby.","the villagers believe there is a Yeti/Bigfoot living nearby."]
        Cryptid = random.choice(CryptidList)
        print(f'{Cryptid}')
        time.sleep(0.5)
    GossipDone = 0
    NameList = ['Alexios','Ajax','Arnoux','Hal','Aylmer','Cloud','Flint','Kiley','Ledger','Ary','Arlo','Cedrick','Matteo','Omar','Jasper','Axel','Jax','Cecil','Javier','Jace','Fox','Magnolia','Lemon','Ari','Arya','Fay','Maiya','Tory','Xena','Aida','Kaz','Charmaine','Alena','Ember','Marlowe','Kimia','Kaelie','Azariah','Celeste','Valencia']
    GossipList = ['had an accident and may never recover.','has no children and is losing fertility.','is cursed because of a physical defect.','is dying from an infectious disease.',"is broke, and can't support their family.",'is lowering product quality to cut costs.','the mayor is using tax money for their vacations.','just inherited a huge sum of money.',"just had a child, but it isn't theirs/their spouse's.",'is dating two people at the same time.','is having an affair with their superiors SO.','is no longer living with their spouse.']
    while GossipDone < 3:
        Name = random.choice(NameList)
        Gossip = random.choice(GossipList)
        print(f'{Name} {Gossip}')
        GossipDone += 1
        NameList.remove(Name)
        GossipList.remove(Gossip)
        time.sleep(0.5)
Any()