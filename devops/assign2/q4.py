with open("file.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines))