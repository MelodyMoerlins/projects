import random

row_1=[0,0,0,0]
row_2=[0,0,0,0]
row_3=[0,0,0,0]
row_4=[0,0,0,0]


def game():
    global row_1
    global row_2
    global row_3
    global row_4

    rows = [row_1,row_2,row_3,row_4]
    columns = [0,1,2,3]
    row = random.choice(rows)
    col = random.choice(columns)

    def rowsprint():
        print(row_1)
        print(row_2)
        print(row_3)
        print(row_4)

    rowsprint()
    choice = input("Chose your move (w,a,s,d): ")

    if choice == 'w':
        for column in row_4:
            if row_3[column] == 0:
                a = row_4[column]
                row_3[column] = a
                row_4[column] = 0

        for column in row_3:
            if row_2[column] == 0:
                b = row_3[column]
                row_2[column] = b
                row_3[column] = 0

        for column in row_2:
            if row_1[column] == 0:
                c = row_2[column]
                row_1[column] = c
                row_2[column] = 0

    elif choice == 'a':
        for column in row_1:
            if row[column] >= 1:
                if row[column-1]== 0:
                    a = row[column]
                    row[column-1] = a
                    row[column] = 0
        print("a")
    elif choice == 's':
        print("s")
    elif choice == 'd':
        print("d")

    if row[col] == 0:
        row[col] = 2
    else:
        for numbs in row:
            if numbs == 0:
                row[numbs] = 2
                break
    game()
game()