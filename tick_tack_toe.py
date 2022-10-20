class Gameboard:
    def __init__(self, num_of_matches=1):

        self.name = "Gameboard"
        self.board_rows = {
            1: ["_", "_", "_"],
            2: ["_", "_", "_"],
            3: ["_", "_", "_"],
        }
        self.rounds = num_of_matches

    def __repr__(self):

        return "{p1_name} and {p2_name}, lets play a game of Tick-tack-toe for {rounds} rounds! \n{p1_name}, your mark will be [{p1_icon}] and {p2_name}, yours will be [{p2_icon}]".format(
            p1_name=player_1.player_name,
            p2_name=player_2.player_name,
            rounds=self.rounds,
            p1_icon=player_1.player_icon,
            p2_icon=player_2.player_icon,
        )

    def draw_board(self):
        header_bar = " {=====}\n [1_2_3]"
        bottom_bar = " {=====}"
        column_separator = "|"
        print(header_bar)
        # going trough all 1-3 key:value pairs, printing the key and the values as joined strings for visual representation
        for k, v in self.board_rows.items():
            joined_row = column_separator.join(v)
            print(str(k) + column_separator + joined_row + column_separator)
        print(bottom_bar)
        return


class Player:
    def __init__(self, player_name, player_icon="x"):
        self.player_name = player_name
        self.player_score = 0
        self.player_icon = player_icon
        self.player_moves = []
        # self.column_choice = 0
        # self.row_choice = 0

    def prompt_move(self):

        self.row_choice = input(
            "{name}, choose the row of your move 1-2-3: ".format(name=self.player_name)
        )
        self.column_choice = input(
            "{name}, choose the column of your move 1-2-3: ".format(
                name=self.player_name
            )
        )

        self.check_move()
        self.column_choice = int(self.column_choice)
        self.row_choice = int(self.row_choice)
        print("You chose row ", self.row_choice)
        print("You chose column ", self.column_choice)
        self.input_move_on_board()

    def check_move(self):

        try:
            int(self.column_choice)
        except ValueError:
            print("Column choice not a number!")
            self.prompt_move()

        try:
            int(self.row_choice)
        except ValueError:
            print("Row choice not a number!")
            self.prompt_move()

    # Needs more work on if the player enters nothing

    def input_move_on_board(self):
        self.data_input_column_choice = self.column_choice - 1
        self.data_input_row_choice = self.row_choice
        print("dict key ", self.data_input_row_choice)
        print("list index", self.data_input_column_choice)
        if self.data_input_column_choice not in range(0, 3):
            print("Your column choice is out of 1-2-3 range! Choose your move again!")
            self.prompt_move()

        elif self.data_input_row_choice not in new_board.board_rows.keys():
            print("Your row choice is out of 1-2-3 range! Choose your move again!")
            self.prompt_move()

        elif (
            new_board.board_rows[self.data_input_row_choice][
                self.data_input_column_choice
            ]
            != "_"
        ):
            print("There is already a mark there!")
            self.prompt_move()
        else:
            new_board.board_rows[self.data_input_row_choice][
                self.data_input_column_choice
            ] = self.player_icon
            player_moves.append([self.data_input_row_choice -1, self.data_input_column_choice])

    def determine_winning(self):
    
        # credit for logic https://jayeshkawli.ghost.io/tic-tac-toe/
        player_moves_list = self.player_moves
        player_won = False

        def check_win_rows(self):
        
            for row_num in range(0,3): #row = 0, row = 1, row = 2
                 # Adding all player moves with 0 index = row to a list
                row_container = [1 for player_move in player_moves_list if player_move[0] == row_num]
                # Checking if player has made 3 moves in one row and returning True if so - player won
                if sum(row_container) == 3:
                    print(f'{self.player_name} won by row!')
                    return player_won = True   
                else:
                    continue
    
        def check_win_columns(self):

            for column_num in range(0,3): #column = 0, column = 1, column = 2
                # Adding all player moves with 1 index = column to a list
                column_container = [1 for player_move in player_moves_list if player_move[1] == column_num]
                # Checking if player has made 3 moves in one column and returning True if so - player won
                if sum(column_container) == 3:
                    print(f'{self.player_name} won by column!')
                    return player_won = True    
                else:
                    continue
    
        def check_digonal(self):

            # Adding a "1" to a list if a player move had equal x and y "coordinates" - moves 1:1, 2:2, 3:3
            diagonal_container = [1 for player_move in player_moves_list if player_move[0] == player_move[1]]

            if sum(diagonal_container) == 3:
                print(f'{self.player_name} won by diagonal!')
                return player_won = True  
            else:
                continue
    
        def check_opposite_diagonal(self):
            #if moves are 0:2, 1,1 and 2,0 - opposite diagonal, then x + y + 1 = 3 so filtering these moves matching this condition out to a container 
            opposite_diagonal_container = [1 for player_move in player_move_list if player_move[0] + player_move[1] + 1 == 3]

            if sum(opposite_diagonal_container) == 3:
                print(f'{self.player_name} won by opposite diagonal!')
                return player_won = True 
            else:
                continue
        
        check_win_rows(self.player_moves_list)
        check_win_columns(self.player_moves_list)
        check_digonal(self.player_moves_list):
        check_opposite_diagonal(self.player_moves_list)

        return player_won






# Entering a number of matches the players want to play and checking if the match count is a valid number

num_of_matches = input(
    "Welcome to a game of Tick-Tack-Toe, choose how many rounds you want to play: "
)

try:
    num_of_matches = int(num_of_matches)

except ValueError:
    print("Not a number! Quitting game")
    quit()

# Players entering their name and player objects getting instantiated

input_name1 = input("First player, enter your name: ")
player_1 = Player(input_name1, "x")

input_name2 = input("Second player, enter your name: ")
player_2 = Player(input_name2, "o")

new_board = Gameboard(num_of_matches)
print(new_board)

# https://jayeshkawli.ghost.io/tic-tac-toe/
new_board.draw_board()

player_1.prompt_move()
new_board.draw_board()

player_2.prompt_move()
new_board.draw_board()
