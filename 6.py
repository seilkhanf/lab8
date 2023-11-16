import string

def translater():
    for char in string.ascii_uppercase:
        named = f"{char}.txt"
        with open(named, 'w') as file:
            file.write(f"files {char}")
        print(f" {named} new")