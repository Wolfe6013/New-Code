import time
#####----- Rules: -----#####
###--- Variable Name = Card Name, ( ) become (_), (,) and (') and (-) get deleted ---###
##-- When adding a new card, put in designated spot, then put it in ONE of the lists of cards, at the end --##

#####----- Cards -----#####
Definer_Cards = ["___Cards:___"]
###--- White-Blue Commander ---###
Isperia_Supreme_Judge = ["Isperia, Supreme Judge","White-Blue","6 Cost","2 Colourless, 2 White, 2 Blue","Legendary Creature","Legendary","Creature","Sphinx","6/4","6/_","_/4","Flying","Draw Card",1]
Archon_of_Redemption = ["Archon of Redemption","White","5 Cost","3 Colourless, 2 White","Creature","Archon","3/4","3/_","_/4","Gain Life",1]
Cartographers_Hawk = ["Cartographer's Hawk","White","2 Cost","1 Colourless, 1 White","Creature","Bird","2/1","2/_","_/1","Flying",1]
Cleansing_Nova = ["Cleansing Nova","White","5 Cost","3 Colourless, 2 White","Sorcery","Destory",1]
Emeria_Angel = ["Emeria Angel","White","4 Cost","2 Colourless, 2 White","Creature","Angel","3/3","3/_","_/3","Flying","Landfall","Bird Token","Token Create",1]
Gideon_Jura = ["Gideon Jura","White","5 Cost","3 Colourless, 2 White","Legendary Planeswalker","Legendary","Planeswalker","Gideon","6, +2, -2, 0",1]
Hanged_Executioner = ["Hanged Executioner","White","3 Cost","2 Colourless, 1 White","Creature","Spirit","1/1","1/_","_/1","Flying","Spirit Token","Token Create","Exile",1]
Remorseful_Cleric = ["Remorseful Cleric","White","2 Cost","1 Colourless, 1 White","Creature","Spirit Cleric","Spirit","Cleric","2/1","2/_","_/1","Flying","Sacrifice","Exile",1]
Sephara_Skys_Blade = ["Sephara, Sky's Blade","White","7 Cost","4 Colourless, 3 White","Legendary Creature","Legendary","Creature","Angel","7/7","7/_","_/7","Flying","Lifelink","Indestructable",1]
SteelPlume_Marshal = ["Steel-Plume Marshal","White","5 Cost","3 Colourless, 2 White","Creature","Bird Soldier","Bird","Soldier","3/3","3/_","_/3","Flying","+_/+_",1]
Storm_Herd = ["Storm Herd","White","10 Cost","8 Colourless, 2 White","Sorcery","Pegasus Token","Token Create",1]
True_Conviction = ["True Conviction","White","6 Cost","3 Colourless, 3 White","Enchantment","Double Strike","Lifelink",1]
Angler_Turtle = ["Angler Turtle","Blue","7 Cost","5 Colourless, 2 Blue","Creature","Turtle","5/7","5/_","_/7","Hexproof",1]
Bident_of_Thassa = ["Bident of Thassa","Blue","4 Cost","2 Colourless, 2 Blue","Legendary Enchantment Artifact","Legendary Enchantment","Legendary Artifact","Enchantment Artifact","Draw Card",1]
Diluvian_Primordial = ["Diluvian Primordial","Blue","7 Cost","5 Colourless, 2 Blue","Creature","Avatar","5/5","5/_","_/5","Flying","Cast","Exile",1]
EverWatching_Threshold = ["Ever-Watching Threshold","Blue","3 Cost","2 Colourless, 1 Blue","Enchantment","Draw Card",1]
Faerie_Formation = ["Faerie Formation","Blue","5 Cost","4 Colourless, 1 Blue","Creature","Faerie","5/4","5/_","_/4","Flying","Faerie Token","Token Create","Draw Card",1]
Gravitational_Shift = ["Gravitational Shift","5 Cost","3 Colourless, 2 Blue","Enchantment","+_/+_","-_/-_",1]
Inspired_Sphinx = ["Inspired Sphinx","Blue","7 Cost","5 Colourless, 2 Blue","Creature","Sphinx","5/5","5/_","_/5","Flying","Draw Card","Thopter Token","Token Create",1]
Sharding_Sphinx = ["Sharding Sphinx","Blue","6 Cost","4 Colourless, 2 Blue","Artifact Creature","Artifact","Creature","Sphinx","4/4","4/_","_/4","Flying","Thopter Token","Token Create",1]
Sphinx_of_Enlightenment = ["Sphinx of Enlightenment","Blue","6 Cost","4 Colourless, 2 Blue","Creature","Sphinx","5/5","5/_","_/5","Flying","Draw Card",1]
Windreader_Sphinx = ["Windreader Sphinx","Blue","7 Cost","5 Colourless, 2 Blue","Creature","Sphinx","3/7","3/_","_/7","Flying","Draw Card",1]
Absorb = ["Absorb","White-Blue","3 Cost","1 White, 2 Blue","Instant","Counter","Gain Life",1]
Skycat_Sovereign = ["Skycat Sovereign","White-Blue","2 Cost","1 White, 1 Blue","Creature","Elemental Cat","Elemental","Cat","1/1","1/_","_/1","Flying","+_/+_","Cat Bird Token","Token Create",1]
Sphinxs_Revelation = ["Sphinx's Revelation","White-Blue","X Cost","X+3 Cost","X Colourless, 1 White, 2 Blue","Instant","Gain Life","Draw Card",1]
Time_Wipe = ["Time Wipe","White-Blue","5 Cost","2 Colourless, 2 White, 1 Blue","Sorcery","Destroy",1]
Aven_Gagglemaster = ["Aven Gagglemaster","White","5 Cost","3 Colourless, 2 White","Creature","Bird Warrior","Bird","Warrior","4/3","4/_","_/3","Flying","Gain Life",1]
Banishing_Light = ["Banishing Light","White","3 Cost","2 Colourless, 1 White","Enchantment","Exile",1]
Condemn = ["Condemn","White","1 Cost","1 White","Instant","Gain Life",1]
Crush_Contraband = ["Crush Contraband","White","4 Cost","3 Colourless, 1 White","Instant","Exile",1]
Disenchant = ["Disenchant","White","2 Cost","1 Colourless, 1 White","Instant","Destroy",1]
Generous_Gift = ["Generous Gift","White","3 Cost","2 Colourless, 1 White","Instant","Destroy","Elephant Token","Token Create",1]
Kangees_Lieutenant = ["Kangee's Lieutenant","White","3 Cost","2 Colourless, 1 White","Creature","Bird Soldier","Bird","Soldier","1/1","1/_","_/1","Flying","+_/+_","Encore",1]
Rally_of_Wings = ["Rally of Wings","White","2 Cost","1 Colourless, 1 White","Instant","Untap","+_/+_",1]
Soul_Snare = ["Soul Snare","White","1 Cost","1 White","Enchantment","Sacrifice","Exile",1]
Swords_to_Plowshares = ["Swords to Plowshares","White","1 Cost","1 White","Instant","Exile","Gain Life",1]
Vow_of_Duty = ["Vow of Duty","White","3 Cost","2 Colourless, 1 White","Enchantment","Aura","+_/+_","Vigilance",1]
Aetherize = ["Aetherize","Blue","4 Cost","3 Colourless, 1 Blue","Instant",1]
Counterspell = ["Counterspell","Blue","2 Cost","2 Blue","Instant","Counter",1]
Favorable_Winds = ["Favorable Winds","Blue","2 Cost","1 Colourless, 1 Blue","Enchantment","+_/+_",1]
Negate = ["Negate","Blue","2 Cost","1 Colourless, 1 Blue","Instant","Counter",1]
Tide_Skimmer = ["Tide Skimmer","Blue","4 Cost","3 Colourless, 1 Blue","Creature","Drake","2/3","2/_","_/3","Flying","Draw Card",1]
Warden_of_Evos_Isle = ["Warden of Evos Isle","Blue","3 Cost","2 Colourless, 1 Blue","Creature","Bird Wizard","Bird","Wizard","2/2","2/_","_/2","Flying",1]
Winged_Words = ["Winged Words","Blue","3 Cost","2 Colourless, 1 Blue","Sorcery","Draw Card",1]
Cloudblazer = ["Cloudblazer","White-Blue","5 Cost","3 Colourless, 1 White, 1 Blue","Creature","Human Scout","Human","Scout","2/2","2/_","_/2","Flying","Gain Life","Draw Card",1]
Empyrean_Eagle = ["Empyrean Eagle","White-Blue","3 Cost","1 Colourless, 1 White, 1 Blue","Creature","Bird Spirit","Bird","Spirit","2/3","2/_","_/3","Flying","+_/+_",1]
Jubilint_Skybonder = ["Jubilant Skybonder","White-Blue","3 Cost","1 Colourless, 2 White or Blue","Creature","Human Wizard","Human","Wizard","2/2","2/_","_/2","Flying","Hexresistant","Hexresistant 2",1]
Kangee_Sky_Warden = ["Kangee, Sky Warden","White-Blue","5 Cost","3 Colourless, 1 White, 1 Blue","Legendary Creature","Legendary","Creature","Bird Wizard","Bird","Wizard","3/3","3/_","_/3","Flying","Vigilance","+_/+_",1]
Migratory_Route = ["Migratory Route","White-Blue","5 Cost","3 Colourless, 1 White, 1 Blue","Sorcery","Bird Token","Token Create","Basic Landcycling",1]
Staggering_Insight = ["Staggering Insight","White-Blue","2 Cost","1 White, 1 Blue","Enchantment","Aura","+_/+_","Lifelink","Draw Card",1]
Thunderclap_Wyvern = ["Thunderclap Wyvern","White-Blue","4 Cost","2 Colourless, 1 White, 1 Blue","Creature","Drake","2/3","2/_","_/3","Flash","Flying","+_/+_",1]
Arcane_Signet = ["Arcane Signet","Colourless","2 Cost","2 Colourless","Artifact","Add Mana",1]
Azorius_Signet = ["Azorius Signet","Colourless","2 Cost","2 Colourless","Artifact","Add Mana",1]
Commanders_Sphere = ["Commander's Sphere","Colourless","3 Cost","3 Colourless","Artifact","Add Mana","Draw Card",1]
Hedron_Archive = ["Hedron Archive","Colourless","4 Cost","4 Colourless","Artifact","Add Mana","Draw Card",1]
Pilgrims_Eye = ["Pilgrim's Eye","Colourless","3 Cost","3 Colourless","Artifact Creature","Artifact","Creature","Thopter","1/1","1/_","_/1","Flying",1]
Sky_Diamond = ["Sky Diamond","Colourless","2 Cost","2 Colourless","Artifact","Add Mana",1]
Skyscanner = ["Skyscanner","Colourless","3 Cost","3 Colourless","Artifact Creature","Artifact","Creature","Thopter","1/1","1/_","_/1","Flying","Draw Card",1]
Sol_Ring = ["Sol Ring","Colourless","1 Cost","1 Colourless","Artifact","Add Mana",1]
Talisman_of_Progress = ["Talisman of Progress","Colourless","2 Cost","2 Colourless","Artifact","Add Mana",1]
Thought_Vessel = ["Thought Vessel","Colourless","2 Cost","2 Colourless","Artifact","Add Mana","No Max Hand Size",1]

