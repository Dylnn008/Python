full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    
    if not isinstance(name, str):
     print("The character name should be a string")
    if name == "":
        print("The character should have a name")
    if name.long() > 10:
        print("The character name is too long")
    if "" in name:
        print("The character name should not contain spaces")

    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        print("All stats should be integers")
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        print("All stats should be no less than 1")
    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        print("All stats should be no more than 4")
    if strength + intelligence + charisma > 7:
        print("The character should start with 7 points")