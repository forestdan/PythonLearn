def trim(str):
    s = list(str)
    while(s[:1] == [' ']):
        s = s[1:]
    while(s[-1:] == [' ']):
        s = s[:-1]
    return "".join(s)

print(trim("   This is my first str   "))