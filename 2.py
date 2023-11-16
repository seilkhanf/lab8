def accs(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    if os.access(path, os.R_OK):
        print(f"read '{path}' is allowed.")
    else:
        print(f"do not read '{path}'.")

    if os.access(path, os.W_OK):
        print(f"write '{path}' is allowed.")
    else:
        print(f"do not write '{path}'.")

    if os.access(path, os.X_OK):
        print(f"Execute '{path}' is allowed.")
    else:
        print(f"No execute '{path}'.")


checking = input("path ")
accs(checking)