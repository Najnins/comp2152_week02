# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]
combatStrength = int(input("Enter your combat Strength (1-6): "))
mCombatStrength = int(input("Enter the monster's combat Strength (1-6): "))

if not (1 <= combatStrength <= 6 and 1 <= mCombatStrength <= 6):
    print("Combat Strength values must be between 1 and 6.")
    exit()

# Define weapons array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Roll the dice for weapon selection
input("Roll the dice to select your weapon (Press enter)")
weaponRoll = random.choice(diceOptions)
print("You rolled a " + str(weaponRoll))

# Select the weapon based on the roll
selectedWeapon = weapons[weaponRoll - 1]
print(f"Your weapon is: {selectedWeapon}")

# Add weaponRoll to hero's combat strength
combatStrength += weaponRoll
print(f"Your updated combat strength is: {combatStrength}")

# Conditional responses based on weaponRoll
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

if selectedWeapon != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Proceed with the fight logic (existing code adjusted for clarity)
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print(f"Your {selectedWeapon} ({combatStrength}) ---> Monster ({mCombatStrength})")
if combatStrength >= mCombatStrength:
    print("You've killed the monster")
else:
    mCombatStrength -= combatStrength
    print(f"You've reduced the monster's strength to: {mCombatStrength}")
    print("The monster strikes back!!!")

    if mCombatStrength >= numLives:
        numLives = 0
        print("You're dead")
    else:
        numLives -= mCombatStrength
        print(f"The monster has reduced your lives to: {numLives}")
