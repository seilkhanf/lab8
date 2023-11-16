def files(path, pathdest):
    try:
        with open(path, 'r') as source_file:
            with open(pathdest, 'w') as destination_file:
                destination_file.write(source_file.read())
        print(f"cont of {path} to {pathdest}")
    except FileNotFoundError:
        print(f" not found: {path}")
    except IOError:
        print(f"oshibka copying contents from {path} to {pathdest}")