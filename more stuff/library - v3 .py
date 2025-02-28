import random
import datetime
from datetime import timedelta, date

#try except for accounts
accountnum = input("What is your account ID? (ex: 11111) ")
try:
    f = open("accounts.csv","r")
    accounts =  f.read()
    if accountnum in accounts:
        if len(accountnum) == 5:
            print("thank you for logging in.")
            allowed = "yes"
        else:
            print("Your account ID is 5 digits long. Please put in full number.")
    else:
        print("account not found.")
    f.close()
except:
    print("error")
    exit()

try:
    if allowed != "yes":
        exit()
except:
    print("please log in to edit or see the data base.")
    newaccount = input("would you like to create an account? ")
    if newaccount == "yes":
        #creates new account
        accounts = open("accounts.csv","a")
        generate = random.random()
        generate = generate * 100000
        generate = int(generate)
        print(f"your new account id is {generate}")
        accounts.write(" "  + str(generate) + ",")
        print("log in again to edit database.")
        exit()
    else:
        exit()

checkout = input("would you like to check out a book? ")

#add account-specific info
if checkout == "yes":
    a = "see"
else:
    returnchoice = input("would you like to return a book? ")
    if returnchoice == "yes":
        f = open("library.csv")
        books = f.read()
        book = input("what book are you returning? ")
        if book in books:
            s = books.index(book)
            n = books[:s]
            s = books[s:]
            p = s.index(",")
            try:
                x = s.index("\n")
            except:
                x = -1
            t = s[p+2:x]
            if "open" not in t: 
                print(f"Book found in database.")
                file = n + s[:p+2] +""+ "open," + s[x:]
                f.close()
                f = open("library.csv","w")
                f.write(file)
                print("your book was successfully returned. Thank you for using this library.")
                exit()
            else:
                print(f"book is not checked out.")
                exit()
        else:
            print(f"we don't own any copies of {book}.")
            donation = input("would you like to donate a book?")
            if donation == "yes":
                a = "add"
            else:
                exit()
    elif accountnum == "66666":
        a = input("see, add, edit, or delete? ").lower()
    else:
        print("You do not have admin permissions. You do not have any other options available to you at this time.")
        exit()


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
    d = input("is this book checked out right now? ")
    if d == "yes":
        d = input("what is the due date of this book (dd/mm) ? ")
        d = " " + d
    else:
        d = " open"
    b.write("," + d + ", ")
#edit works
elif a == "edit":
    b = open("library.csv","r")
    c = b.read()
    d = input("What book would you like to edit? ").lower()
    i = input("would you like to edit the name or date due? ").lower()
    e = input("what would you like to edit it to? ")
    if i == "name":
        if d in c:
            p = c.index(d)
            x = slice(p,p+len(d))
            o = open("library.csv","r+")
            g = o.read()
            l = slice(0,p)
            h = slice(len(d)+p+1,-1)
            u = g[l] + e + ', ' + g[h] + ","
            s = open("library.csv","w")
            s.write(u)
            print("book edited")
    elif i == "date" or "date due":
        g = open("library.csv")
        g = g.read()
        p = g.index(d)
        x = slice(p,-1)
        o = g[x].index(",")
        n = slice(o)
        o = o + p
        h = slice(0,o)
        u = slice(o+6,-1)
        s = g[h] +", "+ e +""+ g[u] + ","
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

#book checkout function
if checkout == "yes":
    book = input("what book would you like to check out from the list? ")
    f = open("library.csv")
    books = f.read()
    if book in books:
        print("book found")
        s = books.index(book)
        n = books[:s]
        s = books[s:]
        p = s.index(",")
        try:
            x = s.index("\n")
        except:
            x = -1
        t = s[p+2:x]
        if "open" in t:
            #date due
            print(f"book available. Checking out {book}")
            today = datetime.datetime.now()
            r = date.today() + timedelta(days = 5)
            print(f"Your book is due on {r.strftime('%m') +'/'+ r.strftime('%d')}")
            file = n + s[:p+2] +""+ r.strftime('%m') + '/' + r.strftime('%d') + f", {accountnum},"+ s[x:]
            f.close()
            f = open("library.csv","w")
            f.write(file)
        else:
            print(f"book is currently taken. It will be back by {t}")