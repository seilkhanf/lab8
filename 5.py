def fileslist(path, dota):
    try:
        with open(path, 'w') as file:
            for item in dota:
                file.write(str(item) + '\n')
        print(f"List successfully written to {path}")
    except IOError:
        print(f"Error writing to {path}")