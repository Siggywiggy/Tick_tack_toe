class Gameboard:
    def __init__(self):

        self.name = "Gameboard"
        self.board_rows = {
            1: ["_", "_", "_"],
            2: ["_", "_", "_"],
            3: ["_", "_", "_"],
        }
        self.rounds = 1

    def __repr__(self):

        return "{p1_name} and {p2_name}, lets play a game of Tick-tack-toe for {rounds} more rounds! \n{p1_name}, your mark will be [{p1_icon}] and {p2_name}, yours will be [{p2_icon}]".format(
            p1_name=player1.player_name,
            p2_name=player2.player_name,
            rounds=self.rounds,
            p1_icon=player1.player_icon,
            p2_icon=player2.player_icon,
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

    def match_ended(self):
        if player1.determine_winning() is True or player2.determine_winning() is True:
            return True
        else:
            return False

    def board_full(self):
        if "_" not in self.board_rows.values():
            print("No winner this round!")
            return True
        else:
            return False


class Player:
    def __init__(self, player_name, player_icon="x"):
        self.player_name = player_name
        self.player_score = 0
        self.player_icon = player_icon
        self.player_moves = []

    def __repr__(self):
        return f"Player {self.player_name}"

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
        # https://stackoverflow.com/questions/5557937/how-do-i-use-try-except-or-if-else-to-validate-user-input
        self.data_input_column_choice = self.column_choice - 1
        self.data_input_row_choice = self.row_choice
        print("dict key ", self.data_input_row_choice)
        print("list index", self.data_input_column_choice)
        if self.data_input_column_choice not in range(0, 3):
            print("Your column choice is out of 1-2-3 range! Choose your move again!")
            self.prompt_move()

        elif self.data_input_row_choice not in game.board_rows.keys():
            print("Your row choice is out of 1-2-3 range! Choose your move again!")
            self.prompt_move()

        elif (
            game.board_rows[self.data_input_row_choice][self.data_input_column_choice]
            != "_"
        ):
            print("There is already a mark there!")
            self.prompt_move()
        else:
            game.board_rows[self.data_input_row_choice][
                self.data_input_column_choice
            ] = self.player_icon
            self.player_moves.append(
                [self.data_input_row_choice - 1, self.data_input_column_choice]
            )

    def determine_winning(self):

        # credit for logic https://jayeshkawli.ghost.io/tic-tac-toe/
        player_won = False

        # Checking if player has made 3 moves in one row and returning True if so - player won

        for row_num in range(0, 3):  # row = 0, row = 1, row = 2
            row_container = [1 for move in self.player_moves if move[0] == row_num]
            # Checking if player has made 3 moves in one row and returning True if so - player won
            if sum(row_container) == 3:
                print(f"{self.player_name} won by row!")
                player_won = True

        # Checking if player has made 3 moves in one column and returning True if so - player won

        for column_num in range(0, 3):  # column = 0, column = 1, column = 2
            column_container = [
                1 for move in self.player_moves if move[1] == column_num
            ]

            if sum(column_container) == 3:
                print(f"{self.player_name} won by column!")
                player_won = True

        # Container for moves that are 1,1, 2,2, 3,3

        diagonal_container = [1 for move in self.player_moves if move[0] == move[1]]

        if sum(diagonal_container) == 3:
            print(f"{self.player_name} won by diagonal!")
            player_won = True

        # if moves are 0:2, 1,1 and 2,0 - opposite diagonal, then x + y + 1 = 3 so filtering these moves matching this condition out to a container
        opposite_diagonal_container = [
            1 for move in self.player_moves if move[0] + move[1] + 1 == 3
        ]

        if sum(opposite_diagonal_container) == 3:
            print(f"{self.player_name} won by opposite diagonal!")
            player_won = True

        # Returning if the player instance has met winning condition
        return player_won

    def add_score(self):
        self.player_score += 1


# Entering a number of matches the players want to play and checking if the match count is a valid number
def get_num_matches():
    num_of_matches = input(
        "Welcome to a game of Tick-Tack-Toe, choose how many rounds you want to play: "
    )

    try:
        num_of_matches = int(num_of_matches)
    except ValueError:
        print("Not a number! Quitting game")
        quit()

    return num_of_matches


# Function returning a list of player names
def get_player_names():
    player_names_list = []
    input_name_1 = input("First player, enter your name: ")
    player_names_list.append(input_name_1)
    input_name_2 = input("Second player, enter your name: ")
    player_names_list.append(input_name_2)
    return player_names_list


# Getting players input for number of matches
num_of_matches = get_num_matches()
# Getting players input for player names
player_names = get_player_names()

# Instantiating player classes
player1 = Player(player_names[0], "x")
player2 = Player(player_names[1], "o")


game = Gameboard()

print(game)

for number in range(0, 9):
    game.draw_board()
    player1.prompt_move()
    game.draw_board()
    player2.prompt_move()

    if player1.determine_winning() is True:
        player1.add_score()
        break
    elif player2.determine_winning() is True:
        player2.add_score()
        break


print(player1.player_score)
print(player2.player_score)
