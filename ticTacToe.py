"""
tic tac toe

-> create a board .
[
    [_, _, _],
    [_, _, _], -> 9 slots 
    [_, _, _]
]

-> maximum 2 users.
-> equal chances almost(that the plyer who is staring have a maximum of 5 and the other player has only 4 chances.)
-> column wise, row wise and diagonal wise winning.
-> can't over write.
-> can play multiple game with points added in each game.
"""






score_list_x = []
score_list_o = []

def game():
    board = [                   # this list showing 1,2,3 etc 
                                # so that we access these values by just inputing the number'ss for eg if input 2 -> list[1]
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
    ]


    def printing():
        for i in board:
            for x in i:
                print(f" |{x}| ",end = "") 
            print()


    def quit(x): # This funcion helps us to quite while playing.....
        if x in "qQ": 
            print("Thanks for playing.....")
            return True
        else: 
            return False
        

    def check_number(user_input):
        if user_input.isdigit():
            return False
        else:
            print("Please input a number between(1-9)")
            return True


    def Maximum(user_input):
        int_value = int(user_input) #converting to integer for checking weather the number is eligible for execution...
        if int_value >=10:
            print(f"The number {int_value} is too big")
            print("Type the number between 1-9")
            return True
        elif int_value < 1:
            print(f"The number {int_value} is too small")
            print("Enter the number between 1-9.")
            return True
        else:
            False


    def add_x(user_input):
        while True:
            choosing_player = "x"
            x = int(user_input)
            new_int = x-1
            if new_int < 3:
                row = 0
                board[row][new_int] = choosing_player
                return True
                    
            elif new_int >= 3 and new_int < 6:
                if new_int == 3:
                    new_int -= 3
                    row = 1
                    board[row][new_int] = choosing_player
                    return True
                    
                elif new_int == 4:
                    new_int -= 3
                    row = 1
                    board[row][new_int] = choosing_player
                    return True
                elif new_int == 5:
                    new_int -= 3
                    row = 1
                    board[row][new_int] = choosing_player
                    return True
            
            elif new_int >= 6:
                if new_int == 6:
                    new_int -= 6
                    row = 2
                    board[row][new_int] = choosing_player
                    return True
                elif new_int == 7:
                    new_int -= 6
                    row = 2
                    board[row][new_int] = choosing_player
                    return True
                elif new_int == 8:
                    new_int -= 6
                    row = 2
                    board[row][new_int] = choosing_player
                    return True


    def add_o(user_input):

        choosing_player2 = "o"
        x = int(user_input)
        new_int = x-1
        
        while True:
            if new_int < 3:
                row = 0
                board[row][new_int] = choosing_player2
                return True
                    
            elif new_int >= 3 and new_int < 6:
                if new_int == 3:
                    new_int -= 3
                    row = 1
                    board[row][new_int] = choosing_player2
                    return True
                    
                elif new_int == 4:
                    new_int -= 3
                    row = 1
                    board[row][new_int] = choosing_player2
                    return True     
                elif new_int == 5:
                    new_int -= 3
                    row = 1
                    board[row][new_int] = choosing_player2
                    return True
            
            elif new_int >= 6:
                if new_int == 6:
                    new_int -= 6
                    row = 2
                    board[row][new_int] = choosing_player2
                    return True
                elif new_int == 7:
                    new_int -= 6
                    row = 2
                    board[row][new_int] = choosing_player2
                    return True
                elif new_int == 8:
                    new_int -= 6
                    row = 2
                    board[row][new_int] = choosing_player2
                    return True
    
    def score(x,score_list_x, score_list_o):
        if x in "x":
            point = 1
            score_list_x.append(point)
        elif x in "o":
            point = 1
            score_list_o.append(point)

    def winning(): # This funtion helps us to check a player won in all possibility
        if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
            print(board[0][1],"won the match.........")
            x = board[0][1]
            score(x,score_list_x,score_list_o)
            return True
        elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
            print(board[1][0],"won the match.........")
            x = board[1][0]
            score(x,score_list_x,score_list_o)
            return True
        elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
            print(board[2][0],"won the match.........")
            x = board[2][0]
            score(x,score_list_x,score_list_o)
            return True 
        elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
            print(board[0][0],"won the match.........")
            x = board[0][0]
            score(x,score_list_x,score_list_o)
            return True
        elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
            print(board[0][1],"won the match.........")
            x = board[0][1]
            score(x,score_list_x,score_list_o)
            return True
        elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
            print(board[0][2],"won the match.........")
            x = board[0][2]
            score(x,score_list_x,score_list_o)
            return True
        elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            print(board[0][2],"won the match.........")
            x = board[0][2]
            score(x,score_list_x,score_list_o)
            return True
        elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print(board[0][0],"won the match.........")
            x = board[0][0]
            score(x,score_list_x,score_list_o)
            return True
        
        else:
            return False

    def occupied_slot(): # helps us find weather the slot is occupied
        new_value = int(user_input)
        new_value -= 1
        
        if new_value < 3: 
            if board[0][new_value] in  "xo":
                return True
        elif new_value < 6:
            new_value -= 3
            if board[1][new_value] in  "xo":
                return True
        elif new_value < 10:
            new_value -= 6
            if board[2][new_value] in  "xo":
                return True
        else:

            return False



    chance = 0
    limit = 0

    while True:
        first_chance = input("choose who is going to play first(x/o) : ")
        if first_chance in "XxOo":
            print(first_chance," is going to play first")
            break
        else:
            print("invalid input")
            continue

    while limit <= 8: # its 8 because initial value of limit is 0. therefore the loop will go once when the limit before its value changes from 0 -> 1. 
        if winning():
            break
        printing()
        user_input = input("Enter number from 1-9 : ")
        if occupied_slot():
            print("occupied")
            continue
        if quit(user_input):break
        if check_number(user_input): continue
        if Maximum(user_input):continue
        while chance < 1:
            if first_chance in "xX":
                chance += 1
                break
            elif first_chance in "oO":
                chance += 2
                break

        key = True
        while key == True:
            if chance %2 == 0:
                chance += 1
                limit += 1 
                if add_o(user_input):

                    key = False          
            else:
                chance += 1
                limit += 1
                if add_x(user_input): 

                    key = False
    if limit >= 9:
        if winning():print("Thank you for playing...")
        else:
            print("No one won, Game over")
            print("Thank you for playing....")
    else:print("Thank you for playing")
    
while True:
    print("Welcome to tic tac toe")
    game()
    x_score = len(score_list_x)
    o_score = len(score_list_o)
    print(f"""
Score board:
 -------
|x -> {x_score}|
|o -> {o_score}|
 -------
""")
    Play_again = input("Do you want to contine(y/n) : ")
    if Play_again in "Nn":
        print("Thank you for using this program....")
        break