Cards_White_Blue_Commander = [Isperia_Supreme_Judge,Archon_of_Redemption,Cartographers_Hawk,Cleansing_Nova,Emeria_Angel,Gideon_Jura,Hanged_Executioner,Remorseful_Cleric,Sephara_Skys_Blade,SteelPlume_Marshal,Storm_Herd,True_Conviction,Angler_Turtle,Bident_of_Thassa,Diluvian_Primordial,EverWatching_Threshold,Faerie_Formation,Gravitational_Shift,Inspired_Sphinx,Sharding_Sphinx,Sphinx_of_Enlightenment,Windreader_Sphinx,Absorb,Skycat_Sovereign,Sphinxs_Revelation,Time_Wipe,Aven_Gagglemaster,Banishing_Light,Condemn,Crush_Contraband,Disenchant,Generous_Gift,Kangees_Lieutenant,Rally_of_Wings,Soul_Snare,Swords_to_Plowshares,Vow_of_Duty,Aetherize,Counterspell,Favorable_Winds,Negate,Tide_Skimmer,Warden_of_Evos_Isle,Winged_Words,Cloudblazer,Empyrean_Eagle,Jubilint_Skybonder,Kangee_Sky_Warden,Migratory_Route,Staggering_Insight,Thunderclap_Wyvern,Arcane_Signet,Azorius_Signet,Commanders_Sphere,Hedron_Archive,Pilgrims_Eye,Sky_Diamond,Skyscanner,Sol_Ring,Talisman_of_Progress,Thought_Vessel]

