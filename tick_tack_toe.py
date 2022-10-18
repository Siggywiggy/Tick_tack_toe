class Gameboard:
    def __init__(self, rounds=3):

        self.name = "Gameboard"
        self.board_rows = [
            {1: ["_", "_", "_"]},
            {2: ["_", "_", "_"]},
            {3: ["_", "_", "_"]},
        ]
        self.rounds = rounds

    def __repr__(self):

        return "{p1_name} and {p2_name}, lets play a game of Tick-tack-toe for {rounds} rounds! \n{p1_name} your mark will be [{p1_icon}] and {p2_name} yours will be [{p2_icon}] ".format(
            p1_name=player_1.player_name,
            p2_name=player_2.player_name,
            rounds=self.rounds,
            p1_icon=player_1.player_icon,
            p2_icon=player_2.player_icon,
        )

    def draw_board(self):

        board_separator_bar = "{=====}"
        column_separator = "|"

        print(board_separator_bar)
        for row_dict in self.board_rows:
            for row_list in row_dict.values():
                joined_row = column_separator.join(row_list)
                print(column_separator + joined_row + column_separator)
        print(board_separator_bar)
        return


class Player:
    def __init__(self, player_name, player_icon):
        self.player_name = player_name
        self.player_score = 0
        self.player_icon = player_icon


input_name1 = input("First player, enter your name: ")
player_1 = Player(input_name1, "x")

input_name2 = input("Second player, enter your name: ")
player_2 = Player(input_name2, "o")


new_board = Gameboard(5)
print(new_board)

new_board.draw_board()
