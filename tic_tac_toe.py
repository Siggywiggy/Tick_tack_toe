# Tic-tac-toe game


class Gameboard:
    def __init__(self, rounds):

        self.name = "Gameboard"
        self.board_rows = {
            1: ["_", "_", "_"],
            2: ["_", "_", "_"],
            3: ["_", "_", "_"],
        }
        self.rounds = rounds

    def __repr__(self):

        return "{p1_name} and {p2_name}, lets play a game of Tic-tac-toe for {rounds} more rounds! \n{p1_name}, your mark will be [{p1_icon}] and {p2_name}, yours will be [{p2_icon}]".format(
            p1_name=player1.player_name,
            p2_name=player2.player_name,
            rounds=self.rounds,
            p1_icon=player1.player_icon,
            p2_icon=player2.player_icon,
        )

    def draw_board(self):
        header_bar = " {--*--}\n [1_2_3]"
        bottom_bar = " {--*--}"
        column_separator = "|"
        print(header_bar)
        # going trough all 1-3 key:value pairs, printing the key and the values as joined strings for visual representation
        for k, v in self.board_rows.items():
            joined_row = column_separator.join(v)
            print(str(k) + column_separator + joined_row + column_separator)
        print(bottom_bar)
        return

    def redraw_board(self):
        for move in player1.player_moves:
            x_coord = move[0] + 1
            y_coord = move[1]
            self.board_rows[x_coord][y_coord] = player1.player_icon
        for move_2 in player2.player_moves:
            x_coord = move_2[0] + 1
            y_coord = move_2[1]
            self.board_rows[x_coord][y_coord] = player2.player_icon

    def reset_board(self):
        game.board_rows = {
            1: ["_", "_", "_"],
            2: ["_", "_", "_"],
            3: ["_", "_", "_"],
        }


class Player:
    def __init__(self, player_name, player_icon="x"):
        self.player_name = player_name
        self.player_score = 0
        self.player_icon = player_icon
        self.player_moves = []

    def __repr__(self):
        return f"Player {self.player_name}"

    def prompt_move(self):
        # Outer while loop to check if the player move isnt already done by player1 or player2. If move has already been done returning back to the top of loop to enter a new move
        while True:
            # Inner while loop to check if player input is valid
            while True:
                # Checking if row input is a number and checking if its within rows
                row_choice = input(
                    "{name}, choose the row of your move 1-2-3: ".format(
                        name=self.player_name
                    )
                )

                try:
                    row_choice = int(row_choice) - 1
                except ValueError:
                    print("Row choice not a number! Try again")
                    continue

                if 0 <= row_choice < 3:
                    break
                else:
                    print("Row choice is out of range 1-2-3")

            while True:
                # Checking if column input is a number and checking if its within rows
                column_choice = input(
                    "{name}, choose the column of your move 1-2-3: ".format(
                        name=self.player_name
                    )
                )

                try:
                    column_choice = int(column_choice) - 1
                except ValueError:
                    print("Column choice not a number! Try again")
                    continue

                if 0 <= column_choice < 3:
                    break
                else:
                    print("Column choice is out of range 1-2-3")

            # Adding verified row and column inputs to a list
            player_move = [row_choice, column_choice]

            # Checking if player move is not within already performed moves
            if (
                player_move not in player1.player_moves
                and player_move not in player2.player_moves
            ):
                self.player_moves.append(player_move)
                break

            else:
                print("There is already a mark there, try again!")
                continue

    def determine_winning(self):

        # credit for logic https://jayeshkawli.ghost.io/tic-tac-toe/
        player_won = False

        # Checking if player has made 3 moves in one row and returning True if so - player won

        for row_num in range(0, 3):  # row = 0, row = 1, row = 2
            row_container = [1 for move in self.player_moves if move[0] == row_num]
            # Checking if player has made 3 moves in one row and returning True if so - player won
            if sum(row_container) == 3:
                self.add_score()
                print(f"{self.player_name} won by row!")
                player_won = True

        # Checking if player has made 3 moves in one column and returning True if so - player won

        for column_num in range(0, 3):  # column = 0, column = 1, column = 2
            column_container = [
                1 for move in self.player_moves if move[1] == column_num
            ]

            if sum(column_container) == 3:
                self.add_score()
                print(f"{self.player_name} won by column!")
                player_won = True

        # Container for moves that are 1,1, 2,2, 3,3

        diagonal_container = [1 for move in self.player_moves if move[0] == move[1]]

        if sum(diagonal_container) == 3:
            self.add_score()
            print(f"{self.player_name} won by diagonal!")
            player_won = True

        # if moves are 0:2, 1,1 and 2,0 - opposite diagonal, then x + y + 1 = 3 so filtering these moves matching this condition out to a container
        opposite_diagonal_container = [
            1 for move in self.player_moves if move[0] + move[1] + 1 == 3
        ]

        if sum(opposite_diagonal_container) == 3:
            self.add_score()
            print(f"{self.player_name} won by opposite diagonal!")
            player_won = True

        # Returning if the player instance has met winning condition
        return player_won

    def add_score(self):
        self.player_score += 1

    def reset_moves(self):
        self.player_moves = []


# Entering a number of matches the players want to play and checking if the match count is a valid integrer
def get_num_matches():

    while True:
        num_of_matches = input(
            "Welcome to a game of Tic-Tac-Toe, choose how many rounds you want to play: "
        )

        try:
            num_of_matches = int(num_of_matches)
        except ValueError:
            print("Not a number! Enter a number!")
            continue

        if num_of_matches > 0:
            break
        else:
            print("Choose a number larger then 0")

    return num_of_matches

    # Function returning a list of player names


def get_player_names():
    player_names_list = []
    input_name_1 = input("First player, enter your name: ")
    player_names_list.append(input_name_1)
    input_name_2 = input("Second player, enter your name: ")
    player_names_list.append(input_name_2)
    return player_names_list


def play_round():

    move_counter = 0

    while True:

        game.draw_board()

        player1.prompt_move()
        move_counter += 1
        # print(f"{move_counter}th move")
        game.redraw_board()
        if player1.determine_winning() is True:
            # player1.add_score()
            print(f"{player1.player_name} won this round!")
            break

        # Checking if move counter isnt 9 already and no winner could be determined beforehand from previous if sentence
        if move_counter == 9:
            print("Its a tie!")
            break

        game.draw_board()
        player2.prompt_move()
        move_counter += 1
        # print(f"{move_counter}th move")
        game.redraw_board()

        if player2.determine_winning() is True:
            print(f"{player2.player_name} won this round!")
            # player1.add_score()
            break

        # Checking if move counter isnt 9 already and no winner could be determined beforehand from previous if sentence
        if move_counter == 9:
            print("Its a tie!")
            break

    return


# Getting players input for player names
player_names = get_player_names()

# Instantiating player classes
player1 = Player(player_names[0], "x")
player2 = Player(player_names[1], "o")


number_of_matches = get_num_matches()

game = Gameboard(number_of_matches)
print(game)

for num in range(0, game.rounds):
    play_round()
    game.reset_board()
    player1.reset_moves()
    player2.reset_moves()

print(
    f"Final tally: {player1.player_name} won {player1.player_score} times and {player2.player_name} won {player2.player_score} times. \nThanks for playing!"
)