Lands_White_Blue_Commander = ["Plains x15","Island x15","Moorland Haunt","Port Town","Prairie Stream","Temple of Enlightenment","Coastal Tower","Command Tower","Meandering River","Sejiri Refuge","Tranquil Cove"]

Tokens_White_Blue_Commander = ["Bird/Spirit x2","Bird/Thopter","Bird/Faerie","Cat Bird/Thopter","Cat Bird/Spirit","Cat Bird/Faerie","Pegasus/Thopter","Pegasus/Faerie","Elephant/Thopter"]

###--- White-Blue Beginner ---###
Dreamshackle_Geist = ["Dreamshackle Geist","Blue","3 Cost","1 Colourless, 2 Blue","Creature","Spirit","3/1","3/_","_/1","Flying",1]
Extraction_Specialist = ["Exraction Specialist","White","3 Cost","2 Colourless, 1 White","Creature","Human Rogue","Human","Rogue","3/2","3/_","_/2","Lifelink",1]
Stormrider_Spirit = ["Stormrider Spirit","Blue","5 Cost","4 Colourless, 1 Blue","Creature","Spirit","3/3","3/_","_/3","Flash","Flying",2]
Nebelgast_Beguiler = ["Nebelgast Beguiler","White","5 Cost","4 Colourless, 1 White","Creature","Spirit","2/5","2/_","_/5",2]
Consuming_Tide = ["Consuming Tide","Blue","4 Cost","Sorcery","Draw Card",1]
Hullbreaker_Horror = ["Hullbreaker Horror","Blue","7 Cost","5 Colourless, 2 Blue","Creature","Kraken Horror","Kraken","Horror","7/8","7/_","_/8","Flash",1]
Brute_Suit = ["Brute Suit","Colourless","3 Cost","3 Colourless","Artifact","Vehicle","4/3","4/_","_/3","Crew","Crew 1","Vigilance",2]
Wretched_Throng = ["Wretched Throng","Blue","2 Cost","1 Colourless, 1 Blue","Creature","Zombie Horror","Zombie","Horror","2/1","2/_","_/1",4]
Fading_Hope = ["Fading Hope","Blue","1 Cost","1 Blue","Instant","Scry","Scry 1",2]
Kill_Shot = ["Kill Shot","White","3 Cost","2 Colourless, 1 White","Instant","Destroy",2]
Backup_Agent = ["Backup Agent","White","2 Cost","1 Colourless, 1 White","Creature","Human Citizen","Human","Citizen","1/1","1/_","_/1","+_/+_",3]
Unholy_Officiant = ["Unholy Officiant","White","1 Cost","1 White","Creature","Vampire Cleric","Vampire","Cleric","1/2","1/_","_/2","Vigilance","+_/+_",2]
Inspiring_Overseer = ["Inspiring Overseer","White","3 Cost","2 Colourless, 1 White","Creature","Angel Cleric","Angel","Cleric","2/1","2/_","_/1","Flying","Gain Life","Draw Card",3]
Welcoming_Vampire = ["Welcoming Vampire","White","3 Cost","2 Colourless, 1 White","Creature","Vampire","2/3","2/_","_/3","Flying","Draw Card",1]
Serpentine_Ambush = ["Serpentine Ambush","Blue","2 Cost","1 Colourless, 1 Blue","Instant","5/5",3]
SevenTail_Mentor = ["Seven-Tail Mentor","White","4 Cost","3 Colourless, 1 White","Creature","Fox Samurai","Fox","Samurai","2/3","2/_","_/2","+_/+_",3]

Cards_White_Blue_Beginner = [Dreamshackle_Geist,Extraction_Specialist,Stormrider_Spirit,Nebelgast_Beguiler,Consuming_Tide,Hullbreaker_Horror,Brute_Suit,Wretched_Throng,Fading_Hope,Kill_Shot,Backup_Agent,Unholy_Officiant,Inspiring_Overseer,Welcoming_Vampire,Serpentine_Ambush,SevenTail_Mentor]

Lands_White_Blue_Beginner = ["Plains x12","Island x11","Tranquil Cove x4"]

