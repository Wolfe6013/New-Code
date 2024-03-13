from random import choice, randint

itemList = []
nameList = []

def save():
    f = open("Gamble.txt","w")
    done = 0
    for player in itemList:
        f.write(f"{nameList[done]}:")
        for item in player:
            f.write(f"/{item}")
        done += 1
        f.write("/\n")
    f.close()

def load():
    try:
        f = open("Gamble.txt","r")
        load_list = f.readlines()
        done = 0
        while done != len(load_list):
            playerName = (load_list[done]).split(':')[0]
            items = (load_list[done]).split('/')[1:]
            done += 1
            items.pop(len(items)-1)
            items.sort()
            itemList.append(items)
            nameList.append(playerName)
    except OSError:
        print("NO LOADABLE SAVE FILE")

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    gray_items = ["Armor-Piercing Rounds","Backup Magazine","Bison Steak","Bundle of Fireworks","Bustling Fungus","Cautious Slug","Crowbar","Delicate Watch","Energy Drink","Focus Crystal","Gasoline","Lens-Maker's Glasses","Medkit","Mocha","Monster Tooth","Oddly-shaped Opal","Paul's Goat Hoof","Personal Shield Generator","Power Elixir","Repulsion Armor Plate","Roll of Pennies","Rusted Key","Soldier's Syringe","Sticky Bomb","Stun Grenade","Topaz Brooch","Tougher Times","Tri-Tip Dagger","Warbanner"]
    green_items = ["AtG Missile Mk. 1","Bandolier","Berzerker's Pauldron","Chronobauble","Death Mark","Fuel Cell","Ghor's Tome","Harvester's Scythe","Hopoo Feather","Hunter's Harpoon","Ignition Tank","Infusion","Kjaro's Band","Leeching Seed","Lepton Daisy","Old Guillotine","Old War Stealthkit","Predatory Instincts","Razorwire","Red Whip","Regenerating Scrap","Rose Buckler","Runald's Band","Shipping Request Form","Shuriken","Squid Polyp","Ukulele","War Horn","Wax Quail","Will-o'-the-wisp"]
    red_items = ["57 Leaf Clover","Aegis","Alien Head","Ben's Raincoat","Bottled Chaos","Brainstalks","Brilliant Behemoth","Ceremonial Dagger","Dio's Best Friend","Frost Relic","H3AD-5T v2","Happiest Mask","Hardlight Afterburner","Interstellar Desk Plant","Laser Scope","N'kuhana's Opinion","Pocket I.C.B.M.","Rejuvenation Rack","Resonance Disc","Sentient Meat Hook","Shattering Justice","Soulbound Catalyst","Spare Drone Parts","Symbiotic Scorpion","Unstable Tesla Coil","Wake of Vultures"]
    active_items = ["Blast Shower","Disposable Missile Launcher","Eccentric Vase","Executive Card","Foreign Fruit","Forgive Me Please","Gnarled Woodsprite","Goobo Jr.","Gorag's Opus","Jade Elephant","Milky Chrysalis","Molotov (6-Pack)","Ocular HUD","Preon Accumulator","Primordial Cube","Radar Scanner","Recycler","Remote Caffeinator","Royal Capacitor","Sawmerang","Super Massive Leech","The Back-up","The Crowdfunder","Trophy Hunter's Tricorn","Volcanic Egg"]

    if '<@1210579164944404520>' in lowered or '<@&1210579760963395587>' in lowered:
        if 'gamble' in lowered:
            #load()
            roll = randint(1,100)         
            sub1 = "["
            sub2 = "]"
            idx1 = lowered.index(sub1)
            idx2 = lowered.index(sub2)
            name = lowered[idx1 + len(sub1) + 1: idx2]
            if roll < 46:
                return f'{name} offered to the shrine but gain nothing...'
            else:
                if roll > 45 and roll < 82:
                    item = choice(gray_items)
                elif roll > 81 and roll < 91:
                    item = choice(green_items)
                elif roll == 91:
                    item = choice(red_items)
                else:
                    item = choice(active_items)
                return f'{name} offered to the shrine and was rewarded!\nYou got a {item}!'

        #elif 'items' in lowered:
            #load()
            pos = 0
            info = []
            for x in nameList:
                info.append(f"{x}: -")
                for y in itemList[pos]:
                    info.append(f"{y} -")
                info.append("\n")
                pos += 1
            info = ' '.join(info)
            return info

        elif 'roll d4' in lowered:
            return f'You rolled: {randint(1, 4)}'
        elif 'roll d6' in lowered:
            return f'You rolled: {randint(1, 6)}'
        elif 'roll d8' in lowered:
            return f'You rolled: {randint(1, 8)}'
        elif 'roll d10' in lowered:
            return f'You rolled: {randint(1, 10)}'
        elif 'roll d12' in lowered:
            return f'You rolled: {randint(1, 12)}'
        elif 'roll d20' in lowered:
            return f'You rolled: {randint(1, 20)}'
        elif 'flip coin' in lowered:
            return f'You flipped: {choice(["Heads","Tails"])}'
        elif 'help' in lowered:
            return f"To use a command, simply <@1210579164944404520> (either the bot or the role) and write the command following that.\nTo get the bot to message you privately, start your message with a '?'\ngamble - offers to the Shrine of Chance. Wonder what you'll get!\nroll d4 - rolls a four sided dice and gives you the outcome.\nroll d6 - rolls a six sided dice and gives you the outcome.\nroll d8 - rolls an eight sided dice and gives you the outcome.\nroll d10 - rolls a ten sided dice and gives you the outcome.\nroll d12 - rolls a twelve sided dice and gives you the outcome.\nroll d20 - rolls a twenty sided dice and gives you the outcome.\nflip coin - flips a coin and gives you the outcome.\nhelp - tells you every command available"
        else:
            return 'Unknown command, try "help" for more info'