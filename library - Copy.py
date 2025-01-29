a = input("see, add, edit, or delete? ").lower()

#see works
if a  == "see":
    b = open("library.csv")
    print(b.read())
    b.close()
#add works
elif a == "add":
    b = open("library.csv",'a')
    f = input("what is the name of the book you'd like to add?(do not use special characters) ")
    b.write("\n" + f)
    d = input("who is the author of this book? ")
    e = input("When is the publication date? ")
    b.write(", " + d + ", "+ e)
#edit
elif a == "edit":
    b = open("library.csv","r")
    c = b.read()
    d = input("What book would you like to edit? ").lower()
    i = input("would you like to edit the name, date, or author?").lower()
    e = input("what would you like to edit it to?")
    if i == "name":
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
    elif i == "date":
        g = open("library.csv")
        g = g.read()
        p = g.index(d)
        x = slice(p,-1)
        o = g[x].index("$")
        n = slice(o)
        o = o + p
        h = slice(0,o)
        u = slice(o+6,-1)
        s = g[h] +"$"+ e +","+ g[u] + ","
        l = open("library.csv","w")
        l.write(s)
    elif i == "author":
        g = open("library.csv")
        g = g.read()
        p = g.index(d)
        x = slice(p,-1)
        o = g[x].index("@")
        n = slice(o)
        o = o + p
        h = slice(0,o)
        w = g[x].index("*")
        w= w + p
        u = slice(w,-1)
        s = g[h] +"@"+ e +"*"+ g[u] + ","
        l = open("library.csv","w")
        l.write(s)
    else:
        "please choose one of the suggested options."
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
        y = g[h].index("\n")
        y = y + len(g[l]) + len(d)
        i = slice(y + 2,-1)
        u = g[l] + g[i] + ","
        s = open("library.csv","w")
        s.write(u)
    else:
        print("not found. try again later, or check your spelling.")
else:
    print("please choose a suggested input.")