###--- Red-Green Beginner ---###
Witchs_Web = ["Witch's Web","Green","2 Cost","1 Colourless, 1 Green","Instant","+_/+_","Reach",3]
Flourishing_Hunter = ["Flourishing Hunter","Green","6 Cost","4 Colourless, 2 Green","Creature","Wolf Spirit","Wolf","Spirit","6/6","6/_","_/6","Gain Life",2]
Burn_the_Accursed = ["Burn the Accursed","Red","5 Cost","4 Colourless, 1 Red","Instant","Deal _ Damage","Exile",2]
Spore_Crawler = ["Spore Crawler","Green","3 Cost","2 Colourless, 1 Green","Creature","Fungus","3/2","3/_","_/2","Draw Card",3]
HighRise_Sawjack = ["High-Rise Sawjack","Green","3 Cost","2 Colourless, 1 Green","Creature","Elf Citizen","Elf","Citizen","2/3","2/_","_/3","Reach","+_/+_",3]
Topiary_Stomper = ["Topiary Stomper","Green","3 Cost","1 Colourless, 2 Green","Creature","Plant Dinosaur","Plant","Dinosaur","4/4","4/_","_/4","Vigilance",1]
Timberland_Guide = ["Timberland Guide","Green","2 Cost","1 Colourless, 1 Green","Creature","Human Scout","Human","Scout","1/1","1/_","_/1","+_/+_",4]
Mounted_Dreadknight = ["Mounted Dreadknight","Red","5 Cost","4 Colourless, 1 Red","Creature","Vampire Knight","Vampire","Knight","5/4","5/_","_/4","Trample","+_/+_",3]
Lambholt_Harrier = ["Lambhold Harrier","Red","2 Cost","1 Colourless, 1 Red","Creature","Wolf","2/2","2/_","_/2",3]
Thundering_Raiju = ["Thundering Raiju","Red","4 Cost","2 Colourless, 2 Red","Creature","Spirit","3/3","3/_","_/3","Haste","+_/+_","Deal _ Damage"]
Voldaren_Stinger = ["Voldaren Stinger","Red","1 Cost","1 Red","Creature","Vampire Warrior","Vampire","Warrior","1/1","1/_","_/1","First Strike","+_/+_",2]
Abrade = ["Abrade","Red","2 Cost","1 Colourless, 1 Red","Instant","Deal _ Damage","Destroy",3]
Creepy_Puppeteer = ["Creepy Puppeteer","Red","4 Cost","3 Colourless, 1 Red","Creature","Human Roge","Human","Rogue","4/3","4/_","_/3","Haste",1]
Glorious_Sunrise = ["Glorious Sunrise","Green","5 Cost","3 Colourless, 2 Green","Enchantment","+_/+_","Trample","Add Mana","Draw Card","Gain Life",1]
Ascendant_Packleader = ["Ascendant Packleader","Green","1 Cost","1 Green","Creature","Wolf","2/1","2/_","_/1","+_/+_",1]

Cards_Red_Green_Beginner = [Witchs_Web,Flourishing_Hunter,Burn_the_Accursed,Spore_Crawler,HighRise_Sawjack,Topiary_Stomper,Timberland_Guide,Mounted_Dreadknight,Lambholt_Harrier,Thundering_Raiju,Voldaren_Stinger,Abrade,Creepy_Puppeteer,Glorious_Sunrise,Ascendant_Packleader]

Lands_Red_Green_Beginner = ["Mountain x12","Forest x11","Rugged Highlands x4"]

