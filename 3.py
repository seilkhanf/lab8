import os

def analisis(path):
    if os.path.exists(path):
        print(f"exists: {path}")
        
        directory, filename = os.path.split(path)
        print(f"direct: {directory}")
        print(f"fname: {filename}")
    else:
        print(f"existss: {path}")