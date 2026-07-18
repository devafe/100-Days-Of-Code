full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif not character_name.strip():
        return 'The character should have a name'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif " " in character_name:
        return 'The character name should not contain spaces'
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if strength < 1 or charisma < 1 or intelligence < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or charisma > 4 or intelligence > 4:
        return 'All stats should be no more than 4'
    if strength + charisma + intelligence != 7:
        return 'The character should start with 7 points'
    strength_bar = full_dot * strength + empty_dot * (7 - strength)
    intelligence_bar = full_dot * intelligence + empty_dot * (7 - intelligence)
    charisma_bar = full_dot * charisma + empty_dot * (7 - charisma)
    return f'{character_name} \nSTR {strength_bar} \n INT {intelligence_bar} \n CHAR {charisma_bar}'
print(create_character('ren', 4, 2, 1 ))