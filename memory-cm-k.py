import random, time, os 

items = list("aabbccddeeffgghh")
random.shuffle(items)
items = [items[:4], items[4:8], items[8:12], items[12:]]

def show_items():
    os.system("clear")
    for r in range(len(items)):
        time.sleep(0.05)
        for c in range(len(items[0])):
            print(items[r][c], end =" , ")
        print()
print("Try to memorise.....")
time.sleep(1)
show_items()
time.sleep(3)
 
board = []
def make_board():
    for r in range(4):
        board.append([])
        for c in range(4):
            board[r].append("*")
make_board()

def show_board(items):
	row = -1
	os.system("clear")
	print("  ",0,"   ",1,"  ",2,"  ",3)
	for r in range(len(board)):
		row += 1
		time.sleep(0.05)
		print(row,board[r], end = " ")
		print()
attemps = 0 
correct = 0 
running = True
while running:
    show_board(items)
    r,c = map(int, input("Guess row and column: "))
    if (r,c) != int:
    	print("wrong entry, try again")
    board[r][c] = items[r][c]
    show_board(items)
    r2,c2 = map(int, input("Guess row and columns: "))
    board[r2][c2] = items[r2][c2]
    show_board(items)
    time.sleep(1)
    attemps += 1
    if board[r][c] == board[r2][c2]:
        correct += 1
        print("correct")
        time.sleep(1)

    else:
        print("Wrong try again!")
        time.sleep(2)
        board[r][c] = "*"
        board[r2][c2] = "*"
        show_board(items)
    if correct == 9:
        print("congrats! you fixed the puzzle in ",attemps, "attemps")
        time.sleep(2)
    
