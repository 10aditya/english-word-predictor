import re

with open("full_words.txt", "r") as f:
    words = f.read()
    print(len(words))

print("Enter ! to stop.")

ip = input("type...\n")

while True:
    pat = ' ip(?:[a-zA-z])* [a-zA-Z]?'.replace('ip', ip)
    reg = re.compile(pat, re.IGNORECASE)
    sugg = reg.findall(words)
    sugg.sort(key=len)
    op = []

    for sug in sugg[:5]:
        op.append(sug.split(' ')[1])

    print(op)
    ip = ip+input(ip)

    if ip[-1:] == '!':
        print(sugg)
        break
