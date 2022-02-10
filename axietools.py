#Axie Tools

#Damage Calculator

import math
          
def damage_calc():
    print("1: Reptile, Plant, Dusk")
    print("2: Aqua, Bird, Dawn")
    print("3: Beast, Bug, Mech")

    att_type = int(input("Attacker type: "))
    def_type = int(input("Defender type: "))

    skill = int(input("Axie skill level: "))

    if att_type == def_type:
        type_bonus = 1
    
    if att_type == 1:
        if def_type == 2:
            type_bonus = 1.15
        if def_type == 3:
            type_bonus = 0.85
    if att_type == 2:
        if def_type == 3:
            type_bonus = 1.15
        if def_type == 1:
            type_bonus = 0.85
    if att_type == 3:
        if def_type == 1:
            type_bonus = 1.15
        if def_type == 2:
            type_bonus = 0.85  

    print("Enter the damage written on the card")
    base_damage = int(input("Card base damage: "))

    print("If an effect is triggered, in decimal(120% type in 1.20), if no bonus is triggered type 1")
    effect_bonus = float(input("Card effect bonus: "))

    print("1: If axie type is the same as card type")
    print("2: If axie type is NOT the same as card type")
    print("3: If Dusk with REP/PLNT, Dawn with BRD/AQ, Mech with BST/BU")

    card_type = int(input("Card type: "))

    if card_type == 1:
        card_bonus = 1.1
    if card_type == 2:
        card_bonus = 1
    if card_type == 3:
        card_bonus = 1.075

    print("If critical (ie. ronin) enter 1 if not enter 0")
    is_crit = int(input("Is crit?: "))
    if is_crit == 1:
        crit = 2
    else:
        crit = 1

    skill_bonus = base_damage * ((skill * 0.55 - 12.25)/100) * 0.985

    total_damage = base_damage * type_bonus * effect_bonus * card_bonus * crit + skill_bonus

    print("Total Damage is: ", math.floor(total_damage))
    menu()

def energy_calc():
    energy = 3
    rnd = 1

    while True:
        if energy >= 10:
            energy = 10
        if energy <= 0:
            energy = 2
        if rnd >= 10:
            print("Bloodmoon")
            
        print("Round ", rnd)
        print("Energy count: ", energy)
        print("-----------------------")
        use = int(input("Energy used: "))

        gain = int(input("Energy gained: "))
        
        dest = int(input("Energy destroyed: "))
        print("-----------------------")
        
        energy = energy - use + gain - dest + 2
        rnd += 1

def menu():
    print("1: Damage Calculator")
    print("2: Energy Calc") 
    print("9: Exit/Menu")
    sel = int(input("What to do?: "))

    if sel == 1:
        damage_calc()
    if sel == 2:
        energy_calc()
    else:
        menu()

if __name__ == "__main__":
    menu()
        
