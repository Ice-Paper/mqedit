weapon_min_damage = 0
weapon_max_damage = 999

#Note this is the same as weapon damage quite literally however if the developer of the game decides to change it we have it here for that anyways
weapon_min_commit_damage = 0
weapon_max_commit_damage = 999

#The length of a weapons name!
weapon_name_max_char_length = 29
#The length of a weapons line desciption
weapon_desc_max_char_line_length = 31

#Can be applied to both names & descriptions but not weapon printed damage
weapon_fonts = ["\S", "\R", "\B", "\c", "\\n"]



weapon_data = ""

weapon_name = ""
weapon_desc = ""
weapon_base = 0
weapon_com1 = 0
weapon_com2 = 0
weapon_com3 = 0
weapon_icon = 0

weapon_effe = 0

#To seperate weapon name from weapon desc the game uses \t to parse that 
#At the start of a weapons text desc if you \S it will set the font style to [font 3]
#\S Special
#\R Red
#\B Blue
#\c Clear
#\\n new line


#   First value is used for the weapons text logo
#   Weapon icon 0 = Sword
#   Weapon icon 1 = Staff
#   Weapon icon 2 = Aim

if weapon_icon == 0:
    # Sword icon
    pass

if weapon_icon == 1:
    # Staff icon
    pass

if weapon_icon == 2:
    # Aim icon
    pass

#   D values and their meanings
#   d 0  = Slow
#   d 1  = Aim down
#   d 2  = BLANK /Not implemented
#   d 3  = Attack down
#   d 4  = Holy Attack down
#   d 5  = Fire Attack down
#   d 6  = Ice Attack down
#   d 7  = Posion Attack down
#   d 8  = Currupt Attack down?

#   d 9  = Sheild down
#   d 10 = Holy Sheild down
#   d 11 = Fire Sheild down
#   d 12 = Ice Sheild down
#   d 13 = Poison Sheild down
#   d 14 = Currupt Sheild down?
#   d 15 = [damage mod] = Poison ? but oddly the poison damage is nuts at times
#   d 16 = Fire damge (Goes down by 1 each turn)
#   d 17 = Not mobile
#   d 18 = Curse damage



#   Second value is used for range
#   1 = 1 tile in each radius
#   2 = 3 horizontal and verticle filled in a star shape
#   3 = 3 horizontal and verticle unfilled
#   0 = NO attack
#   4 = Error no attack


#Last value is unkown but all weapons use 0

default_weapon_names = [
    "Ornamental Katana", 
    "Acolyte's Staff", 
    "Blessed Dagger", 
    "Poisoned Dagger",
    "Fire Sword",
    "Doomender",
    "Candelstabra",
    "Glue Stick",
    "fast sword",
    "faster sword",
    "Simple Crossbow"
    ]

default_weapon_desc = [
    "Impressive, shiny, and\npossibly even capable of\ncutting something.\n\nBase damage: \\a0010\nCommit 1: \\a0014\nCommit 2: \\a0018\nCommit 3: \\a0022",
    "It's just a stick.\n\nBase: \\a0010, pushes target 1 space\nCommit 1: \\a0010, pushes 2 spaces\nCommit 2: \\a0010, pushes 3 spaces\nCommit 3: \\a0020, pushes 3 spaces\nInflicts extra damage if \nsomething is in the way",
    "Made of purest copper to drive\nback the darkness.\n\nBase damage: \\a0010\nCommit 1: \\a0013 or \\a1013\nCommit 2: \\a0016 or \\a1016\nCommit 3: \\a0019 or \\a1019\nUses whichever damage type is\nmore effective against the\ntarget.",
    "flavor text\n\nBase damage: \\a0010\nCommit 1: \\a4010\nCommit 2: \\a4015\nCommit 3: \\a4015, poisons target (5\S4\c per turn for 5 turns)",
    "A significant improvement over earlier designs; this time, only the blade is on fire.\n\nBase damage: \\a0015\nCommit 1: \\a2020\nCommit 2: \\a2025\nCommit 3: \\a2030, ignites target (fire damage each turn, starting at 5\S2\c and decreasing over time)",
    "\Sfor debug purposes only\c\n\nBase damage: \\a0999\nCommit 1: \\a1999\nCommit 2: \\a2999\nCommit 3: \\a3999",
    "Two blades are better than one.\nNot sure about three, though.\n\nDoes secondary damage to\ndiagonally-adjacent enemies\nBase damage: \\a0010\nCommit 1: \\a0010 / \\a0005\nCommit 2: \\a0015 / \\a0010\nCommit 3: \\a2015 / \\a2015",
    "It's sticky.\n\nBase damage: \\a0010, push 1\nCommit 1: \\a0010, push 1, slow 1\nCommit 2: \\a0010, push 1, slow 2\nCommit 3: \\a0010, push 1, slow 3\n\n(Each turn, the target's\n movement will be decreased by\n the intensity of the slow\n effect, then the slow effect\n will decrease by 1)",
    "fast",
    "more fast",
    "it shoots things"
]

#Different Styles of weapon damage
default_weapon_damage_type = ["d ", "a ", "p ", "r ", "s "]

#This effects fire damage & poison but not the glue stick
default_weapon_effect_mod = 5