a = input("see, add, edit, or delete? ").lower()

#see works
if a  == "see":
    b = open("library.csv")
    print(b.read())
    b.close()
#add works
elif a == "add":
    b = open("library.csv",'a')
    f = input("what is the name of the book you'd like to add? ")
    b.write("\n" + f)
    d = input("who is the author of this book? ")
    e = input("When is the publication date? ")
    b.write(", " + d + ", "+ e)
#edit works
elif a == "edit":
    b = open("library.csv","r")
    c = b.read()
    d = input("What book would you like to edit? ").lower()
    g = ""
    e = input("what would you like to edit it to?")
    if d in c:
        p = c.index(d)
        x = slice(p,p+len(d))
        o = open("library.csv","r+")
        g = o.read()
        l = slice(0,p)
        h = slice(len(d)+p+1,-1)
        u = g[l] + e + ',' + g[h] + ","
        s = open("library.csv","w")
        s.write(u)
        print("book edited")
    else:
        print("not found. try again later, or check your spelling.")
#delete works
elif a == "delete":
    b = open("library.csv","r")
    c = b.read()
    d = input("What book would you like to delete? ").lower()
    g = ""
    if d in c:
        p = c.index(d)
        x = slice(p,p+len(d))
        o = open("library.csv","r+")
        g = o.read()
        l = slice(0,p)
        h = slice(len(d)+p+1,-1)
        u = g[l] + g[h] + ","
        s = open("library.csv","w")
        s.write(u)
    else:
        print("not found. try again later, or check your spelling.")
else:
    print("please choose a suggested input.")