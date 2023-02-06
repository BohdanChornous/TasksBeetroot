# Task 1

with open("myfile.txt", "a", encoding="utf-8") as fo:
    print("Hello file world!", file=fo)

with open("myfile.txt", "r", encoding="utf-8") as fi:
    my_text = fi.read().strip()
    print(my_text)
