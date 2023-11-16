import os

def deleting(path):
    try:
        if os.path.exists(path):
            if os.access(path, os.W_OK):
                os.remove(path)
                print(f"deleting {path}")
            else:
                print(f"cannot delete {path}")
        else:
            print(f"no founded {path}")
    except Exception as e:
        print(f"error of deletsf: {e}")