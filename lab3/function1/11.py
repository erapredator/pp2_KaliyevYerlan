def poli(word):
    newstr = word[::-1]
    if newstr == word:
        print("YES")
    else:
        print("NO")

s = input()
poli(s)