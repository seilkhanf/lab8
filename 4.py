def numbline(path):
    try:
        with open(path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"numbersline {path}: {line_count}")
    except FileNotFoundError:
        print(f"File not found: {path}")