###--- Booster ---###
Vanquishers_Axe = ["Vanquisher's Axe","Colourless","1 Cost","1 Colourless","Artifact","Equiptment","+_, +_",1]
Salvaged_Manaworker = ["Salvaged Manaworker","Colourless","2 Cost","2 Colourless","Artifact Creature","Artifact","Creature","Construct","1/3","1/_","_/3","Add Mana",1]
Relic_of_Legends = ["Relic of Legends","Colourless","3 Cost","3 Colourless","Artifact","Add Mana",1]
Automatic_Librarian = ["Automatic Librarian","Colourless","3 Cost","3 Colourless","Artifact Creature","Artifact","Creature","Construct","3/2","3/_","_/2","Scry","Scry 2",1]
Extruder = ["Extruder","Colourless","4 Cost","4 Colourless","Artifact Creature","Artifact","Creature","Juggernaut","4/3","4/_","_/3","Sacrifice","+_/+_","Echo","Echo 4",1]
Llanowar_Stalker = ["Llanowar Stalker","Green","1 Cost","1 Green","Creature","Elf Warrior","Elf","Warrior","1/1","1/_","_/1","+_/+_",1]
Tear_Asunder = ["Tear Asunder","Green","2 Cost","1 Colourless, 1 Green","Instant","Exile","Kicker","Kicker Black","Kicker 1 Colourless, 1 Black",1]
Duskshell_Crawler = ["Duskshell Crawler","Green","2 Cost","1 Colourless, 1 Green","Creature","Insect","0/3","0/_","_/3","+_/+_","Trample",1]
Llanowar_Loamspeaker = ["Llanowar Loamspeaker","Green","2 Cost","1 Colourless, 1 Green","Creature","Elf Druid","Elf","Druid","1/3","1/_","_/3","Add Mana","Land Transform","Elemental","Haste",1]
Deathbloom_Gardener = ["Deathbloom Gardener","Green","3 Cost","2 Colourless, 1 Green","Creature","Elf Druid","Elf","Druid","1/1","1/_","_/1","Deathtouch","Add Mana",1]
Tireless_Provisioner = ["Tireless Provisioner","Green","3 Cost","2 Colourless, 1 Green","Creature","Elf Scout","Elf","Scout","3/2","3/_","_/2","Landfall","Food Token","Token Create","Treasure Token","Token Create",1]
Magnigoth_Sentry = ["Magnigoth Sentry","Green","4 Cost","3 Colourless, 1 Green","Creature","Treefolk","4/4","4/_","_/4","Reach",1]
Lonis_Cryptozoologist = ["Lonis, Cryptozoologist","Green-Blue","2 Cost","1 Green, 1 Blue","Legendary Creature","Legendary","Creature","Snake Elf Scout","Snake Elf","Elf Scout","Snake Scout","Snake","Elf","Scout","1/2","1/_","_/2","Investigate","Clues","Sacrifice",1]
Ronas_Vortex = ["Rona's Vortex","Blue","1 Cost","1 Blue","Instant","Kicker","Kicker Black","Kicker 2 Colourless, 1 Black",1]
Essence_Scatter = ["Essence Scatter","Blue","2 Cost","1 Colourless, 1 Blue","Instant","Counter",1]
Haunting_Figment = ["Haunting Figment","Blue","2 Cost","1 Colourless, 1 Blue","Creature","Illusion","2/1","2/_","_/1","Vigilance","Unblockable",1]
Burdened_Aerialist = ["Burdened Aerialist","Blue","3 Cost","2 Colourless, 1 Blue","Creature","Human Pirate","Human","Pirate","3/1","3/_","_/1","Treasure Token","Token Create","Flying",1]
Chrome_Courier = ["Chrome Courier","White-Blue","3 Cost","1 Colourless, 1 White, 1 Blue","Artifact Creature","Artifact","Creature","Thopter","1/1","1/_","_/1","Flying","Gain Life",1]
Runic_Shot = ["Runic Shot","White","1 Cost","1 White","Sorcery","Kicker","Kicker Blue","Destroy","Scry","Scry 2",1]
Arcbound_Mouser = ["Arcbound Mouser","White","1 Cost","1 White","Artifact Creature","Artifact","Creature","Cat","0/0","0/_","_/0","Lifelink","Modular","Modular 1","+_/+_",1]
Piercing_Rays = ["Piercing Rays","White","2 Cost","1 Colourless, 1 White","Sorcery","Exile","Forecast","Forecast 3","Forecast 2 Colourless, 1 White",1]
Skyblades_Boon = ["Skyblade's Boon","White","2 Cost","1 Colourless, 1 White","Enchantment","Aura","+_/+_","Flying",1]
Juniper_Order_Rootweaver = ["Juniper Order Rootweaver","White","2 Cost","1 Colourless, 1 White","Creature","Human Druid","Human","Druid","2/2","2/_","_/2","Kicker","Kicker Green","Kicker 1 Green","+_/+_",1]
Join_Forces = ["Join Forces","White","3 Cost","2 Colourless, 1 White","Instant","Untap","+_/+_",1]
Charismatic_Vanguard = ["Charismatic Vanguard","White","3 Cost","2 Colourless, 1 White","Creature","Dwarf Soldier","Dwarf","Soldier","3/2","3/_","_/2","+_/+_",1]
Argivian_Phalanx = ["Argivian Phalanx","White","6 Cost","5 Colourless, 1 White","Creature","Human Kor Soldier","Human Kor","Kor Soldier","Human Soldier","Human","Kor","Soldier","4/4","4/_","_/4","Vigilance",1]
Landscaper_Colos = ["Landscaper Colos","White","6 Cost","5 Colourless, 1 White","Creature","Goat Beast","Goat","Beast","4/6","4/_","_/6","Basic Landcycling",1]
Baird_Argivian_Recruiter = ["Baird, Argivian Recruiter","Red-White","2 Cost","1 Red, 1 White","Legendary Creature","Legendary","Creature","Human Soldier","Human","Soldier","2/2","2/_","_/2","Soldier Token","Token Create",1]
Astor_Bearer_of_Blades = ["Astor, Bearer of Blades","Red-White","4 Cost","2 Colourless, 1 Red, 1 White","Legendary Creature","Legendary","Creature","Human Warrior","Human","Warrior","4/4","4/_","_/4",1]
Smash_to_Dust = ["Smash to Dust","Red","2 Cost","1 Colourless, 1 Red","Sorcery","Destroy","Deal _ Damage",1]
Kaleidoscorch = ["Kaleidoscorch","Red","2 Cost","1 Colourless, 1 Red","Sorcery","Deal _ Damage","Flashback","Flashback Red","Flashback 4 Colourless, 1 Red",1]
Lightning_Strike = ["Lightning Strike","Red","2 Cost","1 Colourless, 1 Red","Instant","Deal _ Damage",1]
Lightning_Spear = ["Lightning Spear","Red","2 Cost","1 Colourless, 1 Red","Artifact","Equiptment","+_/+_","Trample","Deal _ Damage",1]
Goblin_Picker = ["Goblin Picker","Red","2 Cost","1 Colourless, 1 Red","Creature","Goblin","2/2","2/_","_/2","Discard Card","Draw Card",1]
Keldon_Strike_Team = ["Keldon Strike Team","Red","3 Cost","2 Colourless, 1 Red","Creature","Human Warrior","Human","Warrior","3/1","3/_","_/1","Kicker","Kicker White","Kicker 1 Colourless, 1 White","Soldier Token","Token Create","Haste",1]
Bone_Splinters = ["Bone Splinters","Black","1 Cost","1 Black","Sorcery","Sacrifice","Destroy",1]
Tribute_to_Urborg = ["Tribute to Urborg","Black","2 Cost","1 Colourless, 1 Black","Instant","Kicker","Kicker Blue","Kicker 1 Colourless, 1 Blue","-_/-_",1]
Aggressive_Sabotage = ["Aggressive Sabotage","Black","3 Cost","2 Colourless, 1 Black","Sorcery","Kicker","Kicker Red","Kicker 1 Red","Discard","Deal _ Damage",1]
Loathsome_Curator = ["Loathsome Curator","Black","5 Cost","4 Colourless, 1 Black","Creature","Gorgon Wizard","Gorgon","Wizard","5/4","5/_","_/4","Exploit","Menace","Destroy",1]
Writhing_Necromass = ["Writhing Necromass","Black","7 Cost","6 Colourless, 1 Black","Creature","Zombie Giant","Zombie","Giant","5/5","5/_","_/5","Deathtouch",1]

Cards_Booster = [Vanquishers_Axe,Salvaged_Manaworker,Relic_of_Legends,Automatic_Librarian,Extruder,Llanowar_Stalker,Tear_Asunder,Duskshell_Crawler,Llanowar_Loamspeaker,Deathbloom_Gardener,Tireless_Provisioner,Magnigoth_Sentry,Lonis_Cryptozoologist,Ronas_Vortex,Essence_Scatter,Haunting_Figment,Burdened_Aerialist,Chrome_Courier,Runic_Shot,Arcbound_Mouser,Piercing_Rays,Skyblades_Boon,Juniper_Order_Rootweaver,Join_Forces,Charismatic_Vanguard,Argivian_Phalanx,Landscaper_Colos,Baird_Argivian_Recruiter,Astor_Bearer_of_Blades,Smash_to_Dust,Kaleidoscorch,Lightning_Strike,Lightning_Spear,Goblin_Picker,Keldon_Strike_Team,Bone_Splinters,Tribute_to_Urborg,Aggressive_Sabotage,Loathsome_Curator,Writhing_Necromass]

