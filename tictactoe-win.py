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
#possible winning condition left for computer
possible_wc = winning_condition[:]

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

#function for bot to execute the available winning condition
def bot_winning_solution():
    global rc, current_wc, runned_wc, possible_wc
    #if current winning condition plan is not possible anymore change winning condition plan
    if(current_wc not in possible_wc):
        current_wc = possible_wc[random.randint(0, len(possible_wc)-1)][:]
        runned_wc = current_wc[:]
        for x in runned_wc[:]:
            if(x not in ac):
                runned_wc.remove(x)
        picked = random.randint(0,len(runned_wc)-1)
        rc = runned_wc[picked]
        return rc
    #if current winning condition plan is still possible
    else:
        for x in runned_wc[:]:
            if(x not in ac):
                runned_wc.remove(x)
        picked = random.randint(0,len(runned_wc)-1)
        rc = runned_wc[picked]
        return rc

#function for bot to execute the available preventing the other winning condition (draw)
def bot_drawing_solution():
    global rc, opponent_wc, ocurrent_wc, orunned_wc
    ocurrent_wc = opponent_wc[random.randint(0, len(opponent_wc)-1)][:]
    orunned_wc = ocurrent_wc[:]
    for x in orunned_wc[:]:
        if(x not in ac):
            orunned_wc.remove(x)
    picked = random.randint(0,len(orunned_wc)-1)
    rc = orunned_wc[picked]
    orunned_wc.pop(picked)
    return rc

#function for bot to prepare plan such as: winning condition and opponent winning condition
def bot_prepare_move(row, column):
    global current_wc, runned_wc, possible_wc
    global ocurrent_wc, orunned_w, opponent_wc
    remove_wc = []; oremove_wc = []
    #prepare winning condition plan
    for i in range(len(possible_wc)):
        for j in range(len(possible_wc[i])):
            if(possible_wc[i][j]==[row, column]):
                remove_wc.append(possible_wc[i])
                break
    for rwc in remove_wc[:]:
        possible_wc.remove(rwc)

    #prepare opponent winning condition plan
    for i in range(len(winning_condition)):
        for j in range(len(winning_condition[i])):
            if(winning_condition[i][j]==[row, column] and winning_condition[i] not in opponent_wc):
                opponent_wc.append(winning_condition[i])
                break
    
    for i in range(len(opponent_wc)):
        for j in range(len(opponent_wc[i])):
            if(gc[opponent_wc[i][j][0]][opponent_wc[i][j][1]]=="O"):
                oremove_wc.append(opponent_wc[i])
                break

    for orwc in oremove_wc[:]:
        opponent_wc.remove(orwc)

    return possible_wc, opponent_wc

#function for bot to execute its first move
def bot_first_move():
    current_wc = possible_wc[random.randint(0, len(possible_wc)-1)][:]
    runned_wc = current_wc[:]
    picked = random.randint(0,len(runned_wc)-1)
    rc = runned_wc[picked]
    runned_wc.pop(picked)
    return rc, current_wc, runned_wc

#function execute player's turn
def finish_turn(row, column):
    global turn, status, winner, rc
    global current_wc, runned_wc, possible_wc
    global ocurrent_wc, orunned_w, opponent_wc
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
    
    if(turn == 1):
        opponent_wc = []
    
    turn = turn + 1

    #if available condition still exist and robot turn
    if(len(ac)>0 and turn % 2 == 0):
        possible_wc, opponent_wc = bot_prepare_move(row, column)

        #if robot first turn
        if(turn == 2):
            rc, current_wc, runned_wc = bot_first_move()
        
        #if both possible winning condition and opponent winning condition still exist
        elif(len(possible_wc)>0 and len(opponent_wc)>0):
            if(random.randint(0,1)==1):
                rc = bot_winning_solution()
            else:
                rc = bot_drawing_solution()

        #if possible winning condition still exist
        elif(len(possible_wc)>0):
            rc = bot_winning_solution()

        #if possible winning condition is not exist and opponent winning condition still exist
        elif(len(possible_wc)==0 and len(opponent_wc)>0):
            rc = bot_drawing_solution()
            
        #if there is no way of winning and losing    
        else:
            rc = ac[random.randint(0,len(ac)-1)]

        #click the recommended corresponding button for bot
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
