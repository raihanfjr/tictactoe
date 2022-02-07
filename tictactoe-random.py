from tkinter import *
import random

root = Tk()
root.title('Tic Tac Toe')

turn = 1
status = "Please pick a block"
winner = "Draw"

#winning condition for player to win the game
winning_condition = [
                    [[0,0],[0,1],[0,2]],
                    [[1,0],[1,1],[1,2]],
                    [[2,0],[2,1],[2,2]],
                    [[0,0],[1,0],[2,0]],
                    [[0,1],[1,1],[2,1]],
                    [[0,2],[1,2],[2,2]],
                    [[0,0],[1,1],[2,2]],
                    [[0,2],[1,1],[2,0]],
                    ]
#game condition
gc = [
        [[],[],[]],
        [[],[],[]],
        [[],[],[]],
    ]
#available condition
ac = [
    [0,0],[0,1],[0,2],
    [1,0],[1,1],[1,2], 
    [2,0],[2,1],[2,2]
    ]

color = 1

#function to check if a player complete the winning condition
def stop_game():
    global winner
    a1.config(state="disabled")
    a2.config(state="disabled")
    a3.config(state="disabled")
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    c1.config(state="disabled")
    c2.config(state="disabled")
    c3.config(state="disabled")
    winner_text = "Winner: Player " + winner 
    labelwinner.config(text=winner_text)
    
#function execute player's turn
def finish_turn(row, column):
    global turn, status, winner
    if(turn % 2 == 0):
        player = "O"
    else:
        player = "X"
    
    status = "Player " + player + " pick block[" + str(row) + "," + str(column) + "]"
    print(status)

    #remove available condition
    ac.remove([row,column])

    gc[row][column] = player
    for wc in winning_condition:
        if(gc[wc[0][0]][wc[0][1]] == player):
            if(
                gc[wc[0][0]][wc[0][1]] == gc[wc[1][0]][wc[1][1]] and 
                gc[wc[0][0]][wc[0][1]] == gc[wc[2][0]][wc[2][1]] and
                gc[wc[1][0]][wc[1][1]] == gc[wc[2][0]][wc[2][1]]):
                winner = player

    #if winner found, game will be stopped
    if(winner!="Draw"):
        stop_game()
    
    turn = turn + 1

    #click the recommended corresponding button for bot
    if(len(ac)>0 and turn % 2 == 0):
        rc = ac[random.randint(0,len(ac)-1)]
        if(rc[0]==0 and rc[1]==0):
            a1_click()
        elif(rc[0]==0 and rc[1]==1):
            a2_click()
        elif(rc[0]==0 and rc[1]==2):
            a3_click()
        if(rc[0]==1 and rc[1]==0):
            b1_click()
        elif(rc[0]==1 and rc[1]==1):
            b2_click()
        elif(rc[0]==1 and rc[1]==2):
            b3_click()
        elif(rc[0]==2 and rc[1]==0):
            c1_click()
        elif(rc[0]==2 and rc[1]==1):
            c2_click()
        elif(rc[0]==2 and rc[1]==2):
            c3_click()
    
    return player

#function to change color based on player turn
def fgcolor():
    global color
    if(color==9):
        fgc = "blue"
    elif(color % 2 == 0):
        fgc = "blue"
    else:
        fgc = "red"
    color = color + 1
    return fgc

#function to execute a button
def a1_click():
    global a1
    a1.config(text=finish_turn(0, 0), state="disabled", disabledforeground=fgcolor())

def a2_click():
    global a2
    a2.config(text=finish_turn(0, 1), state="disabled", disabledforeground=fgcolor())

def a3_click():
    global a3
    a3.config(text=finish_turn(0, 2), state="disabled", disabledforeground=fgcolor())

def b1_click():
    global b1
    b1.config(text=finish_turn(1, 0), state="disabled", disabledforeground=fgcolor())

def b2_click():
    global b2
    b2.config(text=finish_turn(1, 1), state="disabled", disabledforeground=fgcolor())

def b3_click():
    global b3
    b3.config(text=finish_turn(1, 2), state="disabled", disabledforeground=fgcolor())

def c1_click():
    global c1
    c1.config(text=finish_turn(2, 0), state="disabled", disabledforeground=fgcolor())

def c2_click():
    global c2
    c2.config(text=finish_turn(2, 1), state="disabled", disabledforeground=fgcolor())

def c3_click():
    global c3
    c3.config(text=finish_turn(2, 2), state="disabled", disabledforeground=fgcolor())

#tic tac toe label
label = Label(root, text = "Tic Tac Toe", width=10)
label.grid(row=0, column=2)

#dynamic label to see current winner
labelwinner = Label(root, text = "Winner: Draw", width=15)
labelwinner.grid(row=1, column=2)

#tic tac toe button
a1 = Button(root, text="A1", command=lambda: a1_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
a1.grid(row=2, column=1, padx=7, pady=5)

a2 = Button(root, text="A2", command=lambda: a2_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
a2.grid(row=2, column=2, padx=7, pady=5)

a3 = Button(root, text="A3", command=lambda: a3_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
a3.grid(row=2, column=3, padx=7, pady=5)

b1 = Button(root, text="B1", command=lambda: b1_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
b1.grid(row=3, column=1, padx=7, pady=5)

b2 = Button(root, text="B2", command=lambda: b2_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
b2.grid(row=3, column=2, padx=7, pady=5)

b3 = Button(root, text="B3", command=lambda: b3_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
b3.grid(row=3, column=3, padx=7, pady=5)

c1 = Button(root, text="C1", command=lambda: c1_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
c1.grid(row=4, column=1, padx=7, pady=5)

c2 = Button(root, text="C2", command=lambda: c2_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
c2.grid(row=4, column=2, padx=7, pady=5)

c3 = Button(root, text="C3", command=lambda: c3_click(), width=6, height=4, activeforeground ="white", activebackground="grey")
c3.grid(row=4, column=3, padx=7, pady=5)


root.mainloop()