Card_List = [Isperia_Supreme_Judge,Archon_of_Redemption,Cartographers_Hawk,Cleansing_Nova,Emeria_Angel,Gideon_Jura,Hanged_Executioner,Remorseful_Cleric,Sephara_Skys_Blade,SteelPlume_Marshal,Storm_Herd,True_Conviction,Angler_Turtle,Bident_of_Thassa,Diluvian_Primordial,EverWatching_Threshold,Faerie_Formation,Gravitational_Shift,Inspired_Sphinx,Sharding_Sphinx,Sphinx_of_Enlightenment,Windreader_Sphinx,Absorb,Skycat_Sovereign,Sphinxs_Revelation,Time_Wipe,Aven_Gagglemaster,Banishing_Light,Condemn,Crush_Contraband,Disenchant,Generous_Gift,Kangees_Lieutenant,Rally_of_Wings,Soul_Snare,Swords_to_Plowshares,Vow_of_Duty,Aetherize,Counterspell,Favorable_Winds,Negate,Tide_Skimmer,Warden_of_Evos_Isle,Winged_Words,Cloudblazer,Empyrean_Eagle,Jubilint_Skybonder,Kangee_Sky_Warden,Migratory_Route,Staggering_Insight,Thunderclap_Wyvern,Arcane_Signet,Azorius_Signet,Commanders_Sphere,Hedron_Archive,Pilgrims_Eye,Sky_Diamond,Skyscanner,Sol_Ring,Talisman_of_Progress,Thought_Vessel,Dreamshackle_Geist,Extraction_Specialist,Stormrider_Spirit,Nebelgast_Beguiler,Consuming_Tide,Hullbreaker_Horror,Brute_Suit,Wretched_Throng,Fading_Hope,Kill_Shot,Backup_Agent,Unholy_Officiant,Inspiring_Overseer,Welcoming_Vampire,Serpentine_Ambush,SevenTail_Mentor,Witchs_Web,Flourishing_Hunter,Burn_the_Accursed,Spore_Crawler,HighRise_Sawjack,Topiary_Stomper,Timberland_Guide,Mounted_Dreadknight,Lambholt_Harrier,Thundering_Raiju,Voldaren_Stinger,Abrade,Creepy_Puppeteer,Glorious_Sunrise,Ascendant_Packleader,Vanquishers_Axe,Salvaged_Manaworker,Relic_of_Legends,Automatic_Librarian,Extruder,Llanowar_Stalker,Tear_Asunder,Duskshell_Crawler,Llanowar_Loamspeaker,Deathbloom_Gardener,Tireless_Provisioner,Magnigoth_Sentry,Lonis_Cryptozoologist,Ronas_Vortex,Essence_Scatter,Haunting_Figment,Burdened_Aerialist,Chrome_Courier,Runic_Shot,Arcbound_Mouser,Piercing_Rays,Skyblades_Boon,Juniper_Order_Rootweaver,Join_Forces,Charismatic_Vanguard,Argivian_Phalanx,Landscaper_Colos,Baird_Argivian_Recruiter,Astor_Bearer_of_Blades,Smash_to_Dust,Kaleidoscorch,Lightning_Strike,Lightning_Spear,Goblin_Picker,Keldon_Strike_Team,Bone_Splinters,Tribute_to_Urborg,Aggressive_Sabotage,Loathsome_Curator,Writhing_Necromass," "]

#####----- Lands -----#####
Definer_Lands = ["___Lands:___"]
###--- Basic ---###
Island = ["Island","Blue","Blue Land","Basic Land","Basic","Land","Island",26]
Plains = ["Plains","White","White Land","Basic Land","Basic","Land","Plains",27]
Mountain = ["Mountain","Red","Red Land","Basic Land","Basic","Land","Mountain",13]

###--- Other ---###
Rustvale_Bridge = ["Rustvale Bridge","Red-White","Artifact Land","Artifact","Land","Indestructible","Red","White","Red Land","White Land",1]
Drossforge_Bridge = ["Drossforge Bridge","Black-Red","Artifact Land","Artifact","Land","Indestructible","Black","Red","Black land","Red Land",1]
Crystal_Grotto = ["Crystal Grotto","Colourless","Colourless Land","Land","Scry","Scry 1",1]
Moorland_Haunt = ["Moorland Haunt","Colourless","Colourless Land","Land","Exile","Spirit Token","Token Create",1]
Port_Town = ["Port Town","White-Blue","White-Blue Land","Land",1]
Prairie_Stream = ["Prairie Stream","White-Blue","White-Blue Land","Land",1]
Temple_of_Enlightenment = ["Temple of Enlightenment","White-Blue","White-Blue Land","Land","Scry","Scry 1",1]
Coastal_Tower = ["Coastal Tower","White-Blue","White-Blue Land","Land",1]
Command_Tower = ["Command Tower","Colourless","Colourless Land","Land",1]
Meandering_River = ["Meandering River","White-Blue","White-Blue Land","Land",1]
Sejiri_Refuge = ["Sejiri Refuge","White-Blue","White-Blue Land","Land","Gain Life",1]
Tranquil_Cove = ["Tranquil Cove","White-Blue","White-Blue Land","Land","Gain Life",5]
Rugged_Highland = ["Rugged Highland","Red-Green","Red-Green Land","Land","Gain Life",4]

Land_List = [Island,Plains,Mountain,Crystal_Grotto,Rustvale_Bridge,Drossforge_Bridge,Moorland_Haunt,Port_Town,Prairie_Stream,Temple_of_Enlightenment,Coastal_Tower,Command_Tower,Meandering_River,Sejiri_Refuge,Tranquil_Cove,Rugged_Highland," "]

