board1 = "_|_|_ \n"
board2 = "_|_|_ \n"
board3 = " | | \n"
print(board1 + board2 + board3)
game = "not won"
turn = 0

while game != "won":
    line = input("which line would you like to place your X or O in? ").upper()
    column = input("which column would you like to place your X or O in? ").upper()

    if turn%2 == 0:
        x = "x"
    else:
        x = "o"

    if line == 1 or "TOP":
        board = str(board1)
    elif line == 2 or "MIDDLE":
        board = str(board2)
    else:
        board = str(board3)  

    if column == 1:
        column = 0
    elif column == 3:
        column = 4

    a = board[:int(column)-1]
    b = board[int(column):]
        
    row = a+x+b

    if line == 1 or "TOP":
        board1 = row
    elif line == 2 or "MIDDLE":
        board2 = row
    else:
        board3 = row    

    print(board1 + board2 + board3)