
def reverso(n):
    s = str(n)
    i = 0
    for x in range(len(s)):
        i += int(s[x]) * (10**x)
    return i

print(reverso(123456))