#####----- Tokens -----#####
Definer_Tokens = ["___Tokens:___"]
###--- Single Side ---###
Treasure_Token = ["TREASURE","Colourless","Token Artifact","Token","Artifact","Treasure","Add Mana",1]
Badger_Token = ["BADGER","Green","Token Creature","Token","Creature","Badger","3/3","3/_","_/3",1]

Bird_Token = ["BIRD","White","Token Creature","Token","Creature","Bird","1/1","1/_","_/1","Flying","Dual Sided",4]
Spirit_Token = ["Spirit","White","Token Creature","Token","Creature","Spirit","1/1","1/_","_/1","Flying","Dual Sided",3]
Faerie_Token = ["FAERIE","Blue","Token Creature","Token","Creature","Faerie","1/1","1/_","_/1","Flying","Dual Sided",3]
Cat_Bird_Token = ["CAT BIRD","White","Token Creature","Token","Creature","Cat Bird","Cat","Bird","1/1","1/_","_/1","Flying","Dual Sided",3]
Pegasus_Token = ["PEGASUS","White","Token Creature","Token","Creature","Pegasus","1/1","1/_","_/1","Flying","Dual Sided",2]
Elephant_Token = ["ELEPHANT","Green","Token Creature","Token","Creature","Elephant","3/3","3/_","_/3","Dual Sided",1]
Thopter_Token_Blue = ["THOPTER","Blue","Token Artifact Creature","Token Artifact","Token Creature","Artifact Creature","Token","Artifact","Creature","Thopter","1/1","1/_","_/1","Flying","Dual Sided",2]
Thopter_Token_Colourless = ["THOPTER","Colourless","Token Artifact Creature","Token Artifact","Token Creature","Artifact Creature","Token","Artifact","Creature","Thopter","1/1","1/_","_/1","Flying","Dual Sided",2]

###--- Dual Side ---###
Bird__Spirit = ["Bird / Spirit",Bird_Token,Spirit_Token,2]
Bird__Thopter = ["Bird / Thopter",Bird_Token,Thopter_Token_Blue,1]
Bird__Faerie = ["Bird / Faerie",Bird_Token,Faerie_Token,1]
Cat_Bird__Thopter = ["Cat Bird / Thopter",Cat_Bird_Token,Thopter_Token_Colourless,1]
Cat_Bird__Spirit = ["Cat Bird / Spirit",Cat_Bird_Token,Spirit_Token,1]
Cat_Bird__Faerie = ["Cat Bird / Faerie",Cat_Bird_Token,Faerie_Token,1]
Pegasus__Thopter = ["Pegasus / Thopter",Pegasus_Token,Thopter_Token_Blue,1]
Pegasus__Faerie = ["Pegasus / Faerie",Pegasus_Token,Faerie_Token,1]
Elephant__Thopter = ["Elephant / Thopter",Elephant_Token,Thopter_Token_Colourless,1]

Token_List = [Treasure_Token,Badger_Token,Bird__Spirit,Bird__Thopter,Cat_Bird__Thopter,Cat_Bird__Spirit,Cat_Bird__Faerie,Pegasus__Faerie,Pegasus__Thopter,Elephant__Thopter," "]

#####----- Status Definitions -----#####
Definer_Status = ["___Status Conditions:___"]
Flying = ["Flying","When attacking, it can only be blocked by a creature with Reach or Flying."]
Lifelink = ["Lifelink","When this creature deals damage, gain life equal to its attack."]
Deathtouch = ["Deathtouch","When this card deals damage to a creature or planeswalker, the target card dies."]
Hexproof = ["Hexproof","This card can't be the target of spells and effects."]
First_Strike = ["First Strike","When this card attacks, it attacks during the First Strike phase."]
Double_Strike = ["Double Strike","When this card attacks, it attacks during the First Strike phase and during the normal attack phase."]
Indestructible = ["Indestructible","Damage and effects that say 'destroy' don't destroy them."]
Basic_Landcycling = ["Basic Landcycling","Discard this card: Search your library for a basic land card, reveal it, put it in your hand, then shuffle."]
Encore = ["Encore","---Undefined---"]
Flashback = ["Flashback","You may cast this card from your graveyard for its flashback cost. Then exile it."]
Kicker = ["Kicker","You may pay an additional x as you cast this spell."]
Vigilance = ["Vigilance","This card doesn't tap when attacking or blocking."]
Modular = ["Modular","This creature enters the battlefield with a +1/+1 counter on it. When it dies, you may put its +1/+1 counters on target artifact creature."]
Forecast = ["Forecast","Tap target untapped creature (Activate this ability only during your upkeep and only once each turn.)"]
Scry = ["Scry","Look at the top card of your library. You may put that card on the bottom of your library."]
Investigate = ["Investigate","---Undefined---"]
Reach = ["Reach","This card can block flying creatures."]
Landfall = ["Landfall","Whenever a land enters the battlefield under your control, activate effect."]
Echo = ["Echo","---Undefined---"]
Hexresistant = ["Hexresistant","Spells your opponents cast that target this creature cost (x) more to cast"]
Flash = ["Flash","This spell can be cast as though its an instant."]
Haste = ["Haste","This creature, when summoned, doesn't get summoning sickness."]
Equip = ["Equip","Attach to target creature you control. Equip only as a sorcery."]
Crew = ["Crew","Tap any number of creatures you control with total power 1 or more: This Vehicle becomes an artifact creature until end of turn."]
Trample = ["Trample","When this card is blocked, if its damage would reduce the blocking card below 0, and extra damage carries over to the original target."]
Menace = ["Menace","When this card attacks, it can only be blocked by two or more cards."]
Exploit = ["Exploit","When this creature enters the battlefield, you may sacrifice a creature."]

Status_List = [Flying,Lifelink,Deathtouch,Hexproof,First_Strike,Double_Strike,Indestructible,Basic_Landcycling,Encore,Flashback,Kicker,Vigilance,Modular,Forecast,Scry,Investigate,Reach,Landfall,Echo,Hexresistant,Flash,Haste,Crew,Trample,Menace,Exploit," "]

All_List = [Card_List,Land_List,Token_List,Status_List]

SlowMode = False

for x in All_List:
  for y in x:
    print(y[0])

while True:
  input()
  print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
  Check = input('Search for what? ')
  Valid_Found = []

  if Check == "Break":
    break

  if Check == "Card Amount":
    for x in All_List:
      if x != Status_List:
        for y in x:
          if y != " ":
            print(f"{y[0]} - x{y[len(y)-1]}")

  if Check == "Specs":
    Search_Card = input("What is the name of the thing you are looking for? ")
    for x in All_List:
      for y in x:
        if Search_Card in y[0]:
          print("- ", end="")
          for z in y:
            print(f"{z} - ", end="")
          print()
  
  if Check == "Speed Toggle":
    if SlowMode: SlowMode = False
    else: SlowMode = True
    print(SlowMode)

  if Check == "Sort":
    SortType = input("Sort type? ")
    if SortType == 'Alphabetise':
      Alph_What = input("Alphabetise what? ")
      if Alph_What == 'All':
        for x in All_List:
          for y in x:
            Valid_Found.append(y[0])
      if Alph_What == 'Cards':
        for x in Card_List:
          Valid_Found.append(x[0])
      if Alph_What == 'Lands':
        for x in Land_List:
          Valid_Found.append(x[0])
      if Alph_What == 'Tokens':
        for x in Token_List:
          Valid_Found.append(x[0])
    CostX = []
    Cost0 = []
    Cost1 = []
    Cost2 = []
    Cost3 = []
    Cost4 = []
    Cost5 = []
    Cost6 = []
    Cost7 = []
    Cost8 = []
    Cost9 = []
    Cost10 = []
    Cost11 = []
    Cost12 = []
    if SortType == 'Cost':
      for y in Card_List:
        for x in y:
          if x == "X Cost":
            CostX.append(y[0])
          if x == "0 Cost":
            Cost0.append(y[0])
          if x == "1 Cost":
            Cost1.append(y[0])
          if x == "2 Cost":
            Cost2.append(y[0])
          if x == "3 Cost":
            Cost3.append(y[0])
          if x == "4 Cost":
            Cost4.append(y[0])
          if x == "5 Cost":
            Cost5.append(y[0])
          if x == "6 Cost":
            Cost6.append(y[0])
          if x == "7 Cost":
            Cost7.append(y[0])
          if x == "8 Cost":
            Cost8.append(y[0])
          if x == "9 Cost":
            Cost9.append(y[0])
          if x == "10 Cost":
            Cost10.append(y[0])
          if x == "11 Cost":
            Cost11.append(y[0])
          if x == "12 Cost":
            Cost12.append(y[0])
      CostX.sort()
      Cost0.sort()
      Cost1.sort()
      Cost2.sort()
      Cost3.sort()
      Cost4.sort()
      Cost5.sort()
      Cost6.sort()
      Cost7.sort()
      Cost8.sort()
      Cost9.sort()
      Cost10.sort()
      Cost11.sort()
      Cost12.sort()
      In_or_Ex = input("Incline or Excline? ")
      if In_or_Ex == "Incline":
        print("___X Costs___")
        for x in CostX:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___0 Costs___")
        for x in Cost0:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___1 Costs___")
        for x in Cost1:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___2 Costs___")
        for x in Cost2:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___3 Costs___")
        for x in Cost3:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___4 Costs___")
        for x in Cost4:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___5 Costs___")
        for x in Cost5:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___6 Costs___")
        for x in Cost6:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___7 Costs___")
        for x in Cost7:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___8 Costs___")
        for x in Cost8:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___9 Costs___")
        for x in Cost9:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___10 Costs___")
        for x in Cost10:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___11 Costs___")
        for x in Cost11:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___12 Costs___")
        for x in Cost12:
          print(x, end="")
          if SlowMode == True: input()
          else: print()

      if In_or_Ex == "Excline":
        print("___12 Costs___")
        for x in Cost12:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___11 Costs___")
        for x in Cost11:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___10 Costs___")
        for x in Cost10:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___9 Costs___")
        for x in Cost9:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___8 Costs___")
        for x in Cost8:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___7 Costs___")
        for x in Cost7:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___6 Costs___")
        for x in Cost6:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___5 Costs___")
        for x in Cost5:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___4 Costs___")
        for x in Cost4:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___3 Costs___")
        for x in Cost3:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___2 Costs___")
        for x in Cost2:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___1 Costs___")
        for x in Cost1:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___0 Costs___")
        for x in Cost0:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
        print("___X Costs___")
        for x in CostX:
          print(x, end="")
          if SlowMode == True: input()
          else: print()
    if SortType == 'Colour':
      BlackCards = []
      BlueCards = []
      GreenCards = []
      RedCards = []
      WhiteCards = []
      ColourlessCards = []
      if Alph_What == 'All':
        for x in All_List:
          for y in x:
            if y[1] == "Black":
              BlackCards.append(y[0])
            if y[1] == "Blue":
              BlueCards.append(y[0])
            if y[1] == "Green":
              GreenCards.append(y[0])
            if y[1] == "Red":
              RedCards.append(y[0])
            if y[1] == "White":
              WhiteCards.append(y[0])
            if y[1] == "Colourless":
              ColourlessCards.append(y[0])
      if Alph_What == 'Cards':
        for x in Card_List:
          Valid_Found.append(x[0])
      if Alph_What == 'Lands':
        for x in Land_List:
          Valid_Found.append(x[0])
      if Alph_What == 'Tokens':
        for x in Token_List:
          Valid_Found.append(x[0])
  
  for x in All_List:
    for y in x:
      for z in y:
        if Check in str(z):
          Valid_Found.append(y[0])

  Valid_Found = list(set(Valid_Found))
  Valid_Found.sort()

  for x in Valid_Found:
    print(x)