a = input("see, edit, add, or delete? ").lower()

#see works
if a  == "see":
    b = open("library.csv")
    print(b.read())
    b.close()
#edit
elif a == "edit":
    b = open("library.csv")
    e = b.read()
    c = input("what is the name or author of the book you'd like to edit? ").lower()
    if c in e:
        d = input("what would you like to change? (book name, author, or publication date) ").lower()
        if d == "book name" or "name":
            print('placeholder')
        elif d  == "author":
            print("placeholder")
        elif d == "date" or "publication date":
            print("placeholder")
        else:
            print("Please choose a suggested input. ")
    else:
        print("book not found. try again later, or check for spelling errors.")
    b.close()
#add works
elif a == "add":
    b = open("library.csv",'a')
    f = input("what is the name of the book you'd like to add? ")
    b.write("\n" + f)
    d = input("who is the author of this book? ")
    e = input("When is the publication date? ")
    b.write(", " + d + ", "+ e)
#delete
elif a == "delete":
    b = open("library.csv","r")
    c = b.read()
    d = input("What book would you like to delete? ").lower()
    print(d)
    print(c)
    g = ""
    if d in c:
        p = c.index(d)
        print(p)
        x = slice(p,p+len(d))
        print(c[x])
        o = open("library.csv","r+")
        g = o.read()
        l = slice(0,p)
        h = slice(len(d)+p,-1)
        print(g[h]+ "a")
        print(g[l] + "b")
        u = g[h] + g[l]
        s = open("library.csv","w")
        s.write(u)
    else:
        print("not found. try again later, or check your spelling.")
else:
    print("please choose a suggested